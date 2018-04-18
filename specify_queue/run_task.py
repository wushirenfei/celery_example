# -*- coding=utf-8 -*-
# Copyright 2018 QingNiu

"""
:author 马超（ma.chao@qingniu.co）
:date 2018/4/17 

"""
from task_celery import task_worker_1, task_worker_2


def statistics_data(target_list):
    worker1_params = target_list[0::2]
    worker2_params = target_list[1::2]

    task1 = task_worker_1.delay(worker1_params, name='task 1 statistics')
    task2 = task_worker_2.delay(worker2_params, name='task 2 statistics')

    result1 = task1.get()
    result2 = task2.get()

    print('result1: ', result1)
    print('result2: ', result2)


if __name__ == '__main__':
    statistics_data([x for x in range(50)])

