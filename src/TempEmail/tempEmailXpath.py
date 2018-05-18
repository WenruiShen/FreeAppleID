#!/usr/bin/python3
#coding=utf-8

class tempEmailXpath:
    def __init__(self):
        self.guerrillamailUrl = 'https://www.guerrillamail.com/inbox'
        self.email_xpath_base = "/html/body/div[@id='guerrilla_mail']/div[@class='main-panel']"

    def getGuerrillamailUrl(self):
        return self.guerrillamailUrl

    def getEmailBaseXpath(self):
        return self.email_xpath_base


    def getTempEmailDominSelectXpath(self):
        emailAddr_xpath_base = self.email_xpath_base + "/div[@class='show_address']/div[@class='col2']"
        emailDomain_xpath_select = emailAddr_xpath_base + "//select[@id='gm-host-select']"
        return emailDomain_xpath_select


    def getTempEmailAddrXpath(self):
        emailAddr_xpath_base = self.email_xpath_base + "/div[@class='show_address']/div[@class='col2']"
        emailAddr_xpath = emailAddr_xpath_base + "/span[@id='email-widget']"
        return emailAddr_xpath


    def getEmailContentXpath(self):
        emailContent_xpath_base = self.email_xpath_base + "/div[@id='tabs-content']/div[@id='inbox']"
        emailContent_xpath = emailContent_xpath_base + "//table[@id='email_table']/tbody[@id='email_list']/tr"
        return emailContent_xpath


tempEmail = tempEmailXpath()
print(tempEmail.getTempEmailAddrXpath())