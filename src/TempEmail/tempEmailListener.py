#!/usr/bin/python3
#coding=utf-8

##############################################
#
# Author:       Shen Wenrui
# Date:         20180506
# Description:
#
##############################################

import sys
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import threading
import time
import re





def waitAuthCode(tempEmailBrowser, email_xpath_base):
    emailContent_xpath_base = email_xpath_base + "/div[@id='tabs-content']/div[@id='inbox']"
    emailContent_xpath = emailContent_xpath_base + "//table[@id='email_table']/tbody[@id='email_list']/tr"

    oriEmailListLength = getEmailListLength(tempEmailBrowser, emailContent_xpath)
    print(oriEmailListLength)

    # waitting for freshing the inbox.
    for i in range(2):
        remainUpdateSec = getNextUpdateSec(tempEmailBrowser, emailContent_xpath_base)
        print("Next update in: " + str(remainUpdateSec) + " sec")

        print("Start : %s" % time.ctime())
        time.sleep(remainUpdateSec + 3)
        print("End : %s" % time.ctime())

        emailListLength = getEmailListLength(tempEmailBrowser, emailContent_xpath)
        print(emailListLength)

        if(emailListLength > oriEmailListLength):
            authCode = getLatestEmailAuthCode(tempEmailBrowser, emailContent_xpath)
            print("authCode: " + authCode)
            oriEmailListLength = emailListLength
            return authCode

        latestEmailDate = getLatestEmailDat(tempEmailBrowser, emailContent_xpath)
        print(latestEmailDate)

    return None








def guerrillamailListener():
    try:
        # Step-1: Open the browser.
        tempEmailBrowser = webdriver.Chrome()
        if tempEmailBrowser is None:
            return False
        print("Open the browser")

        # Step-2: Open the netpage of guerrillamail.
        if not loadTempEamilPage(tempEmailBrowser):
            return False
        print("Successfully load: " + guerrillamailUrl)

        # Step-3: Get temp email address.
        email_xpath_base = getEmailBaseXpath()
        tempEmailAddr = getTempEmailAddr(tempEmailBrowser, email_xpath_base)
        if tempEmailAddr is None:
            return False

        # Step-4: Init the inbox.
        emailContent_xpath = xxx
        oriEmailElementList, latestEmailDate = getInboxInfo(tempEmailBrowser, emailContent_xpath)

        # Step-5: Start the thread of applying appleId.

        while False:
            # Step-6: Whether register appleId success.

            # Step-7: Whether thread-2 is stopped.

            # Step-8: Blockly listen to the inbox.
            authCode = waitAuthCode(tempEmailBrowser, email_xpath_base)
            if authCode is None:
                print("Failed")

        return True

    except Exception as err:
        print("[ERROR]:" + str(err))

    finally:
        # Close the browser.
        # tempEmailBrowser.quit()
        print("Close the browser.")







