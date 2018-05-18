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



    def personalInfoInput(self, lastName, firstName, user_birthday):
        # Step-1: Load personal info:

        # Step-2: Last_name:
        self.__lastNameInput(self, lastName)

        # Step-3: First_name:
        self.__firstNameInput(firstName)

        # Step-4: Nationality:
        nationality_xpath = self.__xpath.getPersonalInfoXpathNation()
        nationality_select = Select(self.__appleIdRegisterBrowser.find_element_by_xpath(nationality_xpath))
        nationality_value = "USA" # 美国
        nationality_select.select_by_value(nationality_value)

        # Step-5: BirthDay:
        birthday_xpath = self.__xpath.getPersonalInfoXpathBirthday()
        birthday_Element = self.__appleIdRegisterBrowser.find_element_by_xpath(birthday_xpath)
        birthday_Element.clear()
        birthday_Element.send_keys(user_birthday)


    def appleIdPasswordInput(self, signupInput_xpath_base, user_email, user_password):
        signupInput_xpath_safeQuestion = signupInput_xpath_base + "/div[4]/div"
        # Step-4.2.1: Apple-id (E-mail)
        email_xpath = signupInput_xpath_password + "/div[1]//input[@type='email']"
        email_Element = self.__appleIdRegisterBrowser.find_element_by_xpath(email_xpath)
        email_Element.clear()
        email_Element.send_keys(user_email)

        # Step-4.2.2: Password:
        password_xpath = signupInput_xpath_password + "/div[2]//new-password//input[@type='password']"
        password_Element = self.__appleIdRegisterBrowser.find_element_by_xpath(password_xpath)
        password_Element.clear()
        password_Element.send_keys(user_password)

        # Step-4.2.3: Password confirm:
        confirm_password_xpath = signupInput_xpath_password + "/div[2]//confirm-password//input[@type='password']"
        confirm_password_Element = self.__appleIdRegisterBrowser.find_element_by_xpath(confirm_password_xpath)
        confirm_password_Element.clear()
        confirm_password_Element.send_keys(user_password)


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













