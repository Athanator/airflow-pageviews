import airflow.utils.dates
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from urllib import request
import time
import gzip
import shutil
import requests


dag = DAG(
 dag_id="chapter4_stocksense_bashoperator",
 start_date=airflow.utils.dates.days_ago(3),
 schedule_interval="@hourly",
 template_searchpath="/opt/airflow/data"
)


def _get_data(year, month, day, hour, output_path, **_):
	url = f"https://dumps.wikimedia.org/other/pageviews/{year}/{year}-{month:0>2}/pageviews-{year}{month:0>2}{day:0>2}-{hour:0>2}0000.gz"
	
	pages = requests.get(url=url, allow_redirects=True)
	with open(output_path, 'wb') as f:
		f.write(pages.content)


get_data = PythonOperator(
 task_id="get_data",
 python_callable=_get_data,
 op_kwargs={
 "year": "2024",
 "month": "4",
 "day": "1",
 "hour": "3",
 "output_path": "/opt/airflow/data/wikipageviews.gz",
 },
 dag=dag,
)

# Note: For simplification/test purposes, the datetime parameters (year, month, day, hour) have been defined. For production purposes, the above "get_data" function should be rewriten as follows 
#to get datetime parameters from execution time:

#get_data = PythonOperator(
# task_id="get_data",
 #python_callable=_get_data,
# op_kwargs={
 #"year": "{{ execution_date.year }}", B
 #"month": "{{ execution_date.month }}",
# "day": "{{ execution_date.day }}",
# "hour": "{{ execution_date.hour }}",
# "output_path": "/tmp/wikipageviews.gz",
#},
# dag=dag,
#)


extract_gz = BashOperator(
 task_id="extract_gz",
 bash_command="gunzip --force /opt/airflow/data/wikipageviews.gz",
 dag=dag,
)

def _fetch_pageviews(pagenames, execution_date, **_):
	time.sleep(10)
	result = dict.fromkeys(pagenames, 0)
	with open(f"/opt/airflow/data/wikipageviews", "r") as f:
	 	for line in f:
	 		domain_code, page_title, view_counts, _ = line.split(" ")
	 		if domain_code == "en" and page_title in pagenames:
	 			result[page_title] = view_counts
	
	with open("/opt/airflow/data/postgres_query.sql", "w") as f:
		for pagename, pageviewcount in result.items():
			f.write(
				"INSERT INTO pageview_counts VALUES ("
 f"'{pagename}', {pageviewcount}, '{execution_date}'"
 ");\n"
 )



fetch_pageviews = PythonOperator(
 task_id="fetch_pageviews",
 python_callable=_fetch_pageviews,
 op_kwargs={
 "pagenames": {
 "Google",
 "Amazon",
 "Apple",
 "Microsoft",
 "Facebook",
 }
 },
 dag=dag,
)

create_table = PostgresOperator(
        task_id="create_pet_table",
        postgres_conn_id="my_postgres",
        sql="""
            CREATE TABLE IF NOT EXISTS pageview_counts (
 			pagename VARCHAR(50) NOT NULL,
 			pageviewcount INT NOT NULL,
				datetime TIMESTAMP NOT NULL);
          """,
        dag=dag,
    )

write_to_postgres = PostgresOperator(
	task_id="write_to_postgres",
	postgres_conn_id="my_postgres",
	sql="postgres_query.sql",
	dag=dag,
	)
get_data >> extract_gz >> fetch_pageviews >> create_table >> write_to_postgres