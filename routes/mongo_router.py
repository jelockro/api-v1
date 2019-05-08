from flask import Blueprint
from controllers.mongo_controller import call_mongo, vision_client_ids
mongo = Blueprint('mongo', __name__)

@mongo.route("/mongo")
def index():
    return call_mongo()

@mongo.route("/mongo/client_ids/vision")
def vision_clients():
    return vision_client_ids()
