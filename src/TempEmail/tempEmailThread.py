#!/usr/bin/python3
#coding=utf-8

import threading

from .tempEmailListener import tempEmailListener

class guerrillamailThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        print("开启线程： " + self.name)
        print("Start the Main process: applying temp email.")

        guerrillamail = tempEmailListener()
        guerrillamail.guerrillamailBrowser()

        print("结束线程： " + self.name)
        print("End the Main process.")
