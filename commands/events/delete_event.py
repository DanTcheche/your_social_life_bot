from utils import db_handler, send_message


def delete_event(update, context):
    chat_id = update.effective_chat.id
    event_args = context.args
    db_connector, events_col = db_handler()
    if len(event_args) > 1:
        message = f"Invalid message, the only parameter should be the event name."
        return send_message(context, chat_id, message)

    event_name = event_args[0]

    query = {'name': event_name.lower(), "chat_id": chat_id}
    deleted = db_connector.delete_record(events_col, query)
    if deleted == 0:
        message = f"Event {event_name} not found."
        return send_message(context, chat_id, message)
    message = f"Event {event_name} deleted."
    return send_message(context, chat_id, message)
