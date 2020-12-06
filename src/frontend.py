from flask import Blueprint, render_template

bp_frontend = Blueprint('frontend', __name__, static_folder='gps-map/assets')
bp_gps = Blueprint('gps', __name__, template_folder='gps-map', static_folder='gps-map/assets')


@bp_frontend.route('/')
def index():
    return render_template('index.html')

@bp_gps.route('/')
def gps():
    return render_template('gps.html')
