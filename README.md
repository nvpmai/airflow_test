1. Setup and run Airflow

```
export AIRFLOW_HOME=~/airflow
pip install apache-airflow
airflow initdb
```

Please check https://airflow.apache.org/start.html for details

2. In ~/airflow/airflow.cfg, change:

- **dags_folder** to the folder that contains main.py
- **catchup_by_default** to **False** ([Details](https://airflow.apache.org/scheduler.html?highlight=catchup_by_default#backfill-and-catchup))
- **load_examples** to **False**
- **dags_are_paused_at_creation** to **False** so as not to pause the task on creation


3. Run scheduler:

```
airflow webserver -p 8080
airflow scheduler
```

4. Check logs in ~/airflow/logs