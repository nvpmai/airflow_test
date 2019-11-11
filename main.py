from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator


args = {
    "start_date": datetime(2019, 11, 01),
    'owner': 'airflow'
}

dag_1 = DAG(
    dag_id='dag_1_second_1',
    schedule_interval=timedelta(seconds=1),
    default_args=args
)


def hello(task_id):
    with open('./result', 'a+') as fd:
        now = str(datetime.now())
        fd.write(f'Task {task_id}: {now}\n')


def gen_task_1_second(dag):
    for id in range(1000):
        task_id = dag.dag_id + "_id_" + str(id)
        task = PythonOperator(
            task_id=task_id,
            python_callable=hello,
            op_kwargs={"task_id": task_id},
            dag=dag
        )


gen_task_1_second(dag_1)
