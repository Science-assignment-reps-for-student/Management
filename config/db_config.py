import os

class RemoteDBConfig:
    DB_PASSWORD = os.getenv("SCARFS_PASSWORD")
    SQLALCHEMY_DATABASE_URI = 'mysql://root:'+DB_PASSWORD+'@54.180.174.253:3306/scarfs_development'
    SQLALCHEMY_TRACK_MODIFICATIONS = False