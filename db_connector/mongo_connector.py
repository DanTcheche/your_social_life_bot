from pymongo import MongoClient


class MongoConnector:

    def __init__(self):
        self.client = MongoClient('mongodb+srv://<username>:<password>@cluster0.r5gkt.mongodb.net/'
                                  '<cluster>?retryWrites=true&w=majority')
        self.database = None

    def create_database(self, db_name):
        self.database = self.client[f'{db_name}']

    def create_collection(self, collection_name):
        return self.database[collection_name]

    def insert_record(self, collection, data):
        collection.insert(data)
