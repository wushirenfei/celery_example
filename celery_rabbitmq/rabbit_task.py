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

print(r)
print(s)

# print('r ==== ', r.get(on_message=on_message))
print('r ==== ', r.get())
print('s ==== ', s.get())



