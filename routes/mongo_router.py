from flask import Blueprint
from controllers.mongo_controller import *
from setup_logger import logger
mongo = Blueprint('mongo', __name__)


@mongo.route("/mongo")
def index():
    logger.info('route called')
    return call_mongo()


@mongo.route("/mongo/client_ids/vision")
def vision_clients():
    return get_vision_client_ids()


@mongo.route("/mongo/client_ids/evolv")
def evolv_clients():
    logger.info('evolv client route called')
    return get_evolv_client_ids()


@mongo.route("/mongo/backup/evolv/<collection>")
def backup_evolv_clients(collection):
    return get_backup_evolv_collection(collection)


@mongo.route("/mongo/drop/evolv/<collection>")
def drop_backup_evolv_clients(collection):
    return drop_backup_evolv_collection(collection)