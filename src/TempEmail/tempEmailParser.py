#!/usr/bin/python3
#coding=utf-8

##############################################
#
# Author:       Shen Wenrui
# Date:         20180518
# Description:
#
##############################################

import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import re

from .tempEmailXpath import tempEmailXpath

import logging
logger = logging.getLogger("tempEmail")

class tempEmailParser():
    def __init__(self, tempEmailBrowser):
        self.__xpath = tempEmailXpath()
        self.__tempEmailBrowser = tempEmailBrowser

    # parse email address.
    def getTempEmailAddr(self):
        try:
            # Step 1: Select the Domain:
            emailDomain_xpath_select = self.__xpath.getTempEmailDominSelectXpath()
            emailDomain_select = Select(self.__tempEmailBrowser.find_element_by_xpath(emailDomain_xpath_select))
            # "guerrillamail.com", "sharklasers.com"
            emailDomain_value = "sharklasers.com"
            emailDomain_select.select_by_value(emailDomain_value)

            # Step 2: Get the Email address:
            emailAddr_xpath = self.__xpath.getTempEmailAddrXpath()
            tempEmailAddr = self.__tempEmailBrowser.find_element_by_xpath(emailAddr_xpath).text
            if not re.match(r'.+?@.+?\.com', tempEmailAddr):
                logger.info("Illegal tempEmailAddr: " + tempEmailAddr)
                tempEmailAddr = None
        except Exception as err:
            logger.error(repr(err))
            tempEmailAddr = None
        return tempEmailAddr

    # Email Inbox.
    def getEmailListLength(self):
        try:
            # Email list:
            emailContent_xpath = self.__xpath.getEmailContentXpath()
            emailElementList = self.__tempEmailBrowser.find_elements_by_xpath(emailContent_xpath)
            return len(emailElementList)
        except Exception as err:
            logger.error(repr(err))
            return 0

    def getLatestEmailDat(self):
        try:
            # Get the latest Email's date:
            latestEmailDate_xpath = self.__xpath.getLatestEmailDateXpath()
            latestEmailDate = self.__tempEmailBrowser.find_element_by_xpath(latestEmailDate_xpath).text
            return latestEmailDate
        except Exception as err:
            logger.error(repr(err))
            return None

    def getInboxInfo(self):
        emailElementListLen = self.getEmailListLength()
        latestEmailDate = self.getLatestEmailDat()
        return emailElementListLen, latestEmailDate

    def getNextUpdateSec(self):
        try:
            # Get next update sec:
            remainUpdateSec_xpath = self.__xpath.getRemainUpdateSecXpath()
            remainUpdateSec = re.findall(r"Next update in: (.+?) sec",
                                         self.__tempEmailBrowser.find_element_by_xpath(remainUpdateSec_xpath).text)
            remainUpdateSec = remainUpdateSec[0] if len(remainUpdateSec)!=0 else '0'
            return int(remainUpdateSec)
        except Exception as err:
            logger.error(repr(err))
            return None

    def getLatestEmailAuthCode(self):
        try:
            # Select the latest Email's context:
            latestEmailSelect_xpath = self.__xpath.getLatestEmailSelectXpath()
            self.__tempEmailBrowser.find_element_by_xpath(latestEmailSelect_xpath).click()
            # Explicitly wait.
            WebDriverWait(self.__tempEmailBrowser, 5, 0.1).until(
                EC.presence_of_element_located((By.XPATH, self.__xpath.getLatestEmailAuthCodeXpath()))
            )
            # Parse out the Auth Code:
            authCode = self.__tempEmailBrowser.find_element_by_xpath(self.__xpath.getLatestEmailAuthCodeXpath()).text
            if not re.match(r'\w{3,6}', authCode):
                authCode = None
            return authCode
        except Exception as err:
            logger.error(repr(err))
            return None

    # Load the email page and wait explicitly.
    def loadTempEamilPage(self):
        guerrillamailUrl = self.__xpath.getGuerrillamailUrl()
        logger.info("Open:" + guerrillamailUrl)
        self.__tempEmailBrowser.get(guerrillamailUrl)

        try:
            # Explicitly wait.
            WebDriverWait(self.__tempEmailBrowser, 20, 0.5).until(
                EC.presence_of_element_located((By.XPATH, self.__xpath.getTempEmailAddrXpath()))
            )
        except Exception as err:
            logger.error("Failed to load: " + guerrillamailUrl, + ", err: " + repr(err))
            return False

        logger.info("Success to load: " + guerrillamailUrl)
        return True