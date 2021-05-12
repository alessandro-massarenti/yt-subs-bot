# !/usr/bin/env python
# pylint: disable=C0116


from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from typing import List

import config
import os

from ytchannel import YtChannel

api_key: str = os.environ['API_KEY']
bot_key: str = os.environ['BOT_KEY']
totale = 0

mt = YtChannel(config.name, api_key)


def alarm(context: CallbackContext) -> None:
    """Send the alarm message."""
    global totale
    job = context.job

    subs = mt.subs
    print('Controllato')

    if int(subs) != totale:
        totale = int(subs)
        context.bot.send_message(job.context, text=subs + " iscritti su MountainTime")
        print('message sent')


def set_timer(update: Update, context: CallbackContext) -> None:
    """Add a job to the queue."""
    chat_id = update.message.chat_id
    channel_name: str = context.args[0]

    context.job_queue.run_repeating(alarm, 30, context=chat_id)


def main() -> None:
    # Print "Starting up"
    print("Starting up")

    tracked_channels = List[YtChannel]

    # Create the Updater and pass it your bots token.
    updater = Updater(bot_key)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("track", set_timer))

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
