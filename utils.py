import datetime
from db_connector.mongo_connector import MongoConnector


def db_handler():
    db_connector = MongoConnector()
    db_connector.create_database('your_social_life_bot')
    col = db_connector.create_collection('event')
    return db_connector, col


def parse_date(date_str):
    format_str = '%d/%m/%Y %H:%M'  # The format
    date = datetime.datetime.strptime(date_str, format_str)
    return date
