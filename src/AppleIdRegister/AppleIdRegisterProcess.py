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

from .AppleIdRegisterOpt import appleIdRegisterOpt
from .AppleIdRegisterAuthImg import appleIdAuthImgOpt


class appleIdRegisterProcessor:
    def appleIdRegister(self):
        try:
            # Open the browser.
            appleIdRegisterBrowser = webdriver.Chrome()
            if appleIdRegisterBrowser is None:
                return False
            print("Open appleIdRegisterBrowser.")

            self.__appleIdRegisterBody(appleIdRegisterBrowser)

            # Close the browser.
            appleIdRegisterBrowser.quit()
            print("Close appleIdRegisterBrowser.")
        except Exception as err:
            print("[ERROR]:" + repr(err))


    def __appleIdRegisterBody(self, appleIdRegisterBrowser):
        try:

            self.__appleIdRegisterOperator = appleIdRegisterOpt(appleIdRegisterBrowser)
            self.__appleIdAuthImgOperator = appleIdAuthImgOpt(appleIdRegisterBrowser)

            # Step-1: Load appleId SignUp page.
            if not self.__appleIdRegisterOperator.loadAppleIdSignUpPage():
                return False

            # Step-2: Input personal Info.
            if not self.__appleIdRegisterOperator.inputAllInfo():
                print("Failed input personal info.")
                return False

            for i in range(3):
                # Step-3: Recognize the auth img & auth image's code.
                if not self.__appleIdAuthImgOperator.appleIdAuthImgProcessor():
                    continue

                # Step-4: Submit personal info.
                if not self.__appleIdRegisterOperator.submitPersonalInfo():
                    continue

                # Step-5: Block wait for the temp email auth code.
                if False:
                    continue

                # Step-6: Input & submit temp email auth code.
                if False:
                    continue
                return True

            # Step-7: Store into database.
            # TODO:

            return False
        except Exception as err:
            print("[ERROR]:" + repr(err))
            return False


















# Input auth code sent to the email.
browser.implicitly_wait(3)
userInputEmailAuthCode(browser, userInputAuthCode = "966412")



# - 2nd - Page:

accountManageUrl = "https://appleid.apple.com/account/manage"
print(accountManageUrl)

browser.implicitly_wait(5)
browser.get(accountManageUrl)




