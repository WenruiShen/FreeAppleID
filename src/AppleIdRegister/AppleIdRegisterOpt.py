#!/usr/bin/python3
#coding=utf-8

##############################################
#
# Author:       Shen Wenrui
# Date:         20180518
# Description:
#
##############################################

from selenium.webdriver.support.ui import Select

from .AppleIdRegisterXpath import appleIdRegisterXpath
from .AppleIdUserInfo import userInfo

class appleIdRegisterOpt():
    def __init__(self, appleIdRegisterBrowser):
        self.__xpath = appleIdRegisterXpath()
        self.__appleIdRegisterBrowser = appleIdRegisterBrowser
        self.__userInfo = userInfo()


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

    def personalInfoInput(self, lastName, firstName, nation, birthday):
        # Step-1: Load personal info:

        # Step-2: Last_name:
        self.__lastNameInput(lastName)
        # Step-3: First_name:
        self.__firstNameInput(firstName)
        # Step-4: Nationality:
        nation = "USA"  # 美国
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

    def appleIdPasswordInput(self, user_email, user_password):
        # Step-1: Apple-id (E-mail)
        self.__appleIdEmailInput(user_email)

        # Step-2: Password:
        self.__passwordFirstInput(user_password)

        # Step-3: Password confirm:
        self.__passwordConfirm(user_password)


    # Input safe questions.
    signupInput_xpath_safeQuestion = signupInput_xpath_base + "/div[4]/div"
    def safeQuestionInput(self, signupInput_xpath_safeQuestion):
        # Step-4.3.1: Safe question - 1:
        safeQuestion_1_xpath_base = signupInput_xpath_safeQuestion + "//security-questions-answers/div/div[1]"
        safeQuestion_1_xpath = safeQuestion_1_xpath_base + '//select'
        safeQuestion_1_select = Select(self.__appleIdRegisterBrowser.find_element_by_xpath(safeQuestion_1_xpath))
        safeQuestion_1_value = "130" # 你少年时代最好的朋友叫什么名字？
        safeQuestion_1_select.select_by_value(safeQuestion_1_value)

        # Step-4.3.2: Safe question - 1 (Answer):
        answer_1 = "Bob"
        safeQuestion_1_xpath_answer = safeQuestion_1_xpath_base + "//input[@type='text']"
        answer_1_Element = self.__appleIdRegisterBrowser.find_element_by_xpath(safeQuestion_1_xpath_answer)
        answer_1_Element.clear()
        answer_1_Element.send_keys(answer_1)

        # Step-4.3.3: Safe question - 2:
        safeQuestion_2_xpath_base = signupInput_xpath_safeQuestion + "//security-questions-answers/div/div[2]"
        safeQuestion_2_xpath = safeQuestion_2_xpath_base + '//select'
        safeQuestion_2_select = Select(self.__appleIdRegisterBrowser.find_element_by_xpath(safeQuestion_2_xpath))
        safeQuestion_2_value = "136" # 你的理想工作是什么？
        safeQuestion_2_select.select_by_value(safeQuestion_2_value)

        # Step-4.3.4: Safe question - 2 (Answer):
        answer_2 = "Teacher"
        safeQuestion_2_xpath_answer = safeQuestion_2_xpath_base + "//input[@type='text']"
        answer_2_Element = self.__appleIdRegisterBrowser.find_element_by_xpath(safeQuestion_2_xpath_answer)
        answer_2_Element.clear()
        answer_2_Element.send_keys(answer_2)

        # Step-4.3.5: Safe question - 3:
        safeQuestion_3_xpath_base = signupInput_xpath_safeQuestion + "//security-questions-answers/div/div[3]"
        safeQuestion_3_xpath = safeQuestion_3_xpath_base + '//select'
        safeQuestion_3_select = Select(self.__appleIdRegisterBrowser.find_element_by_xpath(safeQuestion_3_xpath))
        safeQuestion_3_value = "145" # 你去过的第一个海滨浴场是哪一个？
        safeQuestion_3_select.select_by_value(safeQuestion_3_value)

        # Step-4.3.6: Safe question - 3 (Answer):
        answer_3 = "Long Beach"
        safeQuestion_3_xpath_answer = safeQuestion_3_xpath_base + "//input[@type='text']"
        answer_3_Element = self.__appleIdRegisterBrowser.find_element_by_xpath(safeQuestion_3_xpath_answer)
        answer_3_Element.clear()
        answer_3_Element.send_keys(answer_3)













