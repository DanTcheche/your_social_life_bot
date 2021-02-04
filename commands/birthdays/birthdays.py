from utils import db_handler, send_message
from commands.birthdays.utils import parse_birthday


def birthdays(update, context):
    chat_id = update.effective_chat.id
    db_connector, birthdays_col = db_handler('birthday')

    query = {"chat_id": chat_id}
    birthdays_query = db_connector.search_records(birthdays_col, query)
    message = list_birthdays(birthdays_query)
    return send_message(context, chat_id, message)


def list_birthdays(birthdays_query):
    message = "Birthdays: \n"
    birthdays_list = []
    for birthday in birthdays_query:
        birthdays_list.append(parse_birthday(birthday))
    message += "\n".join(birthdays_list)
    return message
