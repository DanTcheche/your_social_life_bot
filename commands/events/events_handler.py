from telegram.ext import Updater, CommandHandler

from commands.events.assist_event import assist_event
from commands.events.delete_event import delete_event
from commands.events.events import events
from commands.events.add_event import add_event


def handle_events(dp):
    dp.add_handler(CommandHandler('events', events))
    dp.add_handler(CommandHandler('add_event', add_event))
    dp.add_handler(CommandHandler('assist_event', assist_event))
    dp.add_handler(CommandHandler('delete_event', delete_event))
