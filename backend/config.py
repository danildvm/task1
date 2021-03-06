# Rename this file to config.py and:
# Set SQLALCHEMY_DATABASE_URI
# Set SECRET_KEY
# Set WTF_CSRF_SECRET_KEY
import os


class Config(object):
    """ Global configuration."""

    DEBUG = False

    SECRET_KEY = 'ezj+e4m@auyzke$5)rnc%r!3%enk5%!lmwb22^md2_okgnqem0'

    WTF_CSRF_ENABLED = True

    WTF_CSRF_SECRET_KEY = 'ezj+e4m@auyzke$5)rnc%r!3%enk5%!lmwb22^md2_okgnqem0'

    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@db/postgres'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # password hashing rounds
    BCRYPT_LOG_ROUNDS = 14

    MEDIA_FOLDER = os.path.abspath(os.path.join(
        'client', 'apps', 'city_issues', 'media'))

    # mail configure
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'info.cityissues@gmail.com'
    MAIL_PASSWORD = 'passqwerty'
    ADMIN_MAIL_SUBJECT_PREFIX = '[CityView]'
    ADMIN_MAIL_SENDER = 'CityView Admin <contact@example.com>'


class ProductionConfig(Config):
    """ Production configuration."""
    DEBUG = False

    if 'DATABASE_URL' in os.environ:
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    if 'SECRET_KEY' in os.environ:
        SECRET_KEY = os.environ['SECRET_KEY']
    if 'WTF_CSRF_SECRET_KEY' in os.environ:
        WTF_CSRF_SECRET_KEY = os.environ['WTF_CSRF_SECRET_KEY']

    MEDIA_URL = 'https://limitless-oasis-36193.herokuapp.com/media/app/client/media/'


class DevelopmentConfig(Config):
    """ Development configuration."""
    DEBUG = True
