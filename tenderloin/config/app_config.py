import os


class ProductionAppconfig:
    ENV = "production"
    SECRET_KEY = os.getenv("SECRET_KEY_BASE")
