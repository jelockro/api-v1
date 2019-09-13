from pymongo import *
import sys, json
from bson import json_util

from setup_logger import logger
class MongoDB:
    
    def __init__(self, HOST):
        self.client = self.connect(HOST)

    def connect(self, HOST):
        try:
            # Python 3.x
            from urllib.parse import quote_plus
        except ImportError:
            # Python 2.x
            from urllib import quote_plus
        uri = "mongodb://%s:%s@%s" % (
            quote_plus('NetsmartAdmin'), quote_plus('Netsmart99'), HOST)
        connection = MongoClient(uri, 443)
        logger.info('Connection!') 
        if connection is None:
            # logfile.debug('Unable to connect to mongo database: %s', uri)
            logger.warning('Unable to connect to mongo database: %s', uri)
            return
        else:           
            # logfile.debug('successful connection to mongo database: %s ', uri)
            # logconsole.debug('successful connection to mongo database: %s ', uri)
            logger.info('Connection Works!') 
            return connection
        
    # creates database object
    def getDB(self, database_name):
        return self.client[database_name]

    # pass in database object
    def get_client_ids(self, database):
        client_ids = []
        for name in database.collection_names():
            if name[0] == '_':
                continue
            else:
                client_ids.append(name)
        client_ids.sort()
        client_ids = '{"client_ids": %s}' %(json.dumps(client_ids))
        return client_ids

    def get_client_collection(self, database, client_id):
        client_collection = database[client_id]
        #pprint.pprint(client_collection.find_one())
        data = client_collection.find_one()

        return json.dumps(data, default=json_util.default)

    # def update_client_collection(self, database,  ):

def main():
    print("implement this later")

if __name__ == "__main__":
    main()