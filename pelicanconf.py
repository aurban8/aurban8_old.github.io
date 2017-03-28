#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Andrea Urban'
SITENAME = "Andrea's First Website"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/AndreaUrbanPhD'),
          ('linkedin', 'http://www.linkedin.com/in/andrea-urban-phd'),
          ('github', 'http://github.com/aurban8'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md',)
#, 'ipynb')

PLUGIN_PATHS = ['pelican-plugins', 'plugins']

PLUGINS = ['i18n_subsites', 'ipynb.liquid']
#           , 'liquid_tags.img']
#'liquid_tags.img', #'liquid_tags.video',
#           'liquid_tags.notebook',]
#           'liquid_tags.youtube', 'liquid_tags.vimeo',
#           'liquid_tags.include_code',

THEME = "pelican-themes/pelican-bootstrap3"

JINJA_EXTENSIONS = ['jinja2.ext.i18n']
#JINJA_ENVIRONMENT = ['jinja2.ext.i18n']

#NOTEBOOK_DIR = 'notebooks'

#BOOTSTRAP_THEME = 'spacelab'
#BOOTSTRAP_THEME = 'cosmo'
BOOTSTRAP_THEME = 'simplex'

STATIC_PATHS = ['images']#, notebook]

PYGMENTS_STYLE = 'emacs'

DISPLAY_ARTICLE_INFO_ON_INDEX = True

SUMMARY_MAX_LENGTH = 200
