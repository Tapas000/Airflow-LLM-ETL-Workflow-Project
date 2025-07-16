# This file contain a dag file for airflow , This file create a schema for the postgres database
# And save the extracted enritched_jobs.csv into the postgres db
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime
import pandas as pd

default_args = {
    "start_date": datetime(2025, 7, 16),
    "catchup": False
}

def load_csv_to_postgres():
    df = pd.read_csv('data/enriched_jobs.csv')
    print(f"Loaded {len(df)} rows from CSV")

    # Get connection from Airflow UI
    hook = PostgresHook(postgres_conn_id="postgres_localhost")
    conn = hook.get_conn()
    cur = conn.cursor()

    # Create table if it doesn't exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS job_data (
            title TEXT,
            company TEXT,
            location TEXT,
            experience TEXT,
            skills TEXT,
            tools TEXT
        )
    """)
    conn.commit()
    print("Ensured table exists")

    # Insert data
    for _, row in df.iterrows():
        cur.execute("""
                    INSERT INTO job_data (title, company, location, experience, skills, tools)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """, (
                        row['title'],
                        row['company'],
                        row['location'],
                        row['experience'],
                        row['skills'],
                        row['tools']
                    ))

    conn.commit()
    print("Data inserted into PostgreSQL")

    cur.close()
    conn.close()

with DAG(
    dag_id="load_to_postgres",
    default_args=default_args,
    schedule_interval="@once",
    description="Load enriched job data into Postgres using PostgresHook",
    catchup=False
) as dag:

    load_task = PythonOperator(
        task_id="load_csv_to_postgres",
        python_callable=load_csv_to_postgres
    )
