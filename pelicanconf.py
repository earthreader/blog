#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

CI = os.environ.get('CI') == 'true'

AUTHOR = u'Earth Reader Team'
SITENAME = u'Earth Reader Blog'
SITEURL = 'http://blog.earthreader.org'

TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'

ARTICLE_EXCLUDES = ['pages', 'plugins']

ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/' \
              if CI else ARTICLE_SAVE_AS

STATIC_PATHS = ['content/images']


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
