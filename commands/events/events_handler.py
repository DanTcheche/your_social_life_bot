from telegram.ext import Updater, CommandHandler

from commands.events.attend_event import attend_event
from commands.events.delete_event import delete_event
from commands.events.events import events
from commands.events.add_event import add_event
from commands.events.miss_event import miss_event


def handle_events(dp):
    dp.add_handler(CommandHandler('events', events))
    dp.add_handler(CommandHandler('add_event', add_event))
    dp.add_handler(CommandHandler('attend_event', attend_event))
    dp.add_handler(CommandHandler('delete_event', delete_event))
    dp.add_handler(CommandHandler('miss_event', miss_event))
