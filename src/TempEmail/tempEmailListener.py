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
import queue

from .tempEmailParser import tempEmailParser
from ..AppleIdRegister.AppleIdRegisterThread import appleIdRegisterThread

import logging
logger = logging.getLogger("tempEmail")

class tempEmailListener:
    def guerrillamailBrowser(self):
        try:
            # Open the browser.
            tempEmailBrowser = webdriver.Chrome()
            if tempEmailBrowser is None:
                return False
            logger.info("Open the browser.")

            self.__guerrillamailListener(tempEmailBrowser)

            # Close the browser.
            tempEmailBrowser.quit()
            logger.info("Close the browser.")

        except Exception as err:
            logger.error(repr(err))


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
            logger.info("The temp Email addr: " + tempEmailAddr)

            # Step-3: Init the inbox.
            self.__emailElementListLen, self.__latestEmailDate = self.__tempEmailParser.getInboxInfo()
            logger.debug("Current Inbox Emails list's length: {}, last date: {}.".format(self.__emailElementListLen, self.__latestEmailDate))

            emailAuthCodeQueue = queue.Queue()

            # Step-4: Start the thread of applying appleId.
            logger.info("Now start the thread of Applying Apple ID!")
            # 创建新线程
            thread2 = appleIdRegisterThread(2, "Thread-2", tempEmailAddr, emailAuthCodeQueue)
            # 开启新线程
            thread2.start()

            while True:
                # Step-5: Whether register appleId success.
                # TODO:

                # Step-6: Whether thread-2 is stopped.
                if not thread2.isAlive():
                    break

                # Step-7: Blockly listen to the inbox.
                authCode = self.__waitAuthCode()
                if authCode is None:
                    logger.debug("Failed get authCode")
                    continue
                else:
                    logger.info("Queue send authCode: " + authCode)
                    emailAuthCodeQueue.put(authCode)

            thread2.join()
            return True
        except Exception as err:
            logger.error(repr(err))
            return False


    def __waitAuthCode(self):
        try:

            remainUpdateSec = self.__tempEmailParser.getNextUpdateSec()
            logger.debug("Next update in: {} sec.".format(remainUpdateSec))

            logger.debug("Start : {}".format(time.ctime()))
            time.sleep(remainUpdateSec + 3)
            logger.debug("End : {}".format(time.ctime()))

            emailElementListLen, latestEmailDate = self.__tempEmailParser.getInboxInfo()
            logger.debug("Current Inbox Emails list's length: {}, last date: {}.".format(self.__emailElementListLen,
                                                                                  self.__latestEmailDate))

            if(emailElementListLen > self.__emailElementListLen):
                authCode = self.__tempEmailParser.getLatestEmailAuthCode()
                logger.info("Receive authCode: " + authCode)
                self.__emailElementListLen = emailElementListLen
                self.__latestEmailDate = latestEmailDate
                return authCode
            return None
        except Exception as err:
            logger.error(repr(err))
            return None
















