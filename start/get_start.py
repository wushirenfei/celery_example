# -*- coding=utf-8 -*-

"""
:author Alex Ma
:date 2018/2/8 

"""
import time
from celery import Celery

broker = 'redis://127.0.0.1:6379/5'
backend = 'redis://127.0.0.1:6379/6'
P = 1


app = Celery('tasks', broker=broker, backend=backend)


@app.task(default_retry_delay=10)
def my_task(name, seconds):
    1/0
    time.sleep(int(seconds))

    print('{} sleeps for {} sec'.format(name, seconds))
    print(P)

    return name
