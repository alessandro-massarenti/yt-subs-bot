import urllib.request
import json

name = "Channel name"
key = "GoogleAPIKey"
totale = 0

# !/usr/bin/env python
# pylint: disable=C0116
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to send timed Telegram messages.
This Bot uses the Updater class to handle the bot and the JobQueue to send
timed messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Alarm Bot example, sends a message after a set time.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def alarm(context: CallbackContext) -> None:
    """Send the alarm message."""
    global totale
    job = context.job

    data = urllib.request.urlopen(
        "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + name + "&key=" + key).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]

    print('Controllato')

    if int(subs) != totale:
        totale = int(subs)
        context.bot.send_message(job.context, text=subs + " iscritti su MountainTime")
        print('message sent')


def set_timer(update: Update, context: CallbackContext) -> None:
    """Add a job to the queue."""
    chat_id = update.message.chat_id

    context.job_queue.run_repeating(alarm, 30, context=chat_id)


def main() -> None:
    """Run bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("BotToken")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", set_timer))

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
