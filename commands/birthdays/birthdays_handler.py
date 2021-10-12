from telegram.ext import Updater, CommandHandler

from commands.birthdays.add_birthday import add_birthday
from commands.birthdays.birthdays import birthdays
from commands.birthdays.next_birthday import next_birthday


def handle_birthdays(dp):
    dp.add_handler(CommandHandler('birthdays', birthdays))
    dp.add_handler(CommandHandler('add_birthday', add_birthday))
    dp.add_handler(CommandHandler('next_birthday', next_birthday))
