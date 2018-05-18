





import base64
from IPython.display import Image


# import PIL.Image

# Step-2: Get the Auth img.
def extractAuthImg(browser, authPenal_xpath):
    authImgBase64_xpath = authPenal_xpath + "/div[1]/div/idms-captcha/div/img"

    authImgElement = browser.find_element_by_xpath(authImgBase64_xpath)
    # print('authImgElement is: ' + str(authImgElement.get_attribute('innerHTML')))

    authImgBase64 = authImgElement.get_attribute('src')
    # print(authImgBase64)
    return authImgBase64


def saveAuthImg(authImgBase64, filename='001.jpeg'):
    authImgStr = base64.b64decode(authImgBase64[len('data:image/jpeg;base64, '):])
    authImg_f = open("001.jpeg", "wb")
    authImg_f.write(authImgStr)
    authImg_f.close()


def showAuthImg(filename='001.jpeg'):
    # Show in jupyter:
    Image(filename)

    # show in system:
    # im = PIL.Image.open('001.jpeg')
    # im.show()


def parsedCodeInput(browser, authPenal_xpath, parsed_auth_code):
    # Input the parsed auth code:
    authCode_xpath = authPenal_xpath + "/div[2]//input[@type='text']"
    authCode_Element = browser.find_element_by_xpath(authCode_xpath)
    authCode_Element.clear()
    authCode_Element.send_keys(parsed_auth_code)