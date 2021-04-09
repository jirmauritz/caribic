from flask import Flask

from .frontend import bp_frontend


def create_app():

    app = Flask(__name__)
    app.register_blueprint(bp_frontend)

    return app
