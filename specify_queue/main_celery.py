# -*- coding=utf-8 -*-
# Copyright 2018

"""
:author Alex Ma
:date 2018/4/17 

"""
from celery import Celery


broker = 'amqp://tester:test_password@127.0.0.1:5672'
backend = 'amqp://tester:test_password@127.0.0.1:5672'


app = Celery('ceph', broker=broker, backend=backend,)


app.config_from_object('config')


if __name__ == '__main__':
    app.start()

