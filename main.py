from telegram.ext import Updater, CommandHandler

from commands.events.events_handler import handle_events
from commands.help import help_command


def main():
    updater = Updater(token='YOUR_TOKEN', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('help', help_command))
    handle_events(dp)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
