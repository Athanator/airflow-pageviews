FROM apache/airflow:latest
USER root
RUN apt-get update && \
    apt-get autoremove -yqq --purge && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
USER airflow
ADD --chown=airflow:root requirements.rst .
RUN pip install ipykernel
RUN pip install --no-cache-dir -r requirements.rst