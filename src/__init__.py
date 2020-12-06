from flask import Flask

from .frontend import bp_frontend, bp_gps


def create_app():

    app = Flask(__name__)
    app.register_blueprint(bp_frontend)
    app.register_blueprint(bp_gps, url_prefix='/gps')

    return app
