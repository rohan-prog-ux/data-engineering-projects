from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def extract_data():
    print("Extracting data...")

with DAG('daily_ingestion', start_date=datetime(2024, 1, 1), schedule_interval='@daily') as dag:
    task = PythonOperator(task_id='extract', python_callable=extract_data)
