#!/usr/bin/python3
#coding=utf-8

##############################################
#
# Author:       Shen Wenrui
# Date:         20180526
# Description:
#
##############################################

from src.db.userModels import userModels
from src.Services.loggingInit import setup_logging

setup_logging()

usermodel = userModels()
#usermodel.dbTest()
usermodel.getAllUserInfo()