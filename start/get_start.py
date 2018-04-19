# -*- coding=utf-8 -*-
# Copyright 2018

"""
:author Alex Ma
:date 2018/3/27

"""

import time
from celery import Celery

broker = 'redis://127.0.0.1:6379/5'
backend = 'redis://127.0.0.1:6379/6'


app = Celery('tasks', broker=broker, backend=backend)


@app.task
def my_task(name, seconds):
    time.sleep(int(seconds))
    print('{} sleeps for {} sec'.format(name, seconds))

    return name
