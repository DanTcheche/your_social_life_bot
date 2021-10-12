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
        difference_in_days = get_difference_between_dates_in_days(birthday['date'], now)
        if difference_in_days < distance:
            distance = difference_in_days
            nearest_birthday = birthday
    if not nearest_birthday:
        return send_message(context, chat_id, "Please load birthdays first.")
    message = f"Next birthday is in {difference_in_days} day(s): {parse_birthday(nearest_birthday)}"
    return send_message(context, chat_id, message)

def get_difference_between_dates_in_days(original_date, date_to_compare):
    delta1 = datetime(date_to_compare.year, original_date.month, original_date.day)
    delta2 = datetime(date_to_compare.year+1, original_date.month, original_date.day)
    return ((delta1 if delta1 > date_to_compare else delta2) - date_to_compare).days

