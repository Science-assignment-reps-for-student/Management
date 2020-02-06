import os


class RemoteDBConfig:
    # DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_PASSWORD = 'scarfs0302@'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:'+DB_PASSWORD+'@54.180.174.253:3306/scarfs'
    SQLALCHEMY_TRACK_MODIFICATIONS = False