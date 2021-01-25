import telegram


def parse_event(event):
    j_date = event['date'].strftime('%d/%m %H:%M')
    message = f"<b>{event['name'].capitalize()}</b> the {j_date} in {event['place']}."
    if event['participants']:
        message += f" Participants: {event['participants']}."
    return message


def send_message(context, chat_id, message):
    return context.bot.send_message(chat_id=chat_id, text=message, parse_mode=telegram.ParseMode.HTML)
