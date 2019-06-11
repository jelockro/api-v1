from flask import Blueprint
from controllers.mongo_controller import *
from setup_logger import logger, error_logger
mongo = Blueprint('mongo', __name__)


@mongo.route("/mongo")
def index():
    logger.info('route called')
    return call_mongo()


@mongo.route("/mongo/client_ids/vision")
def vision_clients():
    return get_vision_client_ids()


@mongo.route("/mongo/vision/<int:client_id>")
def vision_client(client_id):
    logger.info('/mongo/vision/<client_id> route called')
    return get_vision_client_collection(client_id)


@mongo.route("/mongo/vision/<int:client_id>/webapp")
def vision_client_web(client_id):
    logger.info('/mongo/vision/<client_id>/webdapp route called')
    return get_vision_client_web_document(client_id)



@mongo.route("/mongo/vision/<int:client_id>/webapp/version")
def vision_client_web_version(client_id):
    logger.info('/mongo/vision/<int:client_id>/web/version route called')
    return get_vision_client_web_version(client_id)


@mongo.route("/mongo/vision/<int:client_id>/webapp/crm_version")
def vision_client_crm_version(client_id):
    logger.info('/mongo/vision/<int:client_id>/web/crm_version route called')
    return get_vision_client_crm_version(client_id)


@mongo.route("/mongo/client_ids/evolv")
def evolv_clients():
    return get_evolv_client_ids()


@mongo.route("/mongo/backup/evolv/<collection>")
def backup_evolv_clients(collection):
    return get_backup_evolv_collection(collection)


@mongo.route("/mongo/drop/evolv/<collection>")
def drop_backup_evolv_clients(collection):
    return drop_backup_evolv_collection(collection)

