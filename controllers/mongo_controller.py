from helpers.mongo_connect import MongoDB, HOST

def call_mongo():
    return 'mongo'

def vision_client_ids():
    # open connection
    cx = MongoDB(HOST)
    # get hiera_vision database
    hiera_vision = cx.getDB('hiera_vision')
    #return client_ids as json
    return cx.get_client_ids(hiera_vision)