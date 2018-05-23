#!/usr/bin/python3
#coding=utf-8

##############################################
#
# Author:       Shen Wenrui
# Date:         20180523
# Description:
#
##############################################

import logging.config

from .settings import LOGGING

def setup_logging():
    logging.config.dictConfig(LOGGING)