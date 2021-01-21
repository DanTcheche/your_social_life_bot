import datetime
import telegram

from commands.events.utils import parse_event
from utils import db_handler


def events(update, context):
    chat_id = update.effective_chat.id
    db, events_col = db_handler()

    query = {"date": {"$gte": datetime.datetime.today()}, "chat_id": chat_id}
    events_query = __get_events_from_db(db, query)
    message = list_events(events_query)
    return context.bot.send_message(chat_id=chat_id, text=message,
                                    parse_mode=telegram.ParseMode.HTML)


def list_events(events_query):
    message = "Next events: \n"
    events_list = []
    for event in events_query:
        events_list.append(parse_event(event))
    message += "\n".join(events_list)
    return message


def __get_events_from_db(db_connector, query):
    return db_connector.search_records(query)
