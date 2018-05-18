




from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def userInputEmailAuthCode(browser, userInputAuthCode = "123456"):
    # Input auth code sent to the email.
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
