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

class tempEmailXpath():
    def __init__(self):
        self.guerrillamailUrl = 'https://www.guerrillamail.com/inbox'
        self.__email_xpath_base = "/html/body/div[@id='guerrilla_mail']/div[@class='main-panel']"

    def getGuerrillamailUrl(self):
        return self.guerrillamailUrl

    def __getEmailBaseXpath(self):
        return self.__email_xpath_base

    # Email address.
    def getTempEmailDominSelectXpath(self):
        emailAddr_xpath_base = self.__getEmailBaseXpath() + "/div[@class='show_address']/div[@class='col2']"
        emailDomain_xpath_select = emailAddr_xpath_base + "//select[@id='gm-host-select']"
        return emailDomain_xpath_select

    def getTempEmailAddrXpath(self):
        emailAddr_xpath_base = self.__getEmailBaseXpath() + "/div[@class='show_address']/div[@class='col2']"
        emailAddr_xpath = emailAddr_xpath_base + "/span[@id='email-widget']"
        return emailAddr_xpath

    # Email content.
    def __getEmailContentXpathBase(self):
        emailContent_xpath_base = self.__getEmailBaseXpath() + "/div[@id='tabs-content']/div[@id='inbox']"
        return emailContent_xpath_base

    def getEmailContentXpath(self):
        emailContent_xpath_base = self.__getEmailContentXpathBase()
        emailContent_xpath = emailContent_xpath_base + "//table[@id='email_table']/tbody[@id='email_list']/tr"
        return emailContent_xpath

    def getLatestEmailDateXpath(self):
        latestEmailDate_xpath = self.getEmailContentXpath() + "[%d]/td[@class='td4']" % 1
        return latestEmailDate_xpath

    def getRemainUpdateSecXpath(self):
        emailContent_xpath_base = self.__getEmailContentXpathBase()
        remainUpdateSec_xpath = emailContent_xpath_base + "//table[@id='email_table']//div[@id='tick']"
        return remainUpdateSec_xpath

    def getLatestEmailContentXpath(self):
        latestEmailContent_xpath = self.getEmailContentXpath() + "[%d]/td[@class='td3']/span[@class='email-excerpt']" % 1
        return latestEmailContent_xpath


#tempEmail = tempEmailXpath()
#print(tempEmail.getTempEmailAddrXpath())