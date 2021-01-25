from db_connector.document_generator import create_participant
from utils import db_handler, send_message


def attend_event(update, context):
    chat_id = update.effective_chat.id
    event_args = context.args
    db_connector, events_col = db_handler()
    if len(event_args) != 1:
        message = f"Invalid message, the only parameter should be the event name."
        return send_message(context, chat_id, message)
    event_name = event_args[0]
    query = {"name": event_name.lower(), "chat_id": chat_id}
    event = events_col.find_one(query)
    if not event:
        message = f"Event {event_name} not found."
        return send_message(context, chat_id, message)
    participants = event['participants']

    participant = create_participant(update.message.from_user)

    if participant['id'] not in [participant['id'] for participant in participants]:
        events_col.update_one(query, {"$push": {'participants': participant}}, upsert=False)

    message = f"{participant['name']} will assist {event['name'].capitalize()}"
    return send_message(context, chat_id, message)
