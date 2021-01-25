from utils import db_handler, parse_date, send_message


def add_event(update, context):
    chat_id = update.effective_chat.id
    event_args = context.args
    db_connector, events_col = db_handler()

    if len(event_args) < 4:
        message = f"Invalid message, the format should be exactly: name(One word) dd/mm/yyyy hh:mm place."
        return send_message(context, chat_id, message)

    try:
        parsed_date = parse_date(f'{event_args[1]} {event_args[2]}')
    except:
        message = f"Invalid date format in message, the format should be exactly: name(One word)" \
                  f" dd/mm/yyyy hh:mm place."
        return send_message(context, chat_id, message)

    event_document = {
        "chat_id": chat_id,
        "name": event_args[0].lower(),
        "date": parsed_date,
        "place": ' '.join(event_args[3:]),
        "creator": update.message.from_user.name,
        "participants": ""
    }

    db_connector.insert_record(events_col, event_document)

    message = f"Event {event_document['name']} created for {event_document['date']}."

    return send_message(context, chat_id, message)

