from db_connector.document_generator import create_event
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

    event_document = create_event(chat_id, event_args, parsed_date, update.message.from_user)

    db_connector.insert_record(events_col, event_document)

    message = f"Event {event_document['name']} created for {event_document['date'].strftime('%d/%m %H:%M')}."

    return send_message(context, chat_id, message)

