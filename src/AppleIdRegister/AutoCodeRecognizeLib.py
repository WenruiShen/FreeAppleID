#!/usr/bin/python3
#coding=utf-8

##############################################
#
# Author:       Shen Wenrui
# Date:         20180522
# Description:
#
##############################################

import json, urllib
from urllib import parse
import re
import logging

logger = logging.getLogger("appleIdRegister")

# &lt;a href=&quot;http://www.juhe.cn/docs/api/id/60/aid/352&quot; target=&quot;_blank&quot;&gt;查询&lt;/a&gt;

class authImgRecongizer():
    def __init__(self):
        self.__homepageUrl = "https://www.juhe.cn/"
        self.__userName = "15201122867"
        self.__password = "tz3dbqxx_jufei"
        self.__appkey = "8df14d494a62a4a5eefcb1dbc6b10eef"
        # 验证码的类型:
        self.__codeType = "1005"
        # 返回的数据的格式，json或xml，默认为json
        self.__dtype = "json"
        self.__apiUrl = "http://op.juhe.cn/vercode/index"

    def __isLegalAuthCode(self, authCode):
        # 正则判断：
        if re.match(r'\w{3,6}', authCode):
            return True
        else:
            logger.error("authCode: % is not legal." % authCode)
            return False

    # 识别验证码
    def __authCodeParseRequest(self, base64Str):
        try:
            params = {
                "key":      self.__appkey,  # 您申请到的APPKEY
                "codeType": self.__codeType,
                "base64Str": base64Str,  # 图片文件
                "dtype":    self.__dtype,

            }
            params = parse.urlencode(params).encode(encoding='UTF8')
            f = urllib.request.urlopen(self.__apiUrl, params)

            content = f.read()
            res = json.loads(content)
            error_code = res["error_code"]
            if error_code == 0:
                # 成功请求
                logger.info("authCodeParseRequest result: %s" % res["result"])
                return res["result"]
            else:
                logger.error("authCodeParseRequest: %s:%s" % (res["error_code"], res["reason"]))
                return None
        except Exception as err:
            logger.error(repr(err))
            return None

    def authCodeRecognize(self, base64Str):
        try:
            authCode = self.__authCodeParseRequest(base64Str)
            if authCode is None:
                return None
            if self.__isLegalAuthCode(authCode):
                return None
            return authCode
        except Exception as err:
            logger.error(repr(err))
            return None