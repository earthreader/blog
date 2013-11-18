#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

CI = os.environ.get('CI') == 'true'

AUTHOR = u'Earth Reader Team'
SITENAME = u'Earth Reader Blog'
SITEURL = 'http://blog.earthreader.org'

THEME = 'svbhack'
USER_LOGO_URL = 'https://0.gravatar.com/avatar' \
                '/c52c2e139b7a530c0b0c7114e5e49d5c?s=280'

TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'

ARTICLE_EXCLUDES = ['pages', 'plugins']

ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/' \
              if CI else ARTICLE_SAVE_AS

STATIC_PATHS = [
    'favicon.ico',
    'content/images'
]
EXTRA_PATH_METADATA = {
    'favicon.ico': {'path': 'favicon.ico'}
}


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'index.xml'
CATEGORY_FEED_ATOM = 'category/%s.xml'
TAG_FEED_ATOM = 'tag/%s.xml'

# Blogroll
LINKS = [
    ('Website', 'http://earthreader.org/'),
    ('GitHub', 'https://github.com/earthreader')
]

# Social widget
SOCIAL = []

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = not CI

USE_FOLDER_AS_CATEGORY = False

TYPOGRIFY = True

PLUGIN_PATH = 'plugins'
PLUGINS = [
    'gravatar'
]
