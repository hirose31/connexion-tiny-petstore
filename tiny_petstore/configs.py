# -*- coding: utf-8 -*-

import os


class Config():
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
    DEBUG = False
    TESTING = False
    APP_PORT = 9090
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = False  # don't show traceback even if in debug mode


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'production'
    DEBUG = False

    DB_NAME = 'prod.db'
    DB_PATH = os.path.join(Config.DATA_DIR, DB_NAME)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
                                             'sqlite:///{0}'.format(DB_PATH))
    SQLALCHEMY_ECHO = False


class DevConfig(Config):
    """Development configuration."""

    ENV = 'development'
    DEBUG = True

    DB_NAME = 'dev.db'
    DB_PATH = os.path.join(Config.DATA_DIR, DB_NAME)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
                                             'sqlite:///{0}'.format(DB_PATH))
    SQLALCHEMY_ECHO = True


class TestConfig(Config):
    """Testing configuration."""

    ENV = 'test'
    DEBUG = True
    TESTING = True

    SQLALCHEMY_DATABASE_URI = 'sqlite://'
