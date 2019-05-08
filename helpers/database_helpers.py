from pymongo import MongoClient
import from mongo_connect import MongoDB
import sys
MONGO_URI = 'mongodb://plxlb-mongo02.netsmartlab.lan'

class MongoDB:
 
    def __init__(self, Mongo_URI):
        self.client = self.connect()

    def connect(Mong_URI):
        return MongoClient(Mongo_URI, 27017)    
    
    def getDB(self, database_name):
        return self.client[database_name]

    def main():
        print("implement this later")

    if __name__ == "__main__":
        main()