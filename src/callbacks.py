# !/usr/bin/env python

# Class responsible of handling callbacks

from typing import List

from telegram import Update
from telegram.ext import CallbackContext

from ytchannel import YtChannel


class CallBacks:
    # Static Attributes
    __tracked_channels: List[YtChannel]

    @staticmethod
    def track_channel(update: Update, context: CallbackContext):
        channel_id = context.args[0]
        CallBacks.__tracked_channels.append(YtChannel(channel_id))

    @staticmethod
    def check_channels():
        diff = []
        for channel in CallBacks.__tracked_channels:
            differences: dict = {}
            views = channel.views
            subs = channel.subs
            videos = channel.videos
            channel.update()

            if views != channel.views:
                differences['views'] = True
            if subs != channel.subs:
                differences['subs'] = True
            if videos != channel.videos:
                differences['videos'] = True

            diff.append(differences)

        return diff
