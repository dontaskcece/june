#!/usr/bin/env python

import os
rootdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
database = os.path.join(rootdir, 'data', 'development.sqlite')

# site inform
SITE_TITLE = 'Python China'
SITE_SIDEBAR = os.path.join(rootdir, 'data', 'sidebar.html')
SITE_ABOUT = '/node/about'
# SITE_ANALYTICS = 'UA-xxx-xxx'

SITE_STYLES = [
    '/static/css/bootstrap.css',
    '/static/css/bootstrap-responsive.css',
    '/static/css/pygments.css',
    '/static/css/site.css',
]

SITE_SCRIPTS = [
    '/static/js/jquery.min.js',
    '/static/js/bootstrap.js',
    '/static/js/site.js',
]


# This is a config file for development
DEBUG = True
SECRET_KEY = 'secret-key-for-development'

SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % database

# cache
CACHE_TYPE = 'filesystem'
CACHE_DIR = os.path.join(rootdir, 'data', 'cache')

# babel settings
BABEL_DEFAULT_LOCALE = 'zh'
BABEL_SUPPORTED_LOCALES = ['zh']
