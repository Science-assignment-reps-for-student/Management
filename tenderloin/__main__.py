from tenderloin.app import create_app
from tenderloin.config.app_config import ProductionAppconfig
from tenderloin.config.db_config import RemoteDBConfig
from tenderloin.const.run_setting import RUN_SETTINGS

if __name__ == "__main__":
    app = create_app(ProductionAppconfig, RemoteDBConfig)

    from waitress import serve

    serve(app, **RUN_SETTINGS)
