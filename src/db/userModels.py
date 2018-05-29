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
import re

from .dbsettings import DATABASES_CONFIGS

logger = logging.getLogger("database")

class userModels():
    #def __init__(self):
    #    self.db = dbconnector_freeId

    def dbVersion(self):
        # 打开数据库连接
        self.db = mysql.connector.connect(**DATABASES_CONFIGS)
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute("SELECT VERSION()")
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        logger.info("Database version : %s " % data)
        # 关闭数据库连接
        self.db.close()

    def getAllUserInfo(self):
        try:
            # 打开数据库连接
            self.db = mysql.connector.connect(**DATABASES_CONFIGS)

            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = self.db.cursor()
            # SQL 查询语句
            sql = "SELECT * FROM FreeAppleIdUserInfo "
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            logger.info("User info rows' size: %d" % len(results))
            for row in results:
                Id_P = row[0]
                userEmail = row[1]
                applePassword = row[2]
                LastName = row[3]
                FirstName = row[4]
                BirthDay = row[5]
                create_time = row[6]
                update_time = row[7]
                # 打印结果
                logger.info("Id_P: %d, \tuserEmail: %s, \tapplePassword: %s, \tLastName: %s, \tFirstName: %s," \
                            " \tBirthDay: %s, \tcreate_time:%s, \tupdate_time:%s" % \
                      (Id_P, userEmail, applePassword, LastName, FirstName, BirthDay, \
                       create_time, update_time))
            return results
        except Exception as err:
            logger.error(repr(err))
            return None
        finally:
            # 关闭数据库连接
            self.db.close()

    # select by email:
    def getUserInfoByEmail(self, tempEmailAddr):
        if tempEmailAddr is None:
            logger.error()
            return None
        try:
            # 打开数据库连接
            self.db = mysql.connector.connect(**DATABASES_CONFIGS)

            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = self.db.cursor()
            # SQL 查询语句
            sql = "SELECT * FROM FreeAppleIdUserInfo WHERE userEmail='%s'" % (tempEmailAddr)
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            row = cursor.fetchone()
            if row is None:
                logger.info("User: %s is empty" % tempEmailAddr)
                return None
            logger.info("Get user: %s" % tempEmailAddr)

            Id_P = row[0]
            userEmail = row[1]
            applePassword = row[2]
            LastName = row[3]
            FirstName = row[4]
            BirthDay = row[5]
            create_time = row[6]
            update_time = row[7]
            # 打印结果
            logger.info("Id_P: %d, \tuserEmail: %s, \tapplePassword: %s, \tLastName: %s, \tFirstName: %s," \
                        " \tBirthDay: %s, \tcreate_time:%s, \tupdate_time:%s" % \
                      (Id_P, userEmail, applePassword, LastName, FirstName, BirthDay, create_time, update_time))
            return row
        except Exception as err:
            logger.error(repr(err))
            return None
        finally:
            # 关闭数据库连接
            self.db.close()

    def insertNewUserInfo(self, userEmail, applePassword, LastName, FirstName, BirthDay):
        if (userEmail is None) or (applePassword is None) or (LastName is None) or \
                                            (FirstName is None) or (BirthDay is None):
            logger.error("userEmail and applePassword must not be None!")
            return False
        if not re.match(r'\d{4}-\d{2}-\d{2}', BirthDay):
            logger.error("BirthDay: %s does not match YYYY-MM-DD format!" % BirthDay)
            return False
        try:
            # 打开数据库连接
            self.db = mysql.connector.connect(**DATABASES_CONFIGS)

            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = self.db.cursor()
            sql = "INSERT INTO FreeAppleIdUserInfo " \
                  "(userEmail, applePassword, LastName, FirstName, BirthDay) " \
                  "VALUES ('%s','%s','%s','%s','%s')" % \
                  (userEmail, applePassword, LastName, FirstName, BirthDay)
            # 执行SQL语句
            cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
            # 打印结果
            logger.info("insertNewUserInfo:[userEmail: %s, \tapplePassword: %s, \tLastName: %s, \tFirstName: %s," \
                        " \tBirthDay: %s]" % \
                        (userEmail, applePassword, LastName, FirstName, BirthDay))
            return True
        except Exception as err:
            # 如果发生错误则回滚
            self.db.rollback()
            logger.error(repr(err))
            return False
        finally:
            # 关闭数据库连接
            self.db.close()

    def updateUserInfo(self, userEmail, applePassword, LastName, FirstName, BirthDay):
        if (userEmail is None) or (applePassword is None) or (LastName is None) or \
                (FirstName is None) or (BirthDay is None):
            logger.error("userEmail and applePassword must not be None!")
            return False
        if (BirthDay is not None) and not re.match(r'\d{4}-\d{2}-\d{2}', BirthDay):
            logger.error("BirthDay: %s does not match YYYY-MM-DD format!" % BirthDay)
            return False
        try:
            # 打开数据库连接
            self.db = mysql.connector.connect(**DATABASES_CONFIGS)

            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = self.db.cursor()
            sql = "UPDATE FreeAppleIdUserInfo SET " \
                  "applePassword='%s', LastName='%s', FirstName='%s', BirthDay='%s' " \
                  "WHERE userEmail='%s'" % \
                  (applePassword, LastName, FirstName, BirthDay, userEmail)
            # 执行SQL语句
            cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
            # 打印结果
            logger.info("updateUserInfo userEmail: %s: [applePassword: %s, \tLastName: %s, \tFirstName: %s," \
                        " \tBirthDay: %s]" % \
                        (userEmail, applePassword, LastName, FirstName, BirthDay))
            return True
        except Exception as err:
            # 如果发生错误则回滚
            self.db.rollback()
            logger.error(repr(err))
            return False
        finally:
            # 关闭数据库连接
            self.db.close()

    def deleteUserInfo(self, userEmail):
        if userEmail is None:
            logger.error("userEmail must not be None!")
            return False
        try:
            # 打开数据库连接
            self.db = mysql.connector.connect(**DATABASES_CONFIGS)

            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = self.db.cursor()
            sql = "DELETE FROM FreeAppleIdUserInfo " \
                  "WHERE userEmail='%s'" % (userEmail)
            # 执行SQL语句
            cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
            # 打印结果
            logger.info("deleteUserInfo userEmail: %s" % userEmail)
            return True
        except Exception as err:
            # 如果发生错误则回滚
            self.db.rollback()
            logger.error(repr(err))
            return False
        finally:
            # 关闭数据库连接
            self.db.close()

    def dbTest(self):
        userEmail       = 'wenrui.shen@icloud.com'
        applePassword   = 'wenrui1992A'
        LastName        = 'Shen'
        FirstName       = 'Wenrui'
        BirthDay        = '2018-05-28'

        self.dbVersion()
        self.insertNewUserInfo(userEmail, applePassword, LastName, FirstName, BirthDay)
        self.getAllUserInfo()

        BirthDay = '2018-01-01'
        self.updateUserInfo(userEmail, applePassword, LastName, FirstName, BirthDay)
        self.getUserInfoByEmail(userEmail)

        self.deleteUserInfo(userEmail)
        self.getUserInfoByEmail(userEmail)

