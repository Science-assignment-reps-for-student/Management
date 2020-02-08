from flask import Flask

def register_extension(flask_app: Flask):
    from app import extension
    extension.db.init_app(flask_app)
    extension.jwt.init_app(flask_app)
    extension.cors.init_app(flask_app)


def register_hook(flask_app: Flask):
    pass


def register_blueprint(flask_app: Flask):
    from app.views.apis.info.personal import assignment
    flask_app.register_blueprint(assignment.api.blueprint)

    from app.views.apis.info.team import team_assignment, experiment
    flask_app.register_blueprint(experiment.api.blueprint)
    flask_app.register_blueprint(team_assignment.api.blueprint)

    from app.views.test import test
    flask_app.register_blueprint(test.api.blueprint)


def create_app(*config_cls) -> Flask:
    flask_app = Flask(__name__)

    for config in config_cls:
        flask_app.config.from_object(config)

    register_extension(flask_app)
    register_hook(flask_app)
    register_blueprint(flask_app)

    return flask_app