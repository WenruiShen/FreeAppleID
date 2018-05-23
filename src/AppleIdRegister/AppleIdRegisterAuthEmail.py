#!/usr/bin/python3
#coding=utf-8

##############################################
#
# Author:       Shen Wenrui
# Date:         20180518
# Description:
#
##############################################


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .AppleIdRegisterXpath import appleIdRegisterXpath

class appleIdEmailAuthOpt():
    def __init__(self, appleIdRegisterBrowser):
        self.__xpath = appleIdRegisterXpath()
        self.__appleIdRegisterBrowser = appleIdRegisterBrowser

    def __submitEmailAuthCode(self):
        return True

    def __inputOneNumber(self, index, num):
        try:
            emailAuthCodeXpathInput = self.__xpath.getEmailAuthCodeXpathInput(index)
            authCodeInputElement = self.__appleIdRegisterBrowser.find_element_by_xpath(emailAuthCodeXpathInput)
            authCodeInputElement.clear()
            authCodeInputElement.send_keys(num)
        except Exception as err:
            print("[ERROR] __inputOneNumber Failed: " + repr(err))
            return None

    def __inputCode(self, emailAuthCode):
        index = 0
        for num in list(emailAuthCode):
            index = index + 1
            self.__inputOneNumber(index, num)

    def __submitAuthCode(self):
        try:
            submitEmailAuthCodeXpathButtonOk = self.__xpath.getSubmitEmailAuthCodeXpathButtonOk()
            self.__appleIdRegisterBrowser.find_element_by_xpath(submitEmailAuthCodeXpathButtonOk).click()

            # Explicitly wait.
            WebDriverWait(self.__appleIdRegisterBrowser, 10, 0.5).until(
                EC.presence_of_element_located((By.XPATH, self.__xpath.getTempEmailAddrXpath()))
            )
            return True
        except Exception as err:
            print("[ERROR] __submitAuthCode Failed: " + repr(err))
            return False

    def inputEmailAuthCode(self, emailAuthCode = "123456"):
        try:
            self.__inputCode(emailAuthCode)
            return self.__submitAuthCode()
        except Exception as err:
            print("[ERROR] InputEmailAuthCode Failed: " + repr(err))
            return False

    def emailAuthCodeListener(self, emailAuthCodeQueue):
        try:
            # 阻塞等待2min
            emailAuthCode = emailAuthCodeQueue.get(timeout=120.0)
            print("Queue receive emailAuthCode: " + emailAuthCode)
            # 正则校验
            # TODO：

            return emailAuthCode
        except Exception as err:
            print("[ERROR] emailAuthCodeListener Failed: " + repr(err))
            return None