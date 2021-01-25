def parse_event(event):
    j_date = event['date'].strftime('%d/%m %H:%M')
    message = f"<b>{event['name'].capitalize()}</b> the {j_date} in {event['place']}. \n"
    participants = [participant['name'] for participant in event['participants']]
    not_assisting = [participant['name'] for participant in event['not_assisting']]
    if event['participants']:
        message += f"Participants: {', '.join(participants)}. \n"
    if event['not_assisting']:
        message += f"Not assisting: {', '.join(not_assisting)}."
    return message
