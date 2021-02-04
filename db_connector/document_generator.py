def create_participant(user):
    return {
        'id': user.id,
        'name': user.name
    }


def create_event(chat_id, event_args, parsed_date, user):
    return {
        "chat_id": chat_id,
        "name": event_args[0].lower(),
        "date": parsed_date,
        "place": ' '.join(event_args[3:]),
        "creator": {
            'id': user.id,
            'name': user.name
        },
        "participants": [],
        "not_assisting": []
    }
