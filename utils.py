import datetime
import telegram
from db_connector.mongo_connector import MongoConnector


def db_handler(collection_name):
    db_connector = MongoConnector()
    db_connector.create_database('your_social_life_bot')
    col = db_connector.create_collection(collection_name)
    return db_connector, col


def parse_date_time(date_str):
    format_str = '%d/%m/%Y %H:%M'  # The format
    date = datetime.datetime.strptime(date_str, format_str)
    return date


def parse_date(date_str):
    format_str = '%d/%m/%Y'  # The format
    date = datetime.datetime.strptime(date_str, format_str)
    return date


def send_message(context, chat_id, message):
    return context.bot.send_message(chat_id=chat_id, text=message, parse_mode=telegram.ParseMode.HTML)

