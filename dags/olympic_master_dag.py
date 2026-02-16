from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine

# --- IMPORTS FROM OUR NEW MODULES ---
from modules.extraction import check_file_exists

# --- CONFIGURATION ---
CSV_PATH = "/opt/airflow/data/athlete_events.csv"
DB_CONNECTION = "postgresql+psycopg2://airflow:airflow@postgres:5432/airflow"

def load_data():
    """Kept inside DAG because it uses specific connection vars"""
    print("Reading CSV...")
    df = pd.read_csv(CSV_PATH)
    engine = create_engine(DB_CONNECTION)
    df.to_sql('raw_athlete_events', engine, if_exists='replace', index=False)

with DAG(
    dag_id='olympic_master_dag_modular', # Changed ID to force a refresh
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    template_searchpath=['/opt/airflow/dags/modules'] # Tell Airflow where to find SQL files
) as dag:

    # 1. Install
    install_task = BashOperator(
        task_id='install_deps',
        bash_command='pip install pandas sqlalchemy psycopg2-binary'
    )

    # 2. Check File (Logic imported from modules/extraction.py)
    check_file_task = PythonOperator(
        task_id='check_file_exists',
        python_callable=check_file_exists,
        op_kwargs={'filepath': CSV_PATH} # Pass the variable into the function
    )

    # 3. Load Data
    load_task = PythonOperator(
        task_id='load_raw_data',
        python_callable=load_data
    )

    # 4. Transform (SQL read from external file)
    transform_task = PostgresOperator(
        task_id='transform_to_silver',
        postgres_conn_id='postgres_default',
        sql='transformation.sql' # Airflow looks in 'modules' because of template_searchpath above
    )

    install_task >> check_file_task >> load_task >> transform_task