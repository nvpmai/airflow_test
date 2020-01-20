from logging import info
from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator


args = {
    'owner': 'airflow'
}


def t1():
    print("DONE TASK 1")


def t2():
    print("DONE TASK 2")


def t3():
    print("DONE TASK 3")


def generate_dag(num):
    for i in range(num):
        dag_id = "dag_" + str(i)

        dag = DAG(
            dag_id=dag_id,
            schedule_interval=timedelta(seconds=10),
            start_date=datetime(2019, 11, 1),
            default_args=args
        )

        PythonOperator(
            task_id="task_" + dag_id,
            python_callable=t1,
            dag=dag
        )

        globals()[dag_id] = dag


generate_dag(5)

# globals()[dag_id] = dag
# Let r