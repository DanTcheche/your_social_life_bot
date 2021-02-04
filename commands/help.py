from utils import send_message


def help_command(update, context):
    chat_id = update.effective_chat.id
    message = f"Commands: \n" \
              f"/help - A little help.\n" \
              f"/birthdays - List all birthdays.\n" \
              f"/add_birthday name(one word) dd/mm/yyyy - Add a birthday.\n" \
              f"/events - List all events.\n" \
              f"/add_event name(one word) dd/mm/yyyy hh:mm place - Add an event.\n" \
              f"/delete_event event_name- Deletes an event.\n" \
              f"/attend_event event_name - Adds you as a participant.\n" \
              f"/miss_event event_name - You are not assisting the event.\n"

    return send_message(context, chat_id, message)
