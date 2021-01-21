from telegram.ext import Updater, CommandHandler

from commands.events.events_handler import handle_events


def main():
    updater = Updater(token='YOUR_TOKEN', use_context=True)
    dp = updater.dispatcher
    handle_events(dp)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
