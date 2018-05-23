#!/usr/bin/python3
#coding=utf-8

import threading
import logging

from .tempEmailListener import tempEmailListener

logger = logging.getLogger("tempEmail")

class guerrillamailThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        logger.info("开启线程: " + self.name)
        logger.info("Start the Main process: applying temp email.")

        guerrillamail = tempEmailListener()
        guerrillamail.guerrillamailBrowser()

        logger.info("结束线程： " + self.name)
        logger.info("End the Main process.")
