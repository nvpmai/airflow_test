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
    print("DONE TASK 1")


for num in range(5):
    dag_id = "dag_" + str(num)

    dag = DAG(
        dag_id=dag_id,
        schedule_interval=timedelta(seconds=5),
        start_date=datetime(2019, 11, 1),
        default_args=args
    )

    PythonOperator(
        task_id="task_" + dag_id,
        python_callable=t1,
        dag=dag
    )

    globals()[dag_id] = dag

# dag = DAG(
#     dag_id="dag_1",
#     schedule_interval=timedelta(seconds=1),
#     start_date=datetime(2019, 11, 1),
#     default_args=args
# )

# PythonOperator(
#     task_id="task_1",
#     python_callable=t1,
#     dag=dag
# )

# dag_2 = DAG(
#     dag_id="dag_2",
#     schedule_interval=timedelta(seconds=1),
#     start_date=datetime(2019, 11, 1),
#     default_args=args
# )

# PythonOperator(
#     task_id="task_2",
#     python_callable=t2,
#     dag=dag_2
# )
