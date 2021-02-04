def parse_birthday(birthday):
    date = birthday['date'].strftime('%d/%m')
    message = f"<b>{birthday['name'].capitalize()}</b>: {date}."
    return message
