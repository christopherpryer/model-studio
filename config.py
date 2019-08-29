"""App config."""
import os
import urllib

# database
driver = '{SQL Server}'
server = '{%s}' % os.environ.get('SQL_SERVER')
database = '{%s}' % 'dev_testing'
_str = urllib.parse.quote_plus(('DRIVER={};SERVER={};DATABASE={}'
            ';Trusted_Connection=yes').format(
                driver,
                server,
                database))

class Config:
    """Global configuration variables."""

    # General Config
    SECRET_KEY = 'dev' #os.environ.get('SECRET_KEY')
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100MB limit

    # Assets
    LESS_BIN = os.environ.get('LESS_BIN')
    ASSETS_DEBUG = os.environ.get('ASSETS_DEBUG')
    LESS_RUN_IN_DEBUG = os.environ.get('LESS_RUN_IN_DEBUG')

    # Static Assets
    STATIC_FOLDER = os.environ.get('STATIC_FOLDER')
    TEMPLATES_FOLDER = os.environ.get('TEMPLATES_FOLDER')
    COMPRESSOR_DEBUG = os.environ.get('COMPRESSOR_DEBUG')

    # Database
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect=%s' % _str
    SQLALCHEMY_TRACK_MODIFICATIONS = False
