from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import logging

logger = logging.getLogger("airflow.task")


def argo():

    logging.info("This should be synced from git to kubernetes via argocd")


with DAG(
    dag_id="argo_cd",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["argocd-demo"],
) as dag:

    previous = None

    for i in range(1, 5):
        t = PythonOperator(
            task_id=f"hello_task_{i}",
            python_callable=argo,
        )

        if previous:
            previous >> t
        previous = t
