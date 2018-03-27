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


testUrl = appleIdSignUpPageUrl
print(testUrl)

browser.implicitly_wait(5)
browser.get(testUrl)
html = browser.page_source
#print(html)

authImgBase64_xpath = "/html/body/div[@id='content']/aid-web/div[@class='app-container']/div[@id='app-content']/" \
                    "div[@id='flow']/create-app/aid-create//div[@class='idms-flow-container']//div[@class='idms-step-content']/" \
                    "div/div/div[6]/div/create-captcha/" \
                    "div/div/div/div/div[1]/div/idms-captcha/div/img"

authImgElement = browser.find_element_by_xpath(authImgBase64_xpath)

print('authImgElement is: ' + str(authImgElement.get_attribute('innerHTML')))
authImgBase64 = authImgElement.get_attribute('src')
print('authImgBase64 is: ' + str(authImgBase64))

browser.quit()
exit()