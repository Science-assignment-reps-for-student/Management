import os

class TestAppConfig:
    ENV = "develop"
    SECRET_KEY = "a79ac8d4b7b27d613ce5b420380e992e7487616d3073db1e86be3a527a1399ee26c43ad303274af40441487d0c1583372ce17cc7c38ebcd7e0751c87ba8cdfae"
    # TEST SECRET_KEY

class ProductionAppconfig:
    ENV = "production"
    SECRET_KEY = os.getenv("SECRET_KEY_BASE")