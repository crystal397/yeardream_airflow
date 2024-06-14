import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

my_dag = DAG(
    dag_id="dags_bash_operator_standard",
    schedule="0 9 * * 1,5",
    start_date=datetime.datetime(2024, 6, 1),
    tags=["homework"]
)