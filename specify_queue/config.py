# -*- coding=utf-8 -*-
# Copyright 2018

"""
:author Alex Ma
:date 2018/4/17 

"""
CELERY_ROUTES = {
    'task_celery.task_worker_1': {'queue': 'task_worker_1'},
    'task_celery.task_worker_2': {'queue': 'task_worker_2'},
}


CELERY_IMPORTS = (
    'task_celery',
)
