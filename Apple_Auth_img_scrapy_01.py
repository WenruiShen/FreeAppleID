##############################################
#
# Author:       Shen Wenrui
# Date:         20180326
# Description:
#
##############################################

import sys
from selenium import webdriver

appleIdHomepageUrl = 'https://appleid.apple.com'
signPageUrl = '/#!&page=signin'


#help(webdriver)
browser = webdriver.Chrome()

# Apple-Id Signin page
signinUrl = appleIdHomepageUrl + signPageUrl
#signinUrl = 'http://www.baidu.com'
print(signinUrl)
browser.get(signinUrl)
html = browser.page_source

# Agent

# Https

#



#browser.quit()
#exit()