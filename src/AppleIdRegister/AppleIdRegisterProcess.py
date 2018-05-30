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

from .AppleIdUserInfo import userInfo
from .AppleIdRegisterOpt import appleIdRegisterOpt
from .AppleIdRegisterAuthImg import appleIdAuthImgOpt
from .AppleIdRegisterAuthEmail import appleIdEmailAuthOpt
from ..db.userModels import userModels

import logging
logger = logging.getLogger("appleIdRegister")

class appleIdRegisterProcessor():
    def __init__(self):
        self.__userInfo = userInfo()
        self.__usermodel = userModels()

    def appleIdRegister(self, userEmail, emailAuthCodeQueue):
        try:
            self.__userInfo.initUserEmail(userEmail)

            # Open the browser.
            appleIdRegisterBrowser = webdriver.Chrome()
            if appleIdRegisterBrowser is None:
                return False
            logger.info("Open appleIdRegisterBrowser.")

            self.__appleIdRegisterBody(appleIdRegisterBrowser, emailAuthCodeQueue)

            # Close the browser.
            appleIdRegisterBrowser.quit()
            logger.info("Close appleIdRegisterBrowser.")
        except Exception as err:
            logger.error(repr(err))


    def __appleIdRegisterBody(self, appleIdRegisterBrowser, emailAuthCodeQueue):
        try:
            self.__appleIdRegisterOperator = appleIdRegisterOpt(appleIdRegisterBrowser)
            self.__appleIdAuthImgOperator = appleIdAuthImgOpt(appleIdRegisterBrowser)
            self.__appleIdEmailAuthOperator = appleIdEmailAuthOpt(appleIdRegisterBrowser)

            # Step-1: Load appleId SignUp page.
            if not self.__appleIdRegisterOperator.loadAppleIdSignUpPage():
                return False

            # Step-2: Input personal Info.
            if not self.__appleIdRegisterOperator.inputAllInfo(self.__userInfo):
                logger.info("Failed input personal info.")
                return False

            for i in range(3):
                # Step-3: Recognize the auth img & auth image's code.
                self.__appleIdAuthImgOperator.appleIdAuthImgProcessor()

                # Step-4: Submit personal info.
                if not self.__appleIdRegisterOperator.submitPersonalInfo():
                    continue

                # Step-5: Block wait for the temp email auth code.
                emailAuthCode = self.__appleIdEmailAuthOperator.emailAuthCodeListener(emailAuthCodeQueue)
                if emailAuthCode is None :
                    continue

                # Step-6: Input & submit temp email auth code.
                if not self.__appleIdEmailAuthOperator.inputEmailAuthCode(emailAuthCode):
                    # Exit Email code input page.
                    # TODO:
                    # if failed to load

                    continue

                # Step-7: Store into database.
                if not self.__usermodel.insertNewUserInfo(self.__userInfo.userEmail, \
                                                           self.__userInfo.userPassword, \
                                                           self.__userInfo.lastName, \
                                                           self.__userInfo.firstName, \
                                                           self.__userInfo.userBirthday):
                    logger.error("Failed store %s into DB." % self.__userInfo.userEmail)
                    return False
                return True
            return False
        except Exception as err:
            logger.error(repr(err))
            return False
