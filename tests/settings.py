#!/usr/bin/env
# -*- encoding: utf-8
# vim: ts=4 et sw=4 sts=4

"""
"""

from django.conf.settings.defaults import *

DEBUG=True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}
INSTALLED_APPS = {
    'tests',
    'category',
}
ROOT_URLCONF='urls'
