from helpers.mongo_connect import MongoDB, HOST


def call_mongo():
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
    return cx.get_client_ids(hiera_evolv)