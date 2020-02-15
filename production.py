from app import create_app
from config.app_config import ProductionAppconfig
from config.db_config import RemoteDBConfig
from const.run_setting import RUN_SETTINGS

if __name__ == '__main__':
    app = create_app(ProductionAppconfig, RemoteDBConfig)
    app.run(**RUN_SETTINGS)