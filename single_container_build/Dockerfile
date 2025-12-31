FROM apache/airflow@sha256:129e6538bbf7e786dce6a8475422aef8c51914cff2011fb8ea3db5433142fa76


USER root
COPY --chown=airflow:airflow dags/ /opt/airflow/dags/
COPY --chown=airflow:airflow single_container_build/init.sh /opt/airflow/
USER airflow
CMD ["bash", "-c", "/opt/airflow/single_container_build/init.sh"]