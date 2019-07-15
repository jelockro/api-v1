from flask import Blueprint
from mongo.mongo_controller import *
from setup_logger import logger

hiera_evolv = Blueprint('hiera_evolv', __name__)




@hiera_evolv.route("/evolv/<client_id>/credentials/LIVE/app_pool_user/password")
def evolv_credentials_live_app_pool_user_password(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    app_pool_user_password = json.dumps(client_dictionary['evolv']['credentials']['LIVE']['app_pool_user']['password'])
    return app_pool_user_password

      
@hiera_evolv.route("/evolv/<client_id>/environments/DEV")
def evolv_environments_dev(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    environments_DEV = json.dumps(client_dictionary['evolv']['environments']['DEV'])
    return environments_DEV

      
@hiera_evolv.route("/evolv/<client_id>/environments/DEV/web/applications/xb")
def evolv_environments_dev_web_applications_xb(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    applications_xb = json.dumps(client_dictionary['evolv']['environments']['DEV']['web']['applications']['xb'])
    return applications_xb

      
@hiera_evolv.route("/evolv/<client_id>/environments/TRAIN")
def evolv_environments_train(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    environments_TRAIN = json.dumps(client_dictionary['evolv']['environments']['TRAIN'])
    return environments_TRAIN

      
@hiera_evolv.route("/evolv/<client_id>/environments/TRAIN/web/app_offline")
def evolv_environments_train_web_app_offline(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    web_app_offline = json.dumps(client_dictionary['evolv']['environments']['TRAIN']['web']['app_offline'])
    return web_app_offline

      
@hiera_evolv.route("/evolv/<client_id>/environments/LIVE")
def evolv_environments_live(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    environments_LIVE = json.dumps(client_dictionary['evolv']['environments']['LIVE'])
    return environments_LIVE

      
@hiera_evolv.route("/evolv/<client_id>/credentials/TEST/evolv_user/password")
def evolv_credentials_test_evolv_user_password(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    evolv_user_password = json.dumps(client_dictionary['evolv']['credentials']['TEST']['evolv_user']['password'])
    return evolv_user_password

      
@hiera_evolv.route("/evolv/<client_id>/environments/LIVE/db")
def evolv_environments_live_db(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    LIVE_db = json.dumps(client_dictionary['evolv']['environments']['LIVE']['db'])
    return LIVE_db

      
@hiera_evolv.route("/evolv/<client_id>/credentials/LIVE/logi_user")
def evolv_credentials_live_logi_user(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    LIVE_logi_user = json.dumps(client_dictionary['evolv']['credentials']['LIVE']['logi_user'])
    return LIVE_logi_user

      
@hiera_evolv.route("/evolv/<client_id>/environments/TRAIN/web/applications")
def evolv_environments_train_web_applications(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    web_applications = json.dumps(client_dictionary['evolv']['environments']['TRAIN']['web']['applications'])
    return web_applications

      
@hiera_evolv.route("/evolv/<client_id>/environments/TRAIN/web/applications/classic")
def evolv_environments_train_web_applications_classic(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    applications_classic = json.dumps(client_dictionary['evolv']['environments']['TRAIN']['web']['applications']['classic'])
    return applications_classic

      
@hiera_evolv.route("/evolv/<client_id>/environments/TRAIN/web/applications/xb")
def evolv_environments_train_web_applications_xb(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    applications_xb = json.dumps(client_dictionary['evolv']['environments']['TRAIN']['web']['applications']['xb'])
    return applications_xb

      
@hiera_evolv.route("/evolv/<client_id>/environments/LIVE/db/version")
def evolv_environments_live_db_version(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    db_version = json.dumps(client_dictionary['evolv']['environments']['LIVE']['db']['version'])
    return db_version

      
@hiera_evolv.route("/evolv/<client_id>/environments/TRAIN/db/version")
def evolv_environments_train_db_version(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    db_version = json.dumps(client_dictionary['evolv']['environments']['TRAIN']['db']['version'])
    return db_version

      
@hiera_evolv.route("/evolv/<client_id>/environments/DEV/db")
def evolv_environments_dev_db(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    DEV_db = json.dumps(client_dictionary['evolv']['environments']['DEV']['db'])
    return DEV_db

      
@hiera_evolv.route("/evolv/<client_id>/environments/DEV/web/applications/logi")
def evolv_environments_dev_web_applications_logi(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    applications_logi = json.dumps(client_dictionary['evolv']['environments']['DEV']['web']['applications']['logi'])
    return applications_logi

      
@hiera_evolv.route("/evolv/<client_id>/credentials/TEST/app_pool_user/password")
def evolv_credentials_test_app_pool_user_password(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    app_pool_user_password = json.dumps(client_dictionary['evolv']['credentials']['TEST']['app_pool_user']['password'])
    return app_pool_user_password

      
@hiera_evolv.route("/evolv/<client_id>/environments/TRAIN/web")
def evolv_environments_train_web(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    TRAIN_web = json.dumps(client_dictionary['evolv']['environments']['TRAIN']['web'])
    return TRAIN_web

      
@hiera_evolv.route("/evolv/<client_id>/environments/LIVE/web/applications/logi")
def evolv_environments_live_web_applications_logi(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    applications_logi = json.dumps(client_dictionary['evolv']['environments']['LIVE']['web']['applications']['logi'])
    return applications_logi

      
@hiera_evolv.route("/evolv/<client_id>/credentials/LIVE")
def evolv_credentials_live(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    credentials_LIVE = json.dumps(client_dictionary['evolv']['credentials']['LIVE'])
    return credentials_LIVE

      
@hiera_evolv.route("/evolv/<client_id>/environments/LIVE/web/applications/xb")
def evolv_environments_live_web_applications_xb(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    applications_xb = json.dumps(client_dictionary['evolv']['environments']['LIVE']['web']['applications']['xb'])
    return applications_xb

      
@hiera_evolv.route("/evolv/<client_id>/credentials/TEST/logi_user/password")
def evolv_credentials_test_logi_user_password(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    logi_user_password = json.dumps(client_dictionary['evolv']['credentials']['TEST']['logi_user']['password'])
    return logi_user_password

      
@hiera_evolv.route("/evolv/<client_id>/_etag")
def evolv__etag(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    evolv__etag = json.dumps(client_dictionary['evolv']['_etag'])
    return evolv__etag

      
@hiera_evolv.route("/evolv/<client_id>/environments/LIVE/web/applications/classic")
def evolv_environments_live_web_applications_classic(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    applications_classic = json.dumps(client_dictionary['evolv']['environments']['LIVE']['web']['applications']['classic'])
    return applications_classic

      
@hiera_evolv.route("/evolv/<client_id>/environments/DEV/web/applications/mobile")
def evolv_environments_dev_web_applications_mobile(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    applications_mobile = json.dumps(client_dictionary['evolv']['environments']['DEV']['web']['applications']['mobile'])
    return applications_mobile

      
@hiera_evolv.route("/evolv/<client_id>/win_server")
def evolv_win_server(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    evolv_win_server = json.dumps(client_dictionary['evolv']['win_server'])
    return evolv_win_server

      
@hiera_evolv.route("/evolv/<client_id>/environments/LIVE/web")
def evolv_environments_live_web(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    LIVE_web = json.dumps(client_dictionary['evolv']['environments']['LIVE']['web'])
    return LIVE_web

      
@hiera_evolv.route("/evolv/<client_id>/credentials/TEST/evolv_user/username")
def evolv_credentials_test_evolv_user_username(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    evolv_user_username = json.dumps(client_dictionary['evolv']['credentials']['TEST']['evolv_user']['username'])
    return evolv_user_username

      
@hiera_evolv.route("/evolv/<client_id>/environments/LIVE/web/version")
def evolv_environments_live_web_version(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    web_version = json.dumps(client_dictionary['evolv']['environments']['LIVE']['web']['version'])
    return web_version

      
@hiera_evolv.route("/evolv/<client_id>/environments/TRAIN/web/applications/mobile")
def evolv_environments_train_web_applications_mobile(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    applications_mobile = json.dumps(client_dictionary['evolv']['environments']['TRAIN']['web']['applications']['mobile'])
    return applications_mobile

      
@hiera_evolv.route("/evolv/<client_id>/credentials/TEST/app_pool_user")
def evolv_credentials_test_app_pool_user(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    TEST_app_pool_user = json.dumps(client_dictionary['evolv']['credentials']['TEST']['app_pool_user'])
    return TEST_app_pool_user

      
@hiera_evolv.route("/evolv/<client_id>/environments/TRAIN/web/version")
def evolv_environments_train_web_version(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    web_version = json.dumps(client_dictionary['evolv']['environments']['TRAIN']['web']['version'])
    return web_version

      
@hiera_evolv.route("/evolv/<client_id>/environments/TRAIN/web/applications/logi")
def evolv_environments_train_web_applications_logi(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    applications_logi = json.dumps(client_dictionary['evolv']['environments']['TRAIN']['web']['applications']['logi'])
    return applications_logi

      
@hiera_evolv.route("/evolv/<client_id>/credentials/TEST/evolv_user")
def evolv_credentials_test_evolv_user(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    TEST_evolv_user = json.dumps(client_dictionary['evolv']['credentials']['TEST']['evolv_user'])
    return TEST_evolv_user

      
@hiera_evolv.route("/evolv/<client_id>/credentials/LIVE/evolv_user")
def evolv_credentials_live_evolv_user(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    LIVE_evolv_user = json.dumps(client_dictionary['evolv']['credentials']['LIVE']['evolv_user'])
    return LIVE_evolv_user

      
@hiera_evolv.route("/evolv/<client_id>/environments/LIVE/web/applications")
def evolv_environments_live_web_applications(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    web_applications = json.dumps(client_dictionary['evolv']['environments']['LIVE']['web']['applications'])
    return web_applications

      
@hiera_evolv.route("/evolv/<client_id>/environments/DEV/db/type")
def evolv_environments_dev_db_type(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    db_type = json.dumps(client_dictionary['evolv']['environments']['DEV']['db']['type'])
    return db_type

      
@hiera_evolv.route("/evolv/<client_id>/win_server/timezone")
def evolv_win_server_timezone(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    win_server_timezone = json.dumps(client_dictionary['evolv']['win_server']['timezone'])
    return win_server_timezone

      
@hiera_evolv.route("/evolv/<client_id>/credentials/LIVE/logi_user/username")
def evolv_credentials_live_logi_user_username(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    logi_user_username = json.dumps(client_dictionary['evolv']['credentials']['LIVE']['logi_user']['username'])
    return logi_user_username

      
@hiera_evolv.route("/evolv/<client_id>/credentials/LIVE/app_pool_user")
def evolv_credentials_live_app_pool_user(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    LIVE_app_pool_user = json.dumps(client_dictionary['evolv']['credentials']['LIVE']['app_pool_user'])
    return LIVE_app_pool_user

      
@hiera_evolv.route("/evolv/<client_id>/_id")
def evolv__id(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    evolv__id = json.dumps(client_dictionary['evolv']['_id'])
    return evolv__id

      
@hiera_evolv.route("/evolv/<client_id>")
def evolv(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    evolv = json.dumps(client_dictionary['evolv'])
    return evolv

      
@hiera_evolv.route("/evolv/<client_id>/environments/DEV/web/applications/classic")
def evolv_environments_dev_web_applications_classic(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    applications_classic = json.dumps(client_dictionary['evolv']['environments']['DEV']['web']['applications']['classic'])
    return applications_classic

      
@hiera_evolv.route("/evolv/<client_id>/win_server/timezone/config/zone")
def evolv_win_server_timezone_config_zone(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    config_zone = json.dumps(client_dictionary['evolv']['win_server']['timezone']['config']['zone'])
    return config_zone

      
@hiera_evolv.route("/evolv/<client_id>/environments/LIVE/web/applications/mobile")
def evolv_environments_live_web_applications_mobile(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    applications_mobile = json.dumps(client_dictionary['evolv']['environments']['LIVE']['web']['applications']['mobile'])
    return applications_mobile

      
@hiera_evolv.route("/evolv/<client_id>/environments/DEV/web/version")
def evolv_environments_dev_web_version(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    web_version = json.dumps(client_dictionary['evolv']['environments']['DEV']['web']['version'])
    return web_version

      
@hiera_evolv.route("/evolv/<client_id>/environments")
def evolv_environments(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    evolv_environments = json.dumps(client_dictionary['evolv']['environments'])
    return evolv_environments

      
@hiera_evolv.route("/evolv/<client_id>/environments/LIVE/db/type")
def evolv_environments_live_db_type(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    db_type = json.dumps(client_dictionary['evolv']['environments']['LIVE']['db']['type'])
    return db_type

      
@hiera_evolv.route("/evolv/<client_id>/credentials/LIVE/evolv_user/password")
def evolv_credentials_live_evolv_user_password(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    evolv_user_password = json.dumps(client_dictionary['evolv']['credentials']['LIVE']['evolv_user']['password'])
    return evolv_user_password

      
@hiera_evolv.route("/evolv/<client_id>/environments/TRAIN/db/type")
def evolv_environments_train_db_type(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    db_type = json.dumps(client_dictionary['evolv']['environments']['TRAIN']['db']['type'])
    return db_type

      
@hiera_evolv.route("/evolv/<client_id>/environments/TRAIN/db")
def evolv_environments_train_db(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    TRAIN_db = json.dumps(client_dictionary['evolv']['environments']['TRAIN']['db'])
    return TRAIN_db

      
@hiera_evolv.route("/evolv/<client_id>/win_server/timezone/config")
def evolv_win_server_timezone_config(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    timezone_config = json.dumps(client_dictionary['evolv']['win_server']['timezone']['config'])
    return timezone_config

      
@hiera_evolv.route("/evolv/<client_id>/environments/DEV/web")
def evolv_environments_dev_web(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    DEV_web = json.dumps(client_dictionary['evolv']['environments']['DEV']['web'])
    return DEV_web

      
@hiera_evolv.route("/evolv/<client_id>/environments/LIVE/web/app_offline")
def evolv_environments_live_web_app_offline(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    web_app_offline = json.dumps(client_dictionary['evolv']['environments']['LIVE']['web']['app_offline'])
    return web_app_offline

      
@hiera_evolv.route("/evolv/<client_id>/credentials")
def evolv_credentials(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    evolv_credentials = json.dumps(client_dictionary['evolv']['credentials'])
    return evolv_credentials

      
@hiera_evolv.route("/evolv/<client_id>/environments/DEV/db/version")
def evolv_environments_dev_db_version(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    db_version = json.dumps(client_dictionary['evolv']['environments']['DEV']['db']['version'])
    return db_version

      
@hiera_evolv.route("/evolv/<client_id>/credentials/TEST")
def evolv_credentials_test(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    credentials_TEST = json.dumps(client_dictionary['evolv']['credentials']['TEST'])
    return credentials_TEST

      
@hiera_evolv.route("/evolv/<client_id>/credentials/LIVE/evolv_user/username")
def evolv_credentials_live_evolv_user_username(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    evolv_user_username = json.dumps(client_dictionary['evolv']['credentials']['LIVE']['evolv_user']['username'])
    return evolv_user_username

      
@hiera_evolv.route("/evolv/<client_id>/environments/DEV/web/app_offline")
def evolv_environments_dev_web_app_offline(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    web_app_offline = json.dumps(client_dictionary['evolv']['environments']['DEV']['web']['app_offline'])
    return web_app_offline

      
@hiera_evolv.route("/evolv/<client_id>/credentials/TEST/logi_user")
def evolv_credentials_test_logi_user(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    TEST_logi_user = json.dumps(client_dictionary['evolv']['credentials']['TEST']['logi_user'])
    return TEST_logi_user

      
@hiera_evolv.route("/evolv/<client_id>/environments_to_deploy_nonProd")
def evolv_environments_to_deploy_nonprod(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    evolv_environments_to_deploy_nonProd = json.dumps(client_dictionary['evolv']['environments_to_deploy_nonProd'])
    return evolv_environments_to_deploy_nonProd

      
@hiera_evolv.route("/evolv/<client_id>/environments/DEV/web/applications")
def evolv_environments_dev_web_applications(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    web_applications = json.dumps(client_dictionary['evolv']['environments']['DEV']['web']['applications'])
    return web_applications

      
@hiera_evolv.route("/evolv/<client_id>/credentials/LIVE/logi_user/password")
def evolv_credentials_live_logi_user_password(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    logi_user_password = json.dumps(client_dictionary['evolv']['credentials']['LIVE']['logi_user']['password'])
    return logi_user_password

      
@hiera_evolv.route("/evolv/<client_id>/credentials/TEST/logi_user/username")
def evolv_credentials_test_logi_user_username(client_id):
    logger.info('get_hiera_evolv_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_evolv = cx.getDB('hiera_evolv')
    client_document = cx.get_client_collection(hiera_evolv, id_string)
    client_dictionary = json.loads(client_document)
    logi_user_username = json.dumps(client_dictionary['evolv']['credentials']['TEST']['logi_user']['username'])
    return logi_user_username

      
