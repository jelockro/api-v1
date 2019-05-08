from flask import Blueprint
from controllers.mongo_controller import call_mongo
mongo = Blueprint('mongo', __name__)

@mongo.route("/mongo")
def index():
    return call_mongo()
