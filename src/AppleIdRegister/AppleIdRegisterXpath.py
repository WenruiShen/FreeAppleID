#!/usr/bin/python3
#coding=utf-8

##############################################
#
# Author:       Shen Wenrui
# Date:         20180518
# Description:
#
##############################################


class appleIdRegisterXpath():
    def __init__(self):
        self.__appleHomepageUrl = 'https://www.apple.com/cn/'
        # Apple-Id Signin page
        self.__appleIdHomePageUrl = 'https://appleid.apple.com'
        # Apple-Id Signup page
        self.__appleIdSignUpPageUrl = self.appleIdHomePageUrl + '/account'

        self.__signupXpathBase = "/html/body/div[@id='content']/aid-web/div[@class='app-container']/div[@id='app-content']/" \
                            "div[@id='flow']/create-app/aid-create"

    def getAppleIdSignUpPageUrl(self):
        return self.__appleIdSignUpPageUrl

    def __getsignupXpathBase(self):
        return self.__signupXpathBase

    def __signupInputXpathBase(self):
        signupInputXpathBase = self.__getsignupXpathBase + \
                                 "//div[@class='idms-flow-container']//div[@class='idms-step-content']/div/div"
        return signupInputXpathBase

