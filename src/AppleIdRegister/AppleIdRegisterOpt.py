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

from .AppleIdRegisterXpath import appleIdRegisterXpath
from .AppleIdUserInfo import userInfo

class appleIdRegisterOpt():
    def __init__(self, appleIdRegisterBrowser):
        self.__xpath = appleIdRegisterXpath()
        self.__appleIdRegisterBrowser = appleIdRegisterBrowser
        self.__userInfo = userInfo()

    def loadAppleIdSignUpPage(self):
        appleIdSignUpPageUrl = self.__xpath.getAppleIdSignUpPageUrl()
        print("Open: " + appleIdSignUpPageUrl)
        self.__appleIdRegisterBrowser.get(appleIdSignUpPageUrl)

        try:
            # Explicitly wait.
            WebDriverWait(self.__appleIdRegisterBrowser, 20, 0.5).until(
                EC.presence_of_element_located((By.XPATH, self.__xpath.getPersonalInfoXpathLastName()))
            )
        except Exception as err:
            print("Failed to load: " + appleIdSignUpPageUrl, + ", err: " + repr(err))
            return False

        print("Success to load: " + appleIdSignUpPageUrl)
        return True


    # Input personal information for signing up.
    def __lastNameInput(self, lastName):
        lastNameXpath = self.__xpath.getPersonalInfoXpathLastName()
        lastNameElement = self.__appleIdRegisterBrowser.find_element_by_xpath(lastNameXpath)
        lastNameElement.clear()
        lastNameElement.send_keys(lastName)

    def __firstNameInput(self, firstName):
        firstNameXpath = self.__xpath.getPersonalInfoXpathFirstName()
        firstNameElement = self.__appleIdRegisterBrowser.find_element_by_xpath(firstNameXpath)
        firstNameElement.clear()
        firstNameElement.send_keys(firstName)

    def __nationSelect(self, nation):
        nationalityXpath = self.__xpath.getPersonalInfoXpathNation()
        nationalitySelector = Select(self.__appleIdRegisterBrowser.find_element_by_xpath(nationalityXpath))
        nationalitySelector.select_by_value(nation)

    def __birthdayInput(self, birthday):
        birthdayXpath = self.__xpath.getPersonalInfoXpathBirthday()
        birthdayElement = self.__appleIdRegisterBrowser.find_element_by_xpath(birthdayXpath)
        birthdayElement.clear()
        birthdayElement.send_keys(birthday)

    def personalInfoInput(self):
        # Step-1: Load personal info:
        lastName =  self.__userInfo.lastName
        firstName = self.__userInfo.firstName
        nation =    self.__userInfo.nation
        birthday =  self.__userInfo.userBirthday
        # Step-2: Last_name:
        self.__lastNameInput(lastName)
        # Step-3: First_name:
        self.__firstNameInput(firstName)
        # Step-4: Nationality:
        self.__nationSelect(nation)
        # Step-5: BirthDay:
        self.__birthdayInput(birthday)

    # Input password.
    def __appleIdEmailInput(self, user_email):
        appleIdEmailXpath = self.__xpath.getAppleIdEmailXpath()
        appleIdEmailElement = self.__appleIdRegisterBrowser.find_element_by_xpath(appleIdEmailXpath)
        appleIdEmailElement.clear()
        appleIdEmailElement.send_keys(user_email)

    def __passwordFirstInput(self, user_password):
        passwordFirstInputXpath = self.__xpath.getPasswordFirstInputXpath()
        passwordFirstInputElement = self.__appleIdRegisterBrowser.find_element_by_xpath(passwordFirstInputXpath)
        passwordFirstInputElement.clear()
        passwordFirstInputElement.send_keys(user_password)

    def __passwordConfirm(self, user_password):
        confirmPasswordXpath = self.__xpath.getPasswordConfirmXpath()
        confirmPasswordElement = self.__appleIdRegisterBrowser.find_element_by_xpath(confirmPasswordXpath)
        confirmPasswordElement.clear()
        confirmPasswordElement.send_keys(user_password)

    def appleIdPasswordInput(self):
        user_email =    self.__userInfo.userEmail
        user_password = self.__userInfo.userPassword
        # Step-1: Apple-id (E-mail)
        self.__appleIdEmailInput(user_email)
        # Step-2: Password:
        self.__passwordFirstInput(user_password)
        # Step-3: Password confirm:
        self.__passwordConfirm(user_password)


    # Input safe questions.
    def __selectOneSafeQuestion(self, questionIndex, safeQuestionValue, answer):
        # Step-1: select one safe question.
        oneSafeQuestionXpath, oneSafeQuestionXpathAnswer = self.__xpath.getOneSafeQuestionXpath(questionIndex)
        safeQuestionSelector = Select(self.__appleIdRegisterBrowser.find_element_by_xpath(oneSafeQuestionXpath))
        safeQuestionSelector.select_by_value(safeQuestionValue)

        # Step-2: Answer this safe question.
        answerElement = self.__appleIdRegisterBrowser.find_element_by_xpath(oneSafeQuestionXpathAnswer)
        answerElement.clear()
        answerElement.send_keys(answer)

    def safeQuestionInput(self):
        # Safe question - 1:
        safeQuestionValue_1 = "130"  # 你少年时代最好的朋友叫什么名字？
        answer_1 = "Bob"
        self.__selectOneSafeQuestion(1, safeQuestionValue_1, answer_1)

        # Safe question - 2:
        safeQuestionValue_2 = "136" # 你的理想工作是什么？
        answer_2 = "Teacher"
        self.__selectOneSafeQuestion(2, safeQuestionValue_2, answer_2)

        # Safe question - 3:
        safeQuestionValue_3 = "145" # 你去过的第一个海滨浴场是哪一个？
        answer_3 = "Long Beach"
        self.__selectOneSafeQuestion(3, safeQuestionValue_3, answer_3)

    def inputAllInfo(self):
        try:
            self.personalInfoInput()
            self.appleIdPasswordInput()
            self.safeQuestionInput()
            return True
        except Exception as err:
            print("[ERROR] InputAllInfo Failed: " + repr(err))
            return False


    # Submit personal information.
    def submitPersonalInfo(self):
        try:
            submitXpath = self.__xpath.getSubmitXpath()
            self.__appleIdRegisterBrowser.find_element_by_xpath(submitXpath).click()
            return True
        except Exception as err:
            print("[ERROR] SubmitPersonalInfo Failed: " + repr(err))
            return False



