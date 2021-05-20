# !/usr/bin/env python
# pylint: disable=C0116


from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from typing import List

import config
import os

from ytchannel import YtChannel


bot_key: str = os.environ['BOT_KEY']

mt = YtChannel(config.name, api_key)


def main() -> None:
    # Print "Starting up"
    print("Spinning up the bot ...")

    tracked_channels = List[YtChannel]

    # Create the Updater and pass it your bots token.
    updater = Updater(bot_key)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("track", set_timer))

    print("Polling started")
    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
