# -*- coding=utf-8 -*-
# Copyright 2018 QingNiu

"""
:author 马超（ma.chao@qingniu.co）
:date 2018/4/17 

"""
import time
import random
from main_celery import app


def statistics_task(worker_name, *args, **kwargs):
    print('args: ', args)
    print('kwargs: ', kwargs)
    # t = random.randint(1, 10)
    # print('sleep {}sec...'.format(t))
    # time.sleep(1)

    return '{} result'.format(worker_name)


@app.task
def task_worker_1(*args, **kwargs):

    return statistics_task('task_worker_1', *args, **kwargs)


@app.task
def task_worker_2(*args, **kwargs):

    return statistics_task('task_worker_2', *args, **kwargs)