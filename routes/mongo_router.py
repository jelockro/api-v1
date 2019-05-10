from flask import Blueprint
from controllers.mongo_controller import call_mongo, get_evolv_client_ids, get_vision_client_ids
mongo = Blueprint('mongo', __name__)

@mongo.route("/mongo")
def index():
    return call_mongo()

@mongo.route("/mongo/client_ids/vision")
def vision_clients():
    return get_vision_client_ids()

@mongo.route("/mongo/client_ids/evolv")
def evolv_clients():
    return get_evolv_client_ids()