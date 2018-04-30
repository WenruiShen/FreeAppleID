#coding=utf-8
##############################################
#
# Author:       Shen Wenrui
# Date:         20180326
# Description:
#
##############################################

import sys
from selenium import webdriver

baiduUrl = 'http://www.baidu.com'

appleHomepageUrl = 'https://www.apple.com/cn/'
# Apple-Id Signin page
appleIdHomePageUrl = 'https://appleid.apple.com'
#signPageUrl = '/#!&page=signin'
#signinUrl = appleIdHomepageUrl + signPageUrl

# Apple-Id Signup page
appleIdSignUpPageUrl = appleIdHomePageUrl + '/account'

browser = webdriver.Chrome()

############################################################################################################

'''
firstName = 'Shen'
lastName = 'Wenrui'
user_birthday = "1992年07月20日"
user_password = "Apple_swr123"
#user_email = "zhangxiaozhai80@gmail.com"
user_email = "zhangtao002a@protonmail.com"   #"Apple_swr123"
'''
'''
firstName = 'Guan'
lastName = 'Jinxi'
user_birthday = "04081992"
user_password = "Apple_gjx123"
user_email = "guanjinxi001a@protonmail.com"
'''

'''
firstName = 'Shi'
lastName = 'Jiachen'
user_birthday = "04081994"
user_password = "Apple_sjc123"
user_email = "shijiachen001a@protonmail.com"
'''

firstName = 'Test'
lastName = 'tester'
user_birthday = "04081994"
user_password = "Apple_test123"
user_email = "c3uiya+8tysatee8mklw@sharklasers.com"

############################################################################################################

# Step-1: Load the Account Sign up page.
testUrl = appleIdSignUpPageUrl
print(testUrl)

browser.implicitly_wait(5)
browser.get(testUrl)
#html = browser.page_source
#print(html)

############################################################################################################

# Step-2: Get the Auth img.
signup_xpath_base = "/html/body/div[@id='content']/aid-web/div[@class='app-container']/div[@id='app-content']/" \
                    "div[@id='flow']/create-app/aid-create"
signupInput_xpath_base = signup_xpath_base + \
                    "//div[@class='idms-flow-container']//div[@class='idms-step-content']/div/div"

authPenal_xpath = signupInput_xpath_base + "/div[6]/div/create-captcha/div/div/div/div/"
authImgBase64_xpath = authPenal_xpath + "/div[1]/div/idms-captcha/div/img"

authImgElement = browser.find_element_by_xpath(authImgBase64_xpath)
#print('authImgElement is: ' + str(authImgElement.get_attribute('innerHTML')))

authImgBase64 = authImgElement.get_attribute('src')
#print(authImgBase64)

############################################################################################################

import base64
authImgStr = base64.b64decode(authImgBase64[len('data:image/jpeg;base64, '):])
authImg_f = open("001.jpeg", "wb")
authImg_f.write(authImgStr)
authImg_f.close()

from IPython.display import Image
Image(filename='001.jpeg')
#import PIL.Image
#im = PIL.Image.open('001.jpeg')
#im.show()

# Step-3: Recognize the Auth img.
#parsed_auth_code = "CF6MZ"
from AutoCodeRecognize import request1
parsed_auth_code = request1(authImgBase64[len('data:image/jpeg;base64, '):])
#parsed_auth_code = "cl6a9"
print(parsed_auth_code)

# Input the parsed auth code:
authCode_xpath = authPenal_xpath + "/div[2]//input[@type='text']"
authCode_Element = browser.find_element_by_xpath(authCode_xpath)
authCode_Element.clear()
authCode_Element.send_keys(parsed_auth_code)

############################################################################################################

# Step-4: Input personal information for signing up.
signupInput_xpath_personalInfo = signupInput_xpath_base + "/div[2]/div"
signupInput_xpath_password     = signupInput_xpath_base + "/div[3]/div"
signupInput_xpath_safeQuestion = signupInput_xpath_base + "/div[4]/div"

# Step-4.1.1: Last_name:
last_name_xpath = signupInput_xpath_personalInfo + "/div[1]//last-name-input//input"
last_name_Element = browser.find_element_by_xpath(last_name_xpath)
last_name_Element.clear()
last_name_Element.send_keys(lastName)

# Step-4.1.2: First_name:
first_name_xpath = signupInput_xpath_personalInfo + "/div[1]//first-name-input//input"
first_name_Element = browser.find_element_by_xpath(first_name_xpath)
first_name_Element.clear()
first_name_Element.send_keys(firstName)

# Step-4.1.3: Nationality:
from selenium.webdriver.support.ui import Select
nationality_xpath = signupInput_xpath_personalInfo + "/div[2]//select"
nationality_select = Select(browser.find_element_by_xpath(nationality_xpath))
nationality_value = "USA" # 美国
nationality_select.select_by_value(nationality_value)

# Step-4.1.4: BirthDay:
birthday_xpath = signupInput_xpath_personalInfo + "/div[3]//input"
birthday_Element = browser.find_element_by_xpath(birthday_xpath)
birthday_Element.clear()
birthday_Element.send_keys(user_birthday)

