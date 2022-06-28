from datetime import timedelta


class Config(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    PORT = 80
    USER_DB_HOST = "localhost"
    USER_DB_NAME = "airbnb_user"
    USER_DB_USER = "root"
    USER_DB_PASSWORD = ""
    USER_DB_PORT = 3306
    USER_SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USER_DB_USER}:{USER_DB_PASSWORD}@{USER_DB_HOST}:{USER_DB_PORT}/{USER_DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ROOM_DB_HOST = "localhost"
    ROOM_DB_NAME = "airbnb_host"
    ROOM_DB_USER = "root"
    ROOM_DB_PASSWORD = ""
    ROOM_DB_PORT = 3306
    ROOM_SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{ROOM_DB_USER}:{ROOM_DB_PASSWORD}@{ROOM_DB_HOST}:{ROOM_DB_PORT}/{ROOM_DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USERNAME = ""
    MAIL_PASSWORD = ""
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_SECRET_KEY = ""
    SECURITY_PASSWORD_SALT = ""

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_SECRET_KEY = ""
    JWT_COOKIE_SECURE = False
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]

    GOOGLE_CLOUD_STORAGE_BUCKET_NAME = ""
