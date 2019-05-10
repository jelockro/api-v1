from pymongo import MongoClient
from celery.utils.log import get_task_logger
import sys, json

HOST = 'plxlb-mongo02.netsmartlab.lan'
logger = get_task_logger

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
        return MongoClient(uri, 27017) 
        
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



    def main():
        print("implement this later")

    if __name__ == "__main__":
        main()