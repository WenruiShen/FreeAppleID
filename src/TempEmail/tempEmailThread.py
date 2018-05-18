#!/usr/bin/python3
#coding=utf-8

import threading


class guerrillamailThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开启线程： " + self.name)
        print("Start the Main process: applying temp email.")

        guerrillamailListener()

        print("结束线程： " + self.name)
        print("End the Main process.")



# 创建新线程
thread1 = guerrillamailThread(1, "Thread-1", 1)

# 开启新线程
thread1.start()