from redis import Redis
from json import loads
from datetime import datetime

def count_redis_success():
    con = Redis(db=6)
    result = con.get("celery-task-meta*")
    count = 0
    for key in con.scan_iter("celery-task-meta*"):
        is_true = 1 if (loads(con.get(key))['status']).lower() == 'success' else 0
        count += is_true
    print(count)


def get_dates():
    con = Redis(db=6)
    result = con.get("celery-task-meta*")
    dates = []
    for key in con.scan_iter("celery-task-meta*"):
        date = loads(con.get(key))['date_done']
        dates.append(datetime.fromisoformat(date))

    dates.sort()
    print(dates)

count_redis_success()
