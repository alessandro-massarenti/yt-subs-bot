# !/usr/bin/env python
# pylint: disable=C0116

import os
from telegram.ext import Updater, CommandHandler
from threading import Timer

import time

from callbacks import CallBacks

bot_key: str = os.environ['BOT_KEY']


class RepeatTimer(Timer):
    def run(self) -> None:
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)
        print("done")


def main() -> None:
    # Print "Starting up"
    print("Spinning up the bot ...")

    # Create the Updater and pass it your bots token.
    updater = Updater(bot_key)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("track", CallBacks.track_channel))

    timer = RepeatTimer(2, CallBacks.check_channels)
    timer.start()

    # Start the Bot
    updater.start_polling()
    print("Polling started")

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()
    timer.cancel()


if __name__ == '__main__':
    main()
