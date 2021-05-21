# !/usr/bin/env python

# Class responsible of handling callbacks

from typing import List

from telegram import Update
from telegram.ext import CallbackContext

from ytchannel import YtChannel


class CallBacks:
    # Static Attributes
    __tracked_channels = List[YtChannel]

    @staticmethod
    def set_timer(update: Update, context: CallbackContext):
        print(update.message)
        print(CallBacks.__tracked_channels)
        print()
