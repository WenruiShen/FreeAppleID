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
import logging

# Database
DATABASES_CONFIGS = {
            'user':'freeapple',
            'password':'dbfreeid2018',
            'db':'FreeAppleIdDB',
            'host':'localhost',
            'port':3306,
            'charset':'utf8'
}

logger = logging.getLogger("database")

# 打开数据库连接
db = mysql.connector.connect(**DATABASES_CONFIGS)

class userModels():
    def __index__(self):
        self.__db = db

    #def insertNewUserInfo(self):

    def getAllUserInfo(self):
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 查询语句
        sql = "SELECT * FROM FreeAppleIdUserInfo "

        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                Id_P = row[0]
                userEmail = row[1]
                applePassword = row[2]
                LastName = row[3]
                FirstName = row[4]
                BirthDay = row[5]
                Address = row[6]
                City = row[7]

                # 打印结果
                logger.info("Id_P: %d, \tuserEmail: %s, \tapplePassword: %s,LastName:,age=%d,sex=%s,income=%d" % \
                      (fname, lname, age, sex, income))
        except Exception as err:
            logger.error(repr(err))






# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
#db.close()

