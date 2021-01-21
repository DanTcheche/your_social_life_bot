from telegram.ext import Updater, CommandHandler

from commands.events.events import events
from commands.events.new_event import new_event


def handle_events(dp):
    dp.add_handler(CommandHandler('events', events))
    dp.add_handler(CommandHandler('add_event', new_event))
