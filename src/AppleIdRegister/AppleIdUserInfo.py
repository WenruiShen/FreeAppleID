#!/usr/bin/python3
#coding=utf-8

##############################################
#
# Author:       Shen Wenrui
# Date:         20180518
# Description:
#
##############################################

import logging
logger = logging.getLogger("appleIdRegister")

class userInfo():
    def __init__(self):
        self.firstName = 'Test'
        self.lastName = 'tester'
        self.userBirthday = "04081994"
        self.userPassword = "Apple_test123"
        self.userEmail = "c3uiya+8tysatee8mklw@sharklasers.com"
        self.nation = "USA"  # 美国

    def initUserEmail(self, tempEmailAddr):
        self.userEmail = tempEmailAddr