# Step-4.2.1: Apple-id (E-mail)
email_xpath = signupInput_xpath_password + "/div[1]//input[@type='email']"
email_Element = browser.find_element_by_xpath(email_xpath)
email_Element.clear()
email_Element.send_keys(user_email)

# Step-4.2.2: Password:
password_xpath = signupInput_xpath_password + "/div[2]//new-password//input[@type='password']"
password_Element = browser.find_element_by_xpath(password_xpath)
password_Element.clear()
password_Element.send_keys(user_password)

# Step-4.2.3: Password confirm:
confirm_password_xpath = signupInput_xpath_password + "/div[2]//confirm-password//input[@type='password']"
confirm_password_Element = browser.find_element_by_xpath(confirm_password_xpath)
confirm_password_Element.clear()
confirm_password_Element.send_keys(user_password)

# Step-4.3.1: Safe question - 1:
safeQuestion_1_xpath_base = signupInput_xpath_safeQuestion + "//security-questions-answers/div/div[1]"
safeQuestion_1_xpath = safeQuestion_1_xpath_base + '//select'
safeQuestion_1_select = Select(browser.find_element_by_xpath(safeQuestion_1_xpath))
safeQuestion_1_value = "130" # 你少年时代最好的朋友叫什么名字？
safeQuestion_1_select.select_by_value(safeQuestion_1_value)

# Step-4.3.2: Safe question - 1 (Answer):
answer_1 = "Bob"
safeQuestion_1_xpath_answer = safeQuestion_1_xpath_base + "//input[@type='text']"
answer_1_Element = browser.find_element_by_xpath(safeQuestion_1_xpath_answer)
answer_1_Element.clear()
answer_1_Element.send_keys(answer_1)

# Step-4.3.3: Safe question - 2:
safeQuestion_2_xpath_base = signupInput_xpath_safeQuestion + "//security-questions-answers/div/div[2]"
safeQuestion_2_xpath = safeQuestion_2_xpath_base + '//select'
safeQuestion_2_select = Select(browser.find_element_by_xpath(safeQuestion_2_xpath))
safeQuestion_2_value = "136" # 你的理想工作是什么？
safeQuestion_2_select.select_by_value(safeQuestion_2_value)

# Step-4.3.4: Safe question - 2 (Answer):
answer_2 = "Teacher"
safeQuestion_2_xpath_answer = safeQuestion_2_xpath_base + "//input[@type='text']"
answer_2_Element = browser.find_element_by_xpath(safeQuestion_2_xpath_answer)
answer_2_Element.clear()
answer_2_Element.send_keys(answer_2)

# Step-4.3.5: Safe question - 3:
safeQuestion_3_xpath_base = signupInput_xpath_safeQuestion + "//security-questions-answers/div/div[3]"
safeQuestion_3_xpath = safeQuestion_3_xpath_base + '//select'
safeQuestion_3_select = Select(browser.find_element_by_xpath(safeQuestion_3_xpath))
safeQuestion_3_value = "145" # 你去过的第一个海滨浴场是哪一个？
safeQuestion_3_select.select_by_value(safeQuestion_3_value)

# Step-4.3.6: Safe question - 3 (Answer):
answer_3 = "Long Beach"
safeQuestion_3_xpath_answer = safeQuestion_3_xpath_base + "//input[@type='text']"
answer_3_Element = browser.find_element_by_xpath(safeQuestion_3_xpath_answer)
answer_3_Element.clear()
answer_3_Element.send_keys(answer_3)

# Submit
submit_xpath = signup_xpath_base + "//div[@class='idms-flow-container']//div[@class='idms-step-footer clearfix']//button[@type='button']"
browser.find_element_by_xpath(submit_xpath).click()


############################################################################################################

# Input auth code sent to the email.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def userInputEmailAuthCode(browser, userInputAuthCode = "123456"):
    emailAuthCode_xpath_base = "/html/body//step-verify-code"
    emailAuthCode_xpath_line = emailAuthCode_xpath_base + "//div[@class='security-code-container force-ltr']"
    #for i in range[1]:
    #print(i)
    index = 0
    for num in list(userInputAuthCode):
        index = index + 1
        emailAuthCode_xpath_input = emailAuthCode_xpath_line + "/div[%s]/input" % index
        #print(emailAuthCode_xpath_input)
        authCodeInputElement = browser.find_element_by_xpath(emailAuthCode_xpath_input)
        authCodeInputElement.clear()
        authCodeInputElement.send_keys(num)
    #Submit the auth code
    emailAuthCode_xpath_buttonOk = emailAuthCode_xpath_base + \
                            "//div[@class='button-group flow-controls clearfix pull-right ']/button[1]"
    browser.find_element_by_xpath(emailAuthCode_xpath_buttonOk).click()
    #element = WebDriverWait(browser, 10).until(
    #    EC.presence_of_element_located((By.ID, "myDynamicElement"))
    #)
    #browser.implicitly_wait(3)
    #if browser.find_element_by_xpath(emailAuthCode_xpath_input) is None:
    #    break



browser.implicitly_wait(3)
#userInputEmailAuthCode(browser, userInputAuthCode = "966412")

############################################################################################################

# - 2nd - Page:
'''
accountManageUrl = "https://appleid.apple.com/account/manage"
print(accountManageUrl)

browser.implicitly_wait(5)
browser.get(accountManageUrl)


browser.quit()
'''


