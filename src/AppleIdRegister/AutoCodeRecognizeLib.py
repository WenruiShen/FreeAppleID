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

import logging
logger = logging.getLogger("appleIdRegister")

class authImgRecongizer():
    def __init__(self):
        self.__apiUrl = "https://www.juhe.cn/"
        self.__userName = "15201122867"
        self.__password = "tz3dbqxx_jufei"
        self.__appkey = "8df14d494a62a4a5eefcb1dbc6b10eef"
        # 验证码的类型:
        # &lt;a href=&quot;http://www.juhe.cn/docs/api/id/60/aid/352&quot; target=&quot;_blank&quot;&gt;查询&lt;/a&gt;
        self.__codeType = "1005"
        # 返回的数据的格式，json或xml，默认为json
        self.__dtype = "json"

    # 识别验证码
    def authCodeParseRequest(self, base64Str):
        url = "http://op.juhe.cn/vercode/index"
        params = {
            "key":      self.__appkey,  # 您申请到的APPKEY
            "codeType": self.__codeType,
            "base64Str": base64Str,  # 图片文件
            "dtype":    self.__dtype,

        }
        params = parse.urlencode(params).encode(encoding='UTF8')
        f = urllib.request.urlopen(url, params)

        content = f.read()
        res = json.loads(content)
        if res:
            error_code = res["error_code"]
            if error_code == 0:
                # 成功请求
                return res["result"]
            else:
                return "%s:%s" % (res["error_code"], res["reason"])
        else:
            return "request api error"
