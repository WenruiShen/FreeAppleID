#!/usr/bin/python3
#coding=utf-8

##############################################
#
# Author:       Shen Wenrui
# Date:         20180526
# Description:
#
##############################################

import mysql.connector

# Database
DATABASES_CONFIGS = {
            'user':'freeapple',
            'password':'dbfreeid2018',
            'db':'FreeAppleIdDB',
            'host':'localhost',
            'port':3306,
            'charset':'utf8'
}

# 打开数据库连接
dbconnector_freeId = mysql.connector.connect(**DATABASES_CONFIGS)


# 关闭数据库连接
#db.close()