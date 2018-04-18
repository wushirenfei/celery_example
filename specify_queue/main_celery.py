# -*- coding=utf-8 -*-
# Copyright 2018 QingNiu

"""
:author 马超（ma.chao@qingniu.co）
:date 2018/4/17 

"""
from celery import Celery


broker = 'amqp://tester:test_password@47.96.22.213:5672'
backend = 'amqp://tester:test_password@47.96.22.213:5672'

app = Celery('ceph', broker=broker, backend=backend,)


app.config_from_object('config')


if __name__ == '__main__':
    app.start()


# def statistics_task(worker_name, *args, **kwargs):
#     print('args: ', args)
#     print('kwargs: ', kwargs)
#     # t = random.randint(1, 10)
#     # print('sleep {}sec...'.format(t))
#     # time.sleep(1)
#
#     return '{} result'.format(worker_name)
#
#
# @app.task
# def task_worker_1(*args, **kwargs):
#
#     return statistics_task('task_worker_1', *args, **kwargs)
#
#
# @app.task
# def task_worker_2(*args, **kwargs):
#
#     return statistics_task('task_worker_2', *args, **kwargs)
