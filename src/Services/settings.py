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
import datetime
import logging
	
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangodb01',
        'USER': 'postgres',
        'PASSWORD': 'presqlswr123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Setting for Django-Python logging framework.
LOGGING_PATH = os.path.join(BASE_DIR, 'django_logging_files')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'standard': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
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
        },
        'appleStoreReviewFile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': os.path.join(LOGGING_PATH, 'appleStoreReview.log'),
        },
        'tempEmailFile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': os.path.join(LOGGING_PATH, 'tempEmail.log'),
        },
        'payAddrExtractFile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': os.path.join(LOGGING_PATH, 'payAddrExtract.log'),
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
        }
    }
}

