##############################################
#
# Author:       Shen Wenrui
# Date:         20180326
# Description:
#
##############################################

import sys
from selenium import webdriver

appleHomepageUrl = 'https://www.apple.com/cn/'
appleIdHomepageUrl = 'https://appleid.apple.com'
signPageUrl = '/#!&page=signin'
signinUrl = appleIdHomepageUrl + signPageUrl
baiduUrl = 'http://www.baidu.com'

#help(webdriver)
browser = webdriver.Chrome()

# Apple-Id Signin page

testUrl = appleIdHomepageUrl
print(testUrl)
browser.get(testUrl)
html = browser.page_source
print(html)
#

# Agent

# Https

#



#browser.quit()
#exit()