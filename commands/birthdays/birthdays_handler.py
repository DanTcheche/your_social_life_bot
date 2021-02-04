from telegram.ext import Updater, CommandHandler

from commands.birthdays.add_birthday import add_birthday
from commands.birthdays.birthdays import birthdays


def handle_birthdays(dp):
    dp.add_handler(CommandHandler('birthdays', birthdays))
    dp.add_handler(CommandHandler('add_birthday', add_birthday))
