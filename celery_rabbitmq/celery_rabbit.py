# -*- coding=utf-8 -*-

"""
:author Alex Ma
:date 2018/2/8 

"""
import time
from celery import Celery

# broker = 'amqp://tester:test_password@127.0.0.1:5672'
# backend = 'amqp://tester:test_password@127.0.0.1:5672'

broker = 'amqp://tester:test_password@47.96.22.213:5672'
backend = 'amqp://tester:test_password@47.96.22.213:5672'


app = Celery('tasks', broker=broker, backend=backend)


@app.task
def rabbit_task(name, seconds):
    time.sleep(int(seconds))
    print('{} sleeps for {} sec'.format(name, seconds))
    return name


