from db_connector.document_generator import create_birthday
from utils import db_handler, parse_date, send_message


def add_birthday(update, context):
    chat_id = update.effective_chat.id
    birthday_args = context.args
    db_connector, birthdays_col = db_handler('birthday')

    if len(birthday_args) != 2:
        message = f"Invalid message, the format should be exactly: name(One word) dd/mm/yyyy."
        return send_message(context, chat_id, message)

    try:
        parsed_date = parse_date(f'{birthday_args[1]}')
    except:
        message = f"Invalid date format in message, the format should be exactly: name(One word) dd/mm/yyyy."
        return send_message(context, chat_id, message)

    birthday_document = create_birthday(chat_id, birthday_args, parsed_date)

    db_connector.insert_record(birthdays_col, birthday_document)

    message = f"Birthday for {birthday_document['name'].capitalize()} " \
              f"added: {birthday_document['date'].strftime('%d/%m')}."

    return send_message(context, chat_id, message)

