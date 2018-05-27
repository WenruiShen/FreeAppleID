#!/usr/bin/python3
#coding=utf-8

##############################################
#
# Author:       Shen Wenrui
# Date:         20180523
# Description:
#
##############################################

from __future__ import absolute_import, unicode_literals
import os

	
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Setting for Django-Python logging framework.
LOGGING_PATH = os.path.join(BASE_DIR, 'logs')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'appleIdRegisterFile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': os.path.join(LOGGING_PATH, 'appleIdRegister.log'),
            'encoding': 'utf8'
        },
        'appleStoreReviewFile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': os.path.join(LOGGING_PATH, 'appleStoreReview.log'),
            'encoding': 'utf8'
        },
        'tempEmailFile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': os.path.join(LOGGING_PATH, 'tempEmail.log'),
            'encoding': 'utf8'
        },
        'payAddrExtractFile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': os.path.join(LOGGING_PATH, 'payAddrExtract.log'),
            'encoding': 'utf8'
        },
        'databaseFile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': os.path.join(LOGGING_PATH, 'database.log'),
            'encoding': 'utf8'
        },
    },
    'loggers': {
        'appleIdRegister': {
            'handlers': ['console', 'appleIdRegisterFile'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'appleStoreReview': {
            'handlers': ['console', 'appleStoreReviewFile'],
            'level': 'DEBUG',
            'propagate': True,  # False
        },
        'tempEmail': {
            'handlers': ['console', 'tempEmailFile'],
            'level': 'DEBUG',
            'propagate': True,  # False
        },
        'payAddrExtract': {
            'handlers': ['console', 'payAddrExtractFile'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'database': {
            'handlers': ['console', 'databaseFile'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}

