from flask import Blueprint, render_template

bp_frontend = Blueprint('frontend', __name__)


@bp_frontend.route('/')
def index():
    return render_template('home.html')

@bp_frontend.route('/gps')
def gps():
    return render_template('gps.html')