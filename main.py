from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from birthdays.birthdays import birthdays
from birthdays.next_birthday import next_birthday
from events.events import events
from events.new_event import next_event


def main():
    updater = Updater(token='YOUR_TOKEN', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('birthdays', birthdays))
    dp.add_handler(CommandHandler('next_birthday', next_birthday))
    dp.add_handler(CommandHandler('events', events))
    dp.add_handler(CommandHandler('next_event', next_event))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
