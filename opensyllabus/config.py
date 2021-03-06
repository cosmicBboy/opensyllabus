# -*- coding:utf8 -*-
"""
Author: Maxim Kosinov
Specialization: Python, HighLoad Crawlers, Data Mining, Scraping
E-Mail: astrey.labs@gmail.com
Skype: geminiozz
O-Desk: Astrey
"""


DATA_DIR = '/mnt/osp-archive-mount/document-dump'
TMP_DIR = '/mnt/osp-archive-mount/document-dump/code/opensyllabus/_tmp'

# log config
LOG_TO_FILE = True
FILE_LOG_VERBOSITY = 'debug'
CONSOLE_LOG_VERBOSITY = 'debug'
LOG_FILE = '/mnt/osp-archive-mount/document-dump/code/opensyllabus/_logs/opensyllabus.log'

# MongoDB configurations
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

PROCESS_REPORT_COUNT = 500
THREADS_COUNT = 10

try:
    from opensyllabus.local_config import *
except ImportError:
    pass