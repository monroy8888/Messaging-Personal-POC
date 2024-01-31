import os

from dotenv import dotenv_values
import sqlalchemy

config = dotenv_values(".env")

MYSQL_DATABASE = config.get("MYSQL_DATABASE")
MYSQL_USER = config.get("MYSQL_USER")
MYSQL_PASSWORD = config.get("MYSQL_PASSWORD")

DATABASE_URL = f"mysql+mysqlconnector://myuser:mypassword@db:3306/mydatabase"


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DATABASE_URL


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL")


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")


configuration = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}