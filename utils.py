from db_connector.mongo_connector import MongoConnector


def db_handler():
    db_connector = MongoConnector()
    db = db_connector.create_database('your_social_life_bot')
    col = db_connector.create_collection('event')
    return db, col
