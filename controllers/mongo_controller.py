from helpers.mongo_connect import MongoDB
from setup_logger import logger, error_logger
HOST = 'localhost'
import json


def call_mongo():
    logger.info('Watch out!') 
    return 'mongo'


def get_vision_client_ids():
    # open connection
    logger.info('get_vision_client_ids called')
    cx = MongoDB(HOST)
    # get hiera_vision database
    hiera_vision = cx.getDB('hiera_vision')
    #return client_ids as json
    return cx.get_client_ids(hiera_vision)


def get_vision_client_collection(id):
    # open connection
    logger.info('get_vision_client_ids called')
    id_string = str(id)
    cx = MongoDB(HOST)
    # get hiera_vision database
    hiera_vision = cx.getDB('hiera_vision')
    # return client_ids as json
    return cx.get_client_collection(hiera_vision, id_string)

def get_vision_client_web_version(id):
    logger.info('get_vision_client_web_version called')
    cx = MongoDB(HOST)
    id_string = str(id)
    hiera_vision = cx.getDB('hiera_vision')
    client_document = cx.get_client_collection(hiera_vision, id_string)
    client_dictionary = json.loads(client_document)
    web_version = client_dictionary['vision']['environments']['LIVE']['web']['version']
    return web_version


def get_evolv_client_ids():
    logger.info('get_evolv_client_ids called')
    cx = MongoDB(HOST)
    # get hiera_vision database
    hiera_evolv = cx.getDB('hiera_evolv')
    #return client_ids as json

    return cx.get_client_ids(hiera_evolv)


def get_evolv_backup_client():
    logger.info('get_evolv_backup_client called')
    cx = MongoDB(HOST)
    backup_evolv = cx.getDB('backup_hiera_evolv') 
    return backup_evolv


def get_backup_evolv_collection(collection):
    logger.info('get_backup_evolv_collection called')
    cx = MongoDB(HOST)
    backup_evolv = cx.getDB('backup_hiera_evolv') 
    documents = ''
    for document in backup_evolv[collection].find():
        print(document)
    return documents


def backup_evolv_collection(documents, collection):
    logger.info('backup_evolv_collection called')
    cx = MongoDB(HOST)
    backup_evolv = cx.getDB('backup_hiera_evolv') 
    backup_evolv[collection].insert_many(documents)


def drop_backup_evolv_collection(collection):
    logger.warning('drop_backup_evolv_collection called')
    cx = MongoDB(HOST)
    backup_evolv = cx.getDB('backup_hiera_evolv') 
    backup_evolv[collection].drop