import datetime
from commands.events.utils import parse_event
from utils import db_handler, send_message


def events(update, context):
    chat_id = update.effective_chat.id
    db_connector, events_col = db_handler()

    query = {"date": {"$gte": datetime.datetime.today()}, "chat_id": chat_id}
    events_query = db_connector.search_records(events_col, query)
    message = list_events(events_query)
    return send_message(context, chat_id, message)


def list_events(events_query):
    message = "Next events: \n"
    events_list = []
    for event in events_query:
        events_list.append(parse_event(event))
    message += "\n".join(events_list)
    return message
