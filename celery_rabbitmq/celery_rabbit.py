# -*- coding=utf-8 -*-

"""
:author Alex Ma
:date 2018/2/8 

"""
import time
from celery import Celery
from celery.exceptions import Reject

broker = 'amqp://tester:test_password@127.0.0.1:5672'
backend = 'amqp://tester:test_password@127.0.0.1:5672'


app = Celery('tasks', broker=broker, backend=backend)


# @app.task
# def rabbit_task(name, seconds):
#     raise Exception
#     time.sleep(int(seconds))
#     print('{} sleeps for {} sec'.format(name, seconds))
#     return name


@app.task(acks_late=True)
def rabbit_task(name, seconds):
    try:
        time.sleep(int(seconds))
        print('{} sleeps for {} sec'.format(name, seconds))
        raise Exception
        return name
    except Exception as err:
        print('Reject task back to queue.')
        raise Reject(err, requeue=false)
