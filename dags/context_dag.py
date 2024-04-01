import airflow.utils.dates
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
dag = DAG(
 dag_id="context_test",
 start_date=airflow.utils.dates.days_ago(3),
 schedule_interval="@hourly",
)

def _print_context(**context):
	start = context["execution_date"]
	end = context["next_execution_date"]
	print(f"Start: {start}, end: {end}")

print_context = PythonOperator(
 task_id="print_context", python_callable=_print_context, dag=dag
)

print_context