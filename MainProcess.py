#!/usr/bin/python3
#coding=utf-8

from src.TempEmail.tempEmailThread import guerrillamailThread
from src.Services.loggingInit import setup_logging

setup_logging()

# 创建新线程
thread1 = guerrillamailThread(1, "Thread-1")

# 开启新线程
thread1.start()

