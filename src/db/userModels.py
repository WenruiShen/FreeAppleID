#!/usr/bin/python3
#coding=utf-8

##############################################
#
# Author:       Shen Wenrui
# Date:         20180526
# Description:
#
##############################################

#import pymysql
import mysql.connector

# Database
DATABASES_CONFIGS = {
            'user':'freeapple',
            'password':'dbfreeid2018',
            'db':'FreeAppleIdDB',
            'host':'127.0.0.1',
            'port':3306,
            'charset':'utf8'
}

# 打开数据库连接
db = mysql.connector.connect(**DATABASES_CONFIGS)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()

