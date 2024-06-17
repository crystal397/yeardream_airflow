import datetime

from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator

@dag(dag_id='dags_bash_operator_decorators',
     start_date=datetime.datetime(2024, 5, 1), 
     schedule="0 13 * * 5#2", 
     tags=["homework"])
def generate_dag():
    EmptyOperator(task_id="dags_bash_operator_standard")

generate_dag()