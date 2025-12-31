#this maps to python 3.12.12 and airflow version 3.1.5
FROM apache/airflow@sha256:129e6538bbf7e786dce6a8475422aef8c51914cff2011fb8ea3db5433142fa76
USER airflow

# Copy your pinned requirements to container
COPY requirements.txt /opt/airflow/requirements.txt
# pip install them and reference the constraint file
COPY pip_constraints/constraints.txt /opt/airflow/constraints.txt
RUN pip install --no-cache-dir \
  --constraint /opt/airflow/constraints.txt \
  -r /opt/airflow/requirements.txt

#switch back to root
USER root
COPY --chown=airflow:airflow dags/ /opt/airflow/dags/
COPY --chown=airflow:airflow single_container_build/init.sh /opt/airflow/init.sh
# Fix Windows CRLF and make it executable
RUN sed -i 's/\r$//' /opt/airflow/init.sh && chmod +x /opt/airflow/init.sh
#switch back to airflow 
USER airflow

#call custom startup script
CMD ["bash","/opt/airflow/init.sh"]