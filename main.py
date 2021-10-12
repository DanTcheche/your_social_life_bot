from telegram.ext import Updater, CommandHandler

from commands.birthdays.birthdays_handler import handle_birthdays
from commands.events.events_handler import handle_events
from commands.help import help_command


def main():
    token = ""
    if (len(token) == 0):
        print("BOT_TOKEN must be provided!")
        return
    updater = Updater(token=token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler(['help', 'start'], help_command))
    handle_events(dp)
    handle_birthdays(dp)
    updater.start_polling()
    print("Bot is Online!")
    updater.idle()


if __name__ == '__main__':
    main()
