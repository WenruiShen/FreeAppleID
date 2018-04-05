#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib
from urllib import parse


# 识别验证码
def request1(base64Str, appkey = "8df14d494a62a4a5eefcb1dbc6b10eef"):
    url = "http://op.juhe.cn/vercode/index"
    params = {
        "key": appkey,  # 您申请到的APPKEY
        "codeType": "1005",
    # 验证码的类型，&lt;a href=&quot;http://www.juhe.cn/docs/api/id/60/aid/352&quot; target=&quot;_blank&quot;&gt;查询&lt;/a&gt;
        "base64Str": base64Str,  # 图片文件
        "dtype": "json",  # 返回的数据的格式，json或xml，默认为json

    }
    params = parse.urlencode(params).encode(encoding='UTF8')
    f = urllib.request.urlopen(url, params)

    content = f.read()

    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            return res["result"]
        else:
            return "%s:%s" % (res["error_code"], res["reason"])
    else:
        return "request api error"
