from db_connector.document_generator import create_participant
from utils import db_handler, send_message


def miss_event(update, context):
    chat_id = update.effective_chat.id
    event_args = context.args
    db_connector, events_col = db_handler('event')
    if len(event_args) != 1:
        message = f"Invalid message, the only parameter should be the event name."
        return send_message(context, chat_id, message)
    event_name = event_args[0]
    query = {"name": event_name.lower(), "chat_id": chat_id}
    event = events_col.find_one(query)
    if not event:
        message = f"Event {event_name} not found."
        return send_message(context, chat_id, message)
    not_assisting_users = event['not_assisting']
    participants = event['participants']

    not_assisting_user = create_participant(update.message.from_user)

    if not_assisting_user['id'] not in [not_assisting_user['id'] for not_assisting_user in not_assisting_users]:
        events_col.update_one(query, {"$push": {'not_assisting': not_assisting_user}}, upsert=False)

    if not_assisting_user['id'] in [participant['id'] for participant in participants]:
        events_col.update_one(query, {"$pull": {'participants': not_assisting_user}}, upsert=False)

    message = f"{not_assisting_user['name']} will not assist {event['name'].capitalize()}"
    return send_message(context, chat_id, message)
