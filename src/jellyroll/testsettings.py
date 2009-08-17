import os

BASE = os.path.abspath(os.path.dirname(__file__))

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/tmp/jellyroll.db'
INSTALLED_APPS = ['django.contrib.contenttypes', 'tagging', 'jellyroll']

JELLYROLL_PROVIDERS = ['jellyroll.providers.%s' % p[:-3]
                       for p in os.listdir(os.path.join(BASE, 'providers'))
                       if p.endswith('.py') and not p.startswith('_')]

# Silence logging
import logging

class Silence(logging.Handler):
    def emit(self, record):
        pass

logging.getLogger("jellyroll").addHandler(Silence())

# Coverage, if installed
try:
    from test_coverage.settings import *
except ImportError:
    pass
else:
    INSTALLED_APPS.append('test_coverage')
    
    COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(BASE)), 'coverage')
    COVERAGE_MODULE_EXCLUDES = ['^django\.', '^tagging\.', 'settings$', '\.templates$', '\.fixtures$']
    
    if not os.path.exists(COVERAGE_REPORT_HTML_OUTPUT_DIR):
        os.mkdir(COVERAGE_REPORT_HTML_OUTPUT_DIR)