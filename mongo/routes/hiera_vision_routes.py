from flask import Blueprint
from mongo.mongo_controller import *
from setup_logger import logger

hiera_vision = Blueprint('hiera_vision', __name__)




@hiera_vision.route("/vision/<client_id>/credentials")
def vision_credentials(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    vision_credentials = json.dumps(client_dictionary['vision']['credentials'])
    return vision_credentials

      
@hiera_vision.route("/vision/<client_id>/win_server/timezone/config")
def vision_win_server_timezone_config(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    timezone_config = json.dumps(client_dictionary['vision']['win_server']['timezone']['config'])
    return timezone_config

      
@hiera_vision.route("/vision/<client_id>/environments/TRAIN/web/version")
def vision_environments_train_web_version(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    web_version = json.dumps(client_dictionary['vision']['environments']['TRAIN']['web']['version'])
    return web_version

      
@hiera_vision.route("/vision/<client_id>/environments/UAT/db")
def vision_environments_uat_db(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    UAT_db = json.dumps(client_dictionary['vision']['environments']['UAT']['db'])
    return UAT_db

      
@hiera_vision.route("/vision/<client_id>/_id")
def vision__id(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    vision__id = json.dumps(client_dictionary['vision']['_id'])
    return vision__id

      
@hiera_vision.route("/vision/<client_id>/win_server/timezone")
def vision_win_server_timezone(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    win_server_timezone = json.dumps(client_dictionary['vision']['win_server']['timezone'])
    return win_server_timezone

      
@hiera_vision.route("/vision/<client_id>/environments/UAT/web/app_offline")
def vision_environments_uat_web_app_offline(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    web_app_offline = json.dumps(client_dictionary['vision']['environments']['UAT']['web']['app_offline'])
    return web_app_offline

      
@hiera_vision.route("/vision/<client_id>/environments/LIVE/web/crm_version")
def vision_environments_live_web_crm_version(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    web_crm_version = json.dumps(client_dictionary['vision']['environments']['LIVE']['web']['crm_version'])
    return web_crm_version

      
@hiera_vision.route("/vision/<client_id>/environments/LIVE/web/app_offline")
def vision_environments_live_web_app_offline(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    web_app_offline = json.dumps(client_dictionary['vision']['environments']['LIVE']['web']['app_offline'])
    return web_app_offline

      
@hiera_vision.route("/vision/<client_id>/_etag")
def vision__etag(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    vision__etag = json.dumps(client_dictionary['vision']['_etag'])
    return vision__etag

      
@hiera_vision.route("/vision/<client_id>/environments/UPG/db")
def vision_environments_upg_db(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    UPG_db = json.dumps(client_dictionary['vision']['environments']['UPG']['db'])
    return UPG_db

      
@hiera_vision.route("/vision/<client_id>/client_auth_domain")
def vision_client_auth_domain(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    vision_client_auth_domain = json.dumps(client_dictionary['vision']['client_auth_domain'])
    return vision_client_auth_domain

      
@hiera_vision.route("/vision/<client_id>/credentials/LIVE/vision_user")
def vision_credentials_live_vision_user(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    LIVE_vision_user = json.dumps(client_dictionary['vision']['credentials']['LIVE']['vision_user'])
    return LIVE_vision_user

      
@hiera_vision.route("/vision/<client_id>/environments/TRAIN")
def vision_environments_train(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    environments_TRAIN = json.dumps(client_dictionary['vision']['environments']['TRAIN'])
    return environments_TRAIN

      
@hiera_vision.route("/vision/<client_id>/environments/DEV/db")
def vision_environments_dev_db(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    DEV_db = json.dumps(client_dictionary['vision']['environments']['DEV']['db'])
    return DEV_db

      
@hiera_vision.route("/vision/<client_id>/environments/DEV/web/crm_version")
def vision_environments_dev_web_crm_version(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    web_crm_version = json.dumps(client_dictionary['vision']['environments']['DEV']['web']['crm_version'])
    return web_crm_version

      
@hiera_vision.route("/vision/<client_id>/credentials/LIVE")
def vision_credentials_live(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    credentials_LIVE = json.dumps(client_dictionary['vision']['credentials']['LIVE'])
    return credentials_LIVE

      
@hiera_vision.route("/vision/<client_id>/components/telephony_service_enabled")
def vision_components_telephony_service_enabled(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    components_telephony_service_enabled = json.dumps(client_dictionary['vision']['components']['telephony_service_enabled'])
    return components_telephony_service_enabled

      
@hiera_vision.route("/vision/<client_id>/environments_to_deploy_nonProd")
def vision_environments_to_deploy_nonprod(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    vision_environments_to_deploy_nonProd = json.dumps(client_dictionary['vision']['environments_to_deploy_nonProd'])
    return vision_environments_to_deploy_nonProd

      
@hiera_vision.route("/vision/<client_id>/credentials/TEST")
def vision_credentials_test(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    credentials_TEST = json.dumps(client_dictionary['vision']['credentials']['TEST'])
    return credentials_TEST

      
@hiera_vision.route("/vision/<client_id>/credentials/LIVE/vision_user/username")
def vision_credentials_live_vision_user_username(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    vision_user_username = json.dumps(client_dictionary['vision']['credentials']['LIVE']['vision_user']['username'])
    return vision_user_username

      
@hiera_vision.route("/vision/<client_id>/rodc/ldap_enabled")
def vision_rodc_ldap_enabled(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    rodc_ldap_enabled = json.dumps(client_dictionary['vision']['rodc']['ldap_enabled'])
    return rodc_ldap_enabled

      
@hiera_vision.route("/vision/<client_id>/environments")
def vision_environments(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    vision_environments = json.dumps(client_dictionary['vision']['environments'])
    return vision_environments

      
@hiera_vision.route("/vision/<client_id>/environments/TRAIN/db/version")
def vision_environments_train_db_version(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    db_version = json.dumps(client_dictionary['vision']['environments']['TRAIN']['db']['version'])
    return db_version

      
@hiera_vision.route("/vision/<client_id>/components/crm_enabled")
def vision_components_crm_enabled(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    components_crm_enabled = json.dumps(client_dictionary['vision']['components']['crm_enabled'])
    return components_crm_enabled

      
@hiera_vision.route("/vision/<client_id>/environments/DEV/web/app_offline")
def vision_environments_dev_web_app_offline(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    web_app_offline = json.dumps(client_dictionary['vision']['environments']['DEV']['web']['app_offline'])
    return web_app_offline

      
@hiera_vision.route("/vision/<client_id>/environments/UAT/db/version")
def vision_environments_uat_db_version(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    db_version = json.dumps(client_dictionary['vision']['environments']['UAT']['db']['version'])
    return db_version

      
@hiera_vision.route("/vision/<client_id>/environments/TRAIN/db")
def vision_environments_train_db(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    TRAIN_db = json.dumps(client_dictionary['vision']['environments']['TRAIN']['db'])
    return TRAIN_db

      
@hiera_vision.route("/vision/<client_id>/environments/DEV")
def vision_environments_dev(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    environments_DEV = json.dumps(client_dictionary['vision']['environments']['DEV'])
    return environments_DEV

      
@hiera_vision.route("/vision/<client_id>/environments/UAT/db/restore_db_version")
def vision_environments_uat_db_restore_db_version(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    db_restore_db_version = json.dumps(client_dictionary['vision']['environments']['UAT']['db']['restore_db_version'])
    return db_restore_db_version

      
@hiera_vision.route("/vision/<client_id>/environments/LIVE/db/restore_db_version")
def vision_environments_live_db_restore_db_version(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    db_restore_db_version = json.dumps(client_dictionary['vision']['environments']['LIVE']['db']['restore_db_version'])
    return db_restore_db_version

      
@hiera_vision.route("/vision/<client_id>/components/mobile_view_enabled")
def vision_components_mobile_view_enabled(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    components_mobile_view_enabled = json.dumps(client_dictionary['vision']['components']['mobile_view_enabled'])
    return components_mobile_view_enabled

      
@hiera_vision.route("/vision/<client_id>/environments/TRAIN/web")
def vision_environments_train_web(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    TRAIN_web = json.dumps(client_dictionary['vision']['environments']['TRAIN']['web'])
    return TRAIN_web

      
@hiera_vision.route("/vision/<client_id>/win_server")
def vision_win_server(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    vision_win_server = json.dumps(client_dictionary['vision']['win_server'])
    return vision_win_server

      
@hiera_vision.route("/vision/<client_id>/environments/LIVE")
def vision_environments_live(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    environments_LIVE = json.dumps(client_dictionary['vision']['environments']['LIVE'])
    return environments_LIVE

      
@hiera_vision.route("/vision/<client_id>/environments/TRAIN/db/restore_db_version")
def vision_environments_train_db_restore_db_version(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    db_restore_db_version = json.dumps(client_dictionary['vision']['environments']['TRAIN']['db']['restore_db_version'])
    return db_restore_db_version

      
@hiera_vision.route("/vision/<client_id>/environments/TRAIN/web/crm_version")
def vision_environments_train_web_crm_version(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    web_crm_version = json.dumps(client_dictionary['vision']['environments']['TRAIN']['web']['crm_version'])
    return web_crm_version

      
@hiera_vision.route("/vision/<client_id>/environments/UPG/web/app_offline")
def vision_environments_upg_web_app_offline(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    web_app_offline = json.dumps(client_dictionary['vision']['environments']['UPG']['web']['app_offline'])
    return web_app_offline

      
@hiera_vision.route("/vision/<client_id>/components/interop_service_enabled")
def vision_components_interop_service_enabled(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    components_interop_service_enabled = json.dumps(client_dictionary['vision']['components']['interop_service_enabled'])
    return components_interop_service_enabled

      
@hiera_vision.route("/vision/<client_id>/environments/UPG/db/restore_db_version")
def vision_environments_upg_db_restore_db_version(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    db_restore_db_version = json.dumps(client_dictionary['vision']['environments']['UPG']['db']['restore_db_version'])
    return db_restore_db_version

      
@hiera_vision.route("/vision/<client_id>/components/devero_service_enabled")
def vision_components_devero_service_enabled(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    components_devero_service_enabled = json.dumps(client_dictionary['vision']['components']['devero_service_enabled'])
    return components_devero_service_enabled

      
@hiera_vision.route("/vision/<client_id>/win_server/timezone/config/zone")
def vision_win_server_timezone_config_zone(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    config_zone = json.dumps(client_dictionary['vision']['win_server']['timezone']['config']['zone'])
    return config_zone

      
@hiera_vision.route("/vision/<client_id>/environments/LIVE/web/version")
def vision_environments_live_web_version(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    web_version = json.dumps(client_dictionary['vision']['environments']['LIVE']['web']['version'])
    return web_version

      
@hiera_vision.route("/vision/<client_id>/credentials/TEST/vision_user/password")
def vision_credentials_test_vision_user_password(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    vision_user_password = json.dumps(client_dictionary['vision']['credentials']['TEST']['vision_user']['password'])
    return vision_user_password

      
@hiera_vision.route("/vision/<client_id>/environments/UPG/web/crm_version")
def vision_environments_upg_web_crm_version(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    web_crm_version = json.dumps(client_dictionary['vision']['environments']['UPG']['web']['crm_version'])
    return web_crm_version

      
@hiera_vision.route("/vision/<client_id>/environments/UAT/web/version")
def vision_environments_uat_web_version(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    web_version = json.dumps(client_dictionary['vision']['environments']['UAT']['web']['version'])
    return web_version

      
@hiera_vision.route("/vision/<client_id>/environments/DEV/web")
def vision_environments_dev_web(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    DEV_web = json.dumps(client_dictionary['vision']['environments']['DEV']['web'])
    return DEV_web

      
@hiera_vision.route("/vision/<client_id>/rodc/primary")
def vision_rodc_primary(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    rodc_primary = json.dumps(client_dictionary['vision']['rodc']['primary'])
    return rodc_primary

      
@hiera_vision.route("/vision/<client_id>/credentials/TEST/vision_user/username")
def vision_credentials_test_vision_user_username(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    vision_user_username = json.dumps(client_dictionary['vision']['credentials']['TEST']['vision_user']['username'])
    return vision_user_username

      
@hiera_vision.route("/vision/<client_id>/rodc")
def vision_rodc(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    vision_rodc = json.dumps(client_dictionary['vision']['rodc'])
    return vision_rodc

      
@hiera_vision.route("/vision/<client_id>/environments/DEV/db/version")
def vision_environments_dev_db_version(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    db_version = json.dumps(client_dictionary['vision']['environments']['DEV']['db']['version'])
    return db_version

      
@hiera_vision.route("/vision/<client_id>/environments/UPG/web/version")
def vision_environments_upg_web_version(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    web_version = json.dumps(client_dictionary['vision']['environments']['UPG']['web']['version'])
    return web_version

      
@hiera_vision.route("/vision/<client_id>/rodc/secondary")
def vision_rodc_secondary(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    rodc_secondary = json.dumps(client_dictionary['vision']['rodc']['secondary'])
    return rodc_secondary

      
@hiera_vision.route("/vision/<client_id>/environments/LIVE/db")
def vision_environments_live_db(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    LIVE_db = json.dumps(client_dictionary['vision']['environments']['LIVE']['db'])
    return LIVE_db

      
@hiera_vision.route("/vision/<client_id>/environments/UAT")
def vision_environments_uat(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    environments_UAT = json.dumps(client_dictionary['vision']['environments']['UAT'])
    return environments_UAT

      
@hiera_vision.route("/vision/<client_id>/environments/UAT/web/crm_version")
def vision_environments_uat_web_crm_version(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    web_crm_version = json.dumps(client_dictionary['vision']['environments']['UAT']['web']['crm_version'])
    return web_crm_version

      
@hiera_vision.route("/vision/<client_id>/environments/LIVE/db/version")
def vision_environments_live_db_version(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    db_version = json.dumps(client_dictionary['vision']['environments']['LIVE']['db']['version'])
    return db_version

      
@hiera_vision.route("/vision/<client_id>/components")
def vision_components(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    vision_components = json.dumps(client_dictionary['vision']['components'])
    return vision_components

      
@hiera_vision.route("/vision/<client_id>/environments/UAT/web")
def vision_environments_uat_web(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    UAT_web = json.dumps(client_dictionary['vision']['environments']['UAT']['web'])
    return UAT_web

      
@hiera_vision.route("/vision/<client_id>/environments/UPG")
def vision_environments_upg(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    environments_UPG = json.dumps(client_dictionary['vision']['environments']['UPG'])
    return environments_UPG

      
@hiera_vision.route("/vision/<client_id>/environments/UPG/db/version")
def vision_environments_upg_db_version(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    db_version = json.dumps(client_dictionary['vision']['environments']['UPG']['db']['version'])
    return db_version

      
@hiera_vision.route("/vision/<client_id>/environments/TRAIN/web/app_offline")
def vision_environments_train_web_app_offline(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    web_app_offline = json.dumps(client_dictionary['vision']['environments']['TRAIN']['web']['app_offline'])
    return web_app_offline

      
@hiera_vision.route("/vision/<client_id>/environments/UPG/web")
def vision_environments_upg_web(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    UPG_web = json.dumps(client_dictionary['vision']['environments']['UPG']['web'])
    return UPG_web

      
@hiera_vision.route("/vision/<client_id>/environments/DEV/db/restore_db_version")
def vision_environments_dev_db_restore_db_version(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    db_restore_db_version = json.dumps(client_dictionary['vision']['environments']['DEV']['db']['restore_db_version'])
    return db_restore_db_version

      
@hiera_vision.route("/vision/<client_id>")
def vision(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    vision = json.dumps(client_dictionary['vision'])
    return vision

      
@hiera_vision.route("/vision/<client_id>/environments/LIVE/web")
def vision_environments_live_web(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    LIVE_web = json.dumps(client_dictionary['vision']['environments']['LIVE']['web'])
    return LIVE_web

      
@hiera_vision.route("/vision/<client_id>/credentials/TEST/vision_user")
def vision_credentials_test_vision_user(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    TEST_vision_user = json.dumps(client_dictionary['vision']['credentials']['TEST']['vision_user'])
    return TEST_vision_user

      
@hiera_vision.route("/vision/<client_id>/credentials/LIVE/vision_user/password")
def vision_credentials_live_vision_user_password(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    vision_user_password = json.dumps(client_dictionary['vision']['credentials']['LIVE']['vision_user']['password'])
    return vision_user_password

      
@hiera_vision.route("/vision/<client_id>/environments/DEV/web/version")
def vision_environments_dev_web_version(client_id):
    logger.info('get_hiera_vision_client_collection_version called')
    cx = MongoDB('localhost')
    id_string = str(client_id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    web_version = json.dumps(client_dictionary['vision']['environments']['DEV']['web']['version'])
    return web_version

      
