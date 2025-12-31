#this maps to python 3.12.12 and airflow version 3.1.5
FROM apache/airflow@sha256:129e6538bbf7e786dce6a8475422aef8c51914cff2011fb8ea3db5433142fa76


USER root
#right now I am only copying dags into this image
COPY --chown=airflow:airflow dags/ /opt/airflow/dags/
USER airflow
