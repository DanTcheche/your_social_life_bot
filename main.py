import os
from telegram.ext import Updater, CommandHandler

from commands.birthdays.birthdays_handler import handle_birthdays
from commands.events.events_handler import handle_events
from commands.help import help_command

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']

def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    print("YOUR SOCIAL LIFE BOT started")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('help', help_command))
    handle_events(dp)
    handle_birthdays(dp)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
