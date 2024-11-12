from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from scripts.extract import extract_movie_data
from scripts.transform import transform_movie_data
from scripts.load import load_movie_data

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    'movie_etl_pipeline',
    default_args=default_args,
    description='An ETL pipeline for TMDB movie data',
    schedule_interval='@daily',
    catchup=False
) as dag:

    def extract_task():
        return extract_movie_data()

    def transform_task(ti):
        raw_data = ti.xcom_pull(task_ids='extract_task')
        transformed_data = transform_movie_data(raw_data)
        return transformed_data

    def load_task(ti):
        transformed_data = ti.xcom_pull(task_ids='transform_task')
        load_movie_data(transformed_data)

    extract = PythonOperator(
        task_id='extract_task',
        python_callable=extract_task
    )

    transform = PythonOperator(
        task_id='transform_task',
        python_callable=transform_task
    )

    load = PythonOperator(
        task_id='load_task',
        python_callable=load_task
    )

    extract >> transform >> load
