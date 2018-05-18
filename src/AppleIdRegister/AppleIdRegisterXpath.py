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
        signupInputXpathBase = self.__getsignupXpathBase() + \
                                 "//div[@class='idms-flow-container']//div[@class='idms-step-content']/div/div"
        return signupInputXpathBase


    # Personal Info.
    def __getPersonalInfoXpath(self):
        personalInfoXpath = self.__signupInputXpathBase() + "/div[2]/div"
        return personalInfoXpath

    def getPersonalInfoXpathLastName(self):
        lastNameXpath = self.__getPersonalInfoXpath() + "/div[1]//last-name-input//input"
        return lastNameXpath

    def getPersonalInfoXpathFirstName(self):
        firstNameXpath = self.__getPersonalInfoXpath() + "/div[1]//first-name-input//input"
        return firstNameXpath

    def getPersonalInfoXpathNation(self):
        nationalityXpath = self.__getPersonalInfoXpath() + "/div[2]//select"
        return nationalityXpath

    def getPersonalInfoXpathBirthday(self):
        birthdayXpath = self.__getPersonalInfoXpath() + "/div[3]//input"
        return birthdayXpath


    # Password.
    def __getPasswordInputXpath(self):
        passwordInputXpath = self.__signupInputXpathBase() + "/div[3]/div"
        return passwordInputXpath


