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

    def search_records(self, collection, query):
        return collection.find(query)

    def delete_record(self, collection, query):
        deleted = collection.delete_one(query)
        return deleted.deleted_count > 0
