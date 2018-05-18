#!/usr/bin/python3
#coding=utf-8



def getEmailListLength(tempEmailBrowser, emailContent_xpath):
    # Step 3: Email list:
    emailElementList = tempEmailBrowser.find_elements_by_xpath(emailContent_xpath)
    return len(emailElementList)

def getNextUpdateSec(tempEmailBrowser, emailContent_xpath_base):
    # Step 4: Get next update sec:
    remainUpdateSec_xpath = emailContent_xpath_base + "//table[@id='email_table']//div[@id='tick']"
    remainUpdateSec = re.findall(r"Next update in: (.+?) sec",
                                 tempEmailBrowser.find_element_by_xpath(remainUpdateSec_xpath).text)
    remainUpdateSec = remainUpdateSec[0] if len(remainUpdateSec)!=0 else '0'
    return int(remainUpdateSec)

def getLatestEmailDat(tempEmailBrowser, emailContent_xpath):
    # Step 3: Get the latest Email's date:
    latestEmailDate_xpath = emailContent_xpath + "[%d]/td[@class='td4']" % 1
    latestEmailDate = tempEmailBrowser.find_element_by_xpath(latestEmailDate_xpath).text
    return latestEmailDate

def getLatestEmailAuthCode(tempEmailBrowser, emailContent_xpath):
    # Step 4: Get the latest Email's context:
    latestEmailContent_xpath = emailContent_xpath + "[%d]/td[@class='td3']/span[@class='email-excerpt']" % 1
    latestEmailContent = tempEmailBrowser.find_element_by_xpath(latestEmailContent_xpath).text
    # Step 5: Parse out the Auth Code:
    return latestEmailContent

def getInboxInfo(tempEmailBrowser, emailContent_xpath):
    emailElementList = getEmailListLength(tempEmailBrowser, emailContent_xpath)
    latestEmailDate = getLatestEmailDat(tempEmailBrowser, emailContent_xpath)
    return emailElementList, latestEmailDate


def getTempEmailAddr(tempEmailBrowser, email_xpath_base):
    # Step 1: Select the Domain:
    emailDomain_xpath_select = getTempEmailDominSelectXpath(email_xpath_base)
    emailDomain_select = Select(tempEmailBrowser.find_element_by_xpath(emailDomain_xpath_select))
    # "guerrillamail.com", "sharklasers.com"
    emailDomain_value = "sharklasers.com"
    emailDomain_select.select_by_value(emailDomain_value)

    # Step 2: Get the Email address:
    emailAddr_xpath = getTempEmailAddrXpath(email_xpath_base)
    tempEmailAddr = tempEmailBrowser.find_element_by_xpath(emailAddr_xpath).text
    if not re.match(r'.+?@.+?\.com', tempEmailAddr):
        print("Illegal tempEmailAddr: " + tempEmailAddr)
        tempEmailAddr = None
    return tempEmailAddr


def loadTempEamilPage(tempEmailBrowser):
    guerrillamailUrl = 'https://www.guerrillamail.com/inbox'
    print("Open:" + guerrillamailUrl)
    # tempEmailBrowser.implicitly_wait(20)
    tempEmailBrowser.get(guerrillamailUrl)

    email_xpath_base = getEmailBaseXpath()
    try:
        # Explicitly wait.
        WebDriverWait(tempEmailBrowser, 20, 0.5).until(
            EC.presence_of_element_located((By.XPATH, getTempEmailAddrXpath(email_xpath_base)))
        )
    except TimeoutException as err:
        print("Failed to load: " + guerrillamailUrl)
        return False

    print("Get temp Email Addr: " + tempEmailAddr)
    return True