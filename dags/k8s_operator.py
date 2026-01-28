from datetime import datetime
from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator

with DAG(
    dag_id="kpo_example_simple",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["kubernetes", "example"],
) as dag:

    run_in_separate_pod = KubernetesPodOperator(
        task_id="run_python_in_pod",
        # Pod basics
        name="python-task-pod",
        namespace="airflow",
        # This is the KEY part — separate image
        image="python:3.11-slim",
        # Command to run inside the container
        cmds=["python", "-c"],
        arguments=[
            "import platform; "
            "print('Hello from a separate pod!'); "
            "print(f'Python version: {platform.python_version()}')"
        ],
        # Logs show up in Airflow UI
        get_logs=True,
        # Cleanup pod after it finishes
        is_delete_operator_pod=True,
        # If Airflow runs inside the cluster
        in_cluster=True,
        # Optional but nice for debugging
        labels={"app": "airflow", "component": "example-task"},
    )
