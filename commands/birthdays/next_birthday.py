from utils import db_handler, send_message
from commands.birthdays.utils import parse_birthday

def next_birthday(update, context):
    chat_id = update.effective_chat.id
    db_connector, birthdays_col = db_handler('birthday')

    query = {"chat_id": chat_id}
    next_birthday = db_connector.search_record(birthdays_col, query)
    if not next_birthday:
        return send_message(context, chat_id, "Please load birthdays first.")
    message = f"Next birthday: {parse_birthday(next_birthday)}"
    return send_message(context, chat_id, message)
