from helpers.mongo_connect import MongoDB
from setup_logger import logger
HOST = 'localhost'

def call_mongo():
    logger.info('Watch out!') 
    return 'mongo'

def get_vision_client_ids():
    # open connection
    cx = MongoDB(HOST)
    # get hiera_vision database
    hiera_vision = cx.getDB('hiera_vision')
    #return client_ids as json
    return cx.get_client_ids(hiera_vision)

def get_evolv_client_ids():
    cx = MongoDB(HOST)
    # get hiera_vision database
    hiera_evolv = cx.getDB('hiera_evolv')
    #return client_ids as json
    logger.info('the function is called')
    return cx.get_client_ids(hiera_evolv)

def get_evolv_backup_client():
    cx = MongoDB(HOST)
    backup_evolv = cx.getDB('backup_hiera_evolv') 
    return backup_evolv

def get_backup_evolv_collection(collection):
    cx = MongoDB(HOST)
    backup_evolv = cx.getDB('backup_hiera_evolv') 
    documents = ''
    for document in backup_evolv[collection].find():
        print(document)
    return documents

def backup_evolv_collection(documents, collection):
    cx = MongoDB(HOST)
    backup_evolv = cx.getDB('backup_hiera_evolv') 
    backup_evolv[collection].insert_many(documents)

def drop_backup_evolv_collection(collection):
    cx = MongoDB(HOST)
    backup_evolv = cx.getDB('backup_hiera_evolv') 
    backup_evolv[collection].drop