from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(dag_id="hello_world", schedule=timedelta(days=30 * 365), start_date=datetime(1970, 1, 1)) as dag:
    (
        BashOperator(task_id="hello", bash_command="echo hello")
        >> BashOperator(task_id="world", bash_command="echo world")
    )
