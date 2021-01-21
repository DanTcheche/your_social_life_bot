from telegram.ext import Updater, CommandHandler

from commands.birthdays.birthdays import birthdays
from commands.birthdays.next_birthday import next_birthday
from db_connector.mongo_connector import MongoConnector
from commands.events.events import events
from commands.events.new_event import next_event


def main():
    updater = Updater(token='YOUR_TOKEN', use_context=True)
    dp = updater.dispatcher
    db_connector = MongoConnector()
    db_connector.create_database('your_social_life_bot')
    dp.add_handler(CommandHandler('birthdays', birthdays))
    dp.add_handler(CommandHandler('next_birthday', next_birthday))
    dp.add_handler(CommandHandler('events', events))
    dp.add_handler(CommandHandler('next_event', next_event))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
