from utils import db_handler, send_message
from datetime import datetime
from commands.birthdays.utils import parse_birthday

def next_birthday(update, context):
    chat_id = update.effective_chat.id
    db_connector, birthdays_col = db_handler('birthday')

    query = {"chat_id": chat_id}
    next_birthday = db_connector.search_records(birthdays_col, query)

    distance = 365
    nearest_birthday = None
    now = datetime.now()
    for birthday in next_birthday:
        c = calculate_dates(birthday['date'], now)
        if c < distance:
            distance = c
            nearest_birthday = birthday
    if not nearest_birthday:
        return send_message(context, chat_id, "Please load birthdays first.")
    message = f"Next birthday is in {c} day(s): {parse_birthday(nearest_birthday)}"
    return send_message(context, chat_id, message)

def calculate_dates(original_date, now):
    delta1 = datetime(now.year, original_date.month, original_date.day)
    delta2 = datetime(now.year+1, original_date.month, original_date.day)
    return ((delta1 if delta1 > now else delta2) - now).days

