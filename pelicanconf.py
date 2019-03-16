#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = SITENAME = u'Side Quest Completed'
SITEURL = 'http://sidequestcompleted.com'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'
LANG = u'en_US.UTF-8'
LOCALE = u'en_US'
CC_LICENSE = u'CC-BY-NC-SA'

# Sets Tagcloud usage
TAG_CLOUD_STEPS = 8
TAG_CLOUD_MAX_ITEMS = 150
DISPLAY_TAGS_INLINE = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds.atom'
CATEGORY_FEED_ATOM = 'feeds/%s.atom'
FEED_ALL_RSS = 'feeds.rss'
CATEGORY_FEED_RSS = 'feeds/%s.rss'
FEED_USE_SUMMARY = True

# Github Profile
GITHUB_URL = 'https://github.com/side-quest-completed/'

# Social widget
SOCIAL = (
    ('GitHub', 'github', 'https://github.com/side-quest-completed/sidequestcompleted.com'),
    # ('Twitter', 'twitter', 'https://twitter.com/sidequestcompleted'),
    # ('Facebook', 'facebook', 'https://facebook.com/??????'),
    # ('iTunes', 'apple', 'https://itunes.apple.com/en/podcast/??????/?????'),
    # ('YouTube', 'youtube', 'http://youtube.com/??????'),
    # ('RSS Feed', 'rss', 'http://feeds.feedburner.com/???????'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DIRECT_TEMPLATES = [
    'archives',
    'authors',
    'categories',
    'index',
    'search',
]
STATIC_PATHS = [
    'extra',
    'images',
]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
}

THEME = './themes/pelican-bootstrap3'
PLUGIN_PATHS = ['./plugins', ]
PLUGINS = [
    # 'castalio',
    'caster',
    'featured_image',
    'feed_summary',
    'pelican-podcast-feed',
    'sitemap',
    'summary',
    'tipue_search',
]
SUMMARY_END_MARKER = "<!-- more -->"

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

SUBSCRIBE = [
    # ('iTunes', 'https://itunes.apple.com/br/podcast/castalio-podcast/id446259197'),
    # ('Pocket Casts', 'http://pca.st/castalio'),
    # ('Podflix', 'https://podflix.com.br/castaliopodcast'),
    (None, None),
    ('FeedBurner (RSS Feed)', 'http://feeds.feedburner.com/SideQuestCompletedRSS'),
    # ('Spotify do Castálio', 'https://open.spotify.com/user/elyezermr/playlist/0PDXXZRXbJNTPVSnopiMXg'),
    # ('YouTube', 'http://bit.ly/CanalCastalio'),
    # ('Overcast', 'https://overcast.fm/itunes446259197/cast-lio-podcast'),
]

# Disqus configuration
# DISQUS_SITENAME = 'castliopodcast'
# GOOGLE_ANALYTICS = "UA-21449168-1"

# Dark navbar
BOOTSTRAP_NAVBAR_INVERSE = True

# Site banner in the sidebar
BANNER = True
BANNER_ALL_PAGES = True
BANNER_IMAGE = 'images/gdslogobig.png'
BANNER_IMAGE_CLASSES = 'img-circle'
BANNER_SUBTITLE = u'A hobbyist gamedev adventure!'
BANNER_BACKGROUND_COLOR='#fff'
SITELOGO = 'images/gdslogobig.png'
SITELOGO_SIZE = 20
HIDE_SITENAME = True
HIDE_SIDEBAR = True
SIDEBAR_BRAND_SUBTITLE = u"A hobbyist gamedev adventure!"
SIDEBAR_BRAND_IMAGE = 'images/gdslogobig.png'
SIDEBAR_BRAND_IMAGE_HEIGHT = 300
FAVICON = 'images/gdslogobig.ico'

# iTunes plugin settings
PODCAST_FEED_PATH = u'feeds/podcast.rss'
PODCAST_FEED_TITLE = u'Side Quest Completed'
PODCAST_FEED_EXPLICIT = u'No'
PODCAST_FEED_LANGUAGE = u'en'
PODCAST_FEED_COPYRIGHT = u'&#x2117; &amp; &#xA9; 2011-{0} {1}'.format(
    datetime.now().year, AUTHOR)
PODCAST_FEED_SUBTITLE = u'A gamedev hobbyist journey'
PODCAST_FEED_AUTHOR = AUTHOR
PODCAST_FEED_SUMMARY = (
    'A podcast about game development as a hobby.'
)
PODCAST_FEED_IMAGE = 'http://sidequestcompleted.com/images/sidequestcompleted-podcast.png'
PODCAST_FEED_CATEGORY = ['Technology', 'Podcasting']

# Cleaner page links
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Show author name
SHOW_ARTICLE_AUTHOR = True

# Show comments count
DISQUS_DISPLAY_COUNTS = True

# Show article info in the index
DISPLAY_ARTICLE_INFO_ON_INDEX = True

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    # ('About', '/about.html'),
    # ('Agenda', '/agenda.html'),
    ('Episodes', '/archives.html'),
    # ('YouTube', '/youtube.html')
)
