from pymongo import MongoClient
import sys
HOST = 'plxlb-mongo02.netsmartlab.lan'

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

    # passi in database object
    def get_client_ids(self, database):
        client_ids = []
        for names in database.collection_names():
            print(names)




    def main():
        print("implement this later")

    if __name__ == "__main__":
        main()