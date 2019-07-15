from flask import Blueprint

puppet = Blueprint('puppet', __name__)

@puppet.route("/puppet")
def index():
    return 'puppet'