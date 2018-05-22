#!/usr/bin/python3
#coding=utf-8

##############################################
#
# Author:       Shen Wenrui
# Date:         20180518
# Description:
#
##############################################



from selenium import webdriver
import time

from .tempEmailParser import tempEmailParser
from ..AppleIdRegister.AppleIdRegisterThread import appleIdRegisterThread

class tempEmailListener:
    def guerrillamailBrowser(self):
        try:
            # Open the browser.
            tempEmailBrowser = webdriver.Chrome()
            if tempEmailBrowser is None:
                return False
            print("Open the browser.")

            self.__guerrillamailListener(tempEmailBrowser)

            # Close the browser.
            tempEmailBrowser.quit()
            print("Close the browser.")

        except Exception as err:
            print("[ERROR]:" + repr(err))


    def __guerrillamailListener(self, tempEmailBrowser):
        try:

            self.__tempEmailParser = tempEmailParser(tempEmailBrowser)

            # Step-1: Open the netpage of guerrillamail.
            if not self.__tempEmailParser.loadTempEamilPage():
                return False

            # Step-2: Get temp email address.
            tempEmailAddr = self.__tempEmailParser.getTempEmailAddr()
            if tempEmailAddr is None:
                return False
            print("The temp Email addr: " + tempEmailAddr)

            # Step-3: Init the inbox.
            self.__emailElementListLen, self.__latestEmailDate = self.__tempEmailParser.getInboxInfo()
            print("Current Inbox Emails list's length: {}, last date: {}.".format(self.__emailElementListLen, self.__latestEmailDate))

            # Step-4: Start the thread of applying appleId.
            print("Now start the thread of Applying Apple ID!")
            # 创建新线程
            thread2 = appleIdRegisterThread(2, "Thread-2", tempEmailAddr)
            # 开启新线程
            thread2.start()

            while True:
                # Step-5: Whether register appleId success.

                # Step-6: Whether thread-2 is stopped.
                if not thread2.isAlive():
                    return False

                # Step-7: Blockly listen to the inbox.
                authCode = self.__waitAuthCode()
                if authCode is None:
                    print("Failed")

            return True
        except Exception as err:
            print("[ERROR]:" + repr(err))
            return False


    def __waitAuthCode(self):
        try:
            remainUpdateSec = self.__tempEmailParser.getNextUpdateSec()
            print("Next update in: {} sec.".format(remainUpdateSec))

            print("Start : {}".format(time.ctime()))
            time.sleep(remainUpdateSec + 3)
            print("End : {}".format(time.ctime()))

            emailElementListLen, latestEmailDate = self.__tempEmailParser.getInboxInfo()
            print("Current Inbox Emails list's length: {}, last date: {}.".format(self.__emailElementListLen,
                                                                                  self.__latestEmailDate))

            if(emailElementListLen > self.__emailElementListLen):
                authCode = self.__tempEmailParser.getLatestEmailAuthCode()
                print("authCode: " + authCode)
                self.__emailElementListLen = emailElementListLen
                self.__latestEmailDate = latestEmailDate
                return authCode
            return None
        except Exception as err:
            print("[ERROR]:" + repr(err))
            return None
















