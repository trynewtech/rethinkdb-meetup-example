"""\
Default Configuration

Do NOT change the values here for risk of accidentally committing them.
Use the appropriate environment variable or create a settings_local.py instead.
"""

import os


# Server settings
HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')
DEBUG = os.environ.get('DEBUG')
SECRET_KEY = os.environ.get('SECRET_KEY')
SERVER_NAME = os.environ.get('SERVER_NAME')


# Database settings
DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE_PORT = os.environ.get('DATABASE_PORT')
DATABASE_DB = os.environ.get('DATABASE_DB')
DATABASE_AUTH_KEY = os.environ.get('DATABASE_AUTH_KEY')
