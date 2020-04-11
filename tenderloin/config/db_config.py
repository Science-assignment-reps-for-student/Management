import os


class RemoteDBConfig:
    DB_PASSWORD = os.getenv("SCARFS_PASSWORD")
    SQLALCHEMY_DATABASE_URI = (
        "mysql://root:"
        + DB_PASSWORD
        + "@scarfs.cm63idi6gyr1.ap-northeast-2.rds.amazonaws.com/scarfs_production"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
