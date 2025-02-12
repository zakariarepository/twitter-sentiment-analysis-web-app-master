# project/server/config.py
import os


class BaseConfig:
    """Base configuration."""

    FLASK_APP = "main/__init__.py"
    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious")
    DEBUG = False
    BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAKgOnwEAAAAAW7nKsRjNWJljyX0vob%%2FaDkseuYo%3D4XQvtLW54nwzySxjMXeccyPiOwN2j01Gy6rPwsIZm6Rh60wOPn"


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG = True
    FLASK_ENV = "development"


class TestingConfig(BaseConfig):
    """Testing configuration."""

    DEBUG = True
    FLASK_ENV = "testing"


class ProductionConfig(BaseConfig):
    """Production configuration."""

    DEBUG = False
    FLASK_ENV = "production"
