#!/usr/bin/python3
#coding=utf-8

from .TempEmail.tempEmailThread import guerrillamailThread


# 创建新线程
thread1 = guerrillamailThread(1, "Thread-1")

# 开启新线程
thread1.start()