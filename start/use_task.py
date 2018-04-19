# -*- coding=utf-8 -*-
# Copyright 2018

"""
:author Alex Ma
:date 2018/3/27

"""
from get_start import my_task


def on_message(body):
    print('body -- ', body)


r = my_task.delay('Rookie', 5)
s = my_task.delay('TheShy', 4)
j = my_task.delay('JLK', 3)

print('r --- ', r.get(on_message=on_message))
print('s --- ', s.get(on_message=on_message))
print('j --- ', j.get(on_message=on_message))
