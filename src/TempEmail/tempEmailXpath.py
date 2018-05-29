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

import logging
logger = logging.getLogger("tempEmail")

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

    # Email list.
    def __getEmailContentXpathBase(self):
        emailContent_xpath_base = self.__getEmailBaseXpath() + "/div[@id='tabs-content']/div[@id='inbox']"
        return emailContent_xpath_base

    def getEmailListDisplayXpath(self):
        emailContent_xpath_base = self.__getEmailContentXpathBase()
        EmailListDisplay_xpath = emailContent_xpath_base + "//table[@id='email_table']"
        return EmailListDisplay_xpath

    def getRemainUpdateSecXpath(self):
        emailContent_xpath_base = self.__getEmailContentXpathBase()
        remainUpdateSec_xpath = emailContent_xpath_base + "//table[@id='email_table']//div[@id='tick']"
        return remainUpdateSec_xpath

    # xpath of eamils' list.
    def getEmailContentXpath(self):
        emailContent_xpath_base = self.__getEmailContentXpathBase()
        emailContent_xpath = emailContent_xpath_base + "//table[@id='email_table']/tbody[@id='email_list']/tr"
        return emailContent_xpath

    # Select the latest email.
    def getLatestEmailSelectXpath(self):
        latestEmailSelect_xpath = self.getEmailContentXpath() + "[%d]" % 1
        return  latestEmailSelect_xpath

    def getLatestEmailDateXpath(self):
        latestEmailDate_xpath = self.getEmailContentXpath() + "[%d]/td[@class='td4']" % 1
        return latestEmailDate_xpath

    def getLatestEmailContentXpath(self):
        latestEmailContent_xpath = self.getEmailContentXpath() + "[%d]/td[@class='td3']/span[@class='email-excerpt']" % 1
        return latestEmailContent_xpath

    # Email main text:
    def getLatestEmailMainTextDisplayXpath(self):
        emailContent_xpath_base = self.__getEmailContentXpathBase()
        latestEmailMainTextDisplay_xpath = emailContent_xpath_base + "/div[@id='display_email']"
        return latestEmailMainTextDisplay_xpath

    def __getLatestEmailMainTextXpathBase(self):
        emailContent_xpath_base = self.__getEmailContentXpathBase()
        latestEmailMainText_xpath_base = emailContent_xpath_base + "/div[@id='display_email']/div[@class='email_page']"
        return latestEmailMainText_xpath_base

    def getBackToInboxXpath(self):
        backToInboxXpath = self.__getLatestEmailMainTextXpathBase() + "/div[1]//a[@id='back_to_inbox_link']"
        return backToInboxXpath

    def getLatestEmailMainTextPartXpath(self, index):
        latestEmailMainTextPart_xpath = self.__getLatestEmailMainTextXpathBase() + "/div[@class='email']/div[@class='email_body']" \
                                                                               "/div/div[1]/table/tbody/tr/td[2]/table/tbody" \
                                                                               "/tr[%d]/td" % index
        return latestEmailMainTextPart_xpath

    def getLatestEmailAuthCodeXpath(self):
        latestEmailAuthCode_xpath = self.getLatestEmailMainTextPartXpath(3)
        return latestEmailAuthCode_xpath
