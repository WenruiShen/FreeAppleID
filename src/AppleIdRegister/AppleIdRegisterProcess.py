#!/usr/bin/python3
#coding=utf-8

##############################################
#
# Author:       Shen Wenrui
# Date:         20180518
# Description:
#
##############################################



# Step 3: thrn on the browser
browser = webdriver.Chrome()



# Step 5: Load the Account Sign up page.
appleIdBrowser = webdriver.Chrome()

print(appleIdSignUpPageUrl)
appleIdBrowser.implicitly_wait(5)
appleIdBrowser.get(appleIdSignUpPageUrl)
#html = appleIdBrowser.page_source
#print(html)


personalInfoInput(browser, signupInput_xpath_base, lastName, firstName, user_birthday)
appleIdPasswordInput(browser, signupInput_xpath_base, user_email, user_password)
safeQuestionInput(browser, signupInput_xpath_safeQuestion)


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



browser.quit()


