# -*- coding=utf-8 -*-
# Copyright 2018 QingNiu

"""
:author 马超（ma.chao@qingniu.co）
:date 2018/3/27 

"""
from celery_rabbit import rabbit_task


def on_message(body):
    print('body -- ', body)


r = rabbit_task.delay('Rookie', 5)
s = rabbit_task.delay('TheShy', 2)
j = rabbit_task.delay('JLK', 3)


print('r ==== ', r.get())
print('s ==== ', s.get())
print('j ==== ', j.get())



