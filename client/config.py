import os
import sys

import django


TOKEN = '5140675106:AAHe5IaSOlAnjS4ExKJ7DL_qGZ2yHQP3hx8'

PARENT_PACKAGE = '..'
APP_PACKAGE = 'server'
PARENT_DIR = os.path.dirname(os.path.dirname(__file__))
APP_DIR = os.path.join(PARENT_DIR, APP_PACKAGE)

sys.path.append(APP_DIR)
sys.path.append(PARENT_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
