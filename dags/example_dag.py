from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
        dag_id="example_dag",
        start_date=datetime(2025, 7, 16),
        description="A simple example DAG",
        schedule_interval="@daily",
        catchup=False
) as dag:

    task1 = BashOperator(
        task_id="say_hello",
        bash_command="echo 'Hello from inside Dockerized Airflow!'"
    )

    task2 = BashOperator(
        task_id="second_task",
        bash_command="echo 'I am the second task'"
    )

    task1 >> task2

    #6f888b4056f76b7ae272d35d490d2b7ba93626d889d13dc5014df47da5b649e8
