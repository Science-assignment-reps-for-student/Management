from app import create_app
from config.app_config import TestAppConfig
from config.db_config import RemoteDBConfig
from const.run_setting import RUN_SETTINGS

if __name__ == '__main__':
    app = create_app(TestAppConfig, RemoteDBConfig)
    app.run(**RUN_SETTINGS)