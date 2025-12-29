from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import logging

logger = logging.getLogger("airflow.task")


def hello_world():

    logging.info("hello world")
    print("is this working?")


with DAG(
    dag_id="hello_100_tasks",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["k8s-demo"],
) as dag:

    previous = None

    for i in range(1, 20):
        t = PythonOperator(
            task_id=f"hello_task_{i}",
            python_callable=hello_world,
        )

        if previous:
            previous >> t
        previous = t
