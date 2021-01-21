def parse_event(event):
    j_date = event['date'].strftime('%d/%m %H:%M')
    return f"<b>{event['name']}</b> el {j_date} en {event['place']}. Participantes: {event['participants']}."
