"""\
Default Configuration

Do NOT change the values here for risk of accidentally committing them.
Use the appropriate environment variable or create a settings_local.py instead.
"""

import os


HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')
DEBUG = os.environ.get('DEBUG')
SECRET_KEY = os.environ.get('SECRET_KEY')
SERVER_NAME = os.environ.get('SERVER_NAME')
