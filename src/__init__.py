from flask import Flask

from .frontend import frontend_blueprint


def create_app():

    app = Flask(__name__)
    app.register_blueprint(frontend_blueprint)

    return app
