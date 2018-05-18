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

            # Step-1: Load appleId SignUp page.
            if not self.__appleIdRegisterOperator.loadAppleIdSignUpPage():
                return False

            # Step-2: Input personal Info.
            if not self.__appleIdRegisterOperator.inpuAllInfo():
                print("Failed input personal info.")
                return False

            for i in range(3):
                # Step-3: Recognize the auth img.

                # Step-4: Submit personal info & auth image's code.
                if False:
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










authPenal_xpath = signupInput_xpath_base + "/div[6]/div/create-captcha/div/div/div/div/"

# Step-3: Recognize the Auth img.
authImgBase64 = extractAuthImg(browser, authPenal_xpath)

#filename='001.jpeg'
#saveAuthImg(authImgBase64, filename)
#showAuthImg(filename)

#parsed_auth_code = "CF6MZ"
parsed_auth_code = authCodeParseRequest(authImgBase64[len('data:image/jpeg;base64, '):])
print(parsed_auth_code)

parsedCodeInput(browser, authPenal_xpath, parsed_auth_code)


# Submit personal information.
submit_xpath = signup_xpath_base + "//div[@class='idms-flow-container']//div[@class='idms-step-footer clearfix']//button[@type='button']"
browser.find_element_by_xpath(submit_xpath).click()


# Input auth code sent to the email.
browser.implicitly_wait(3)
userInputEmailAuthCode(browser, userInputAuthCode = "966412")



# - 2nd - Page:

accountManageUrl = "https://appleid.apple.com/account/manage"
print(accountManageUrl)

browser.implicitly_wait(5)
browser.get(accountManageUrl)




