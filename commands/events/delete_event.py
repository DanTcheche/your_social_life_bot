from utils import db_handler, send_message


def delete_event(update, context):
    chat_id = update.effective_chat.id
    event_args = context.args
    db_connector, events_col = db_handler('event')
    message = None
    if len(event_args) != 1:
        message = f"Invalid message, the only parameter should be the event name."
        return send_message(context, chat_id, message)

    event_name = event_args[0]

    query = {'name': event_name.lower(), "chat_id": chat_id}
    event = db_connector.search_record(events_col, query)
    if not event:
        message = f"Event {event_name} not found."
    if not message and event['creator']['id'] == update.message.from_user.id:
        deleted = db_connector.delete_record(events_col, query)
        if deleted == 0:
            message = f"There was an error deleting the event."
        else:
            message = f"Event {event_name} deleted."
    if not message:
        message = "Only the creator of the event can delete it."
    return send_message(context, chat_id, message)
