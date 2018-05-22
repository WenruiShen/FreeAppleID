#!/usr/bin/python3
#coding=utf-8

##############################################
#
# Author:       Shen Wenrui
# Date:         20180518
# Description:
#
##############################################


import threading

from .AppleIdRegisterProcess import appleIdRegisterProcessor

class appleIdRegisterThread(threading.Thread):
    def __init__(self, threadID, name, userEmail):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.userEmail = userEmail

    def run(self):
        print("开启线程： " + self.name)
        print("Start the AppleID register process.")

        appleIdRegister = appleIdRegisterProcessor()
        appleIdRegister.appleIdRegister(self.userEmail)

        print("结束线程： " + self.name)
        print("End the AppleID register process.")






