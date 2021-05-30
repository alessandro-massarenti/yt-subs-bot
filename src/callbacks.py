# !/usr/bin/env python

# Class responsible of handling callbacks

from typing import List

from telegram import Update
from telegram.ext import CallbackContext

from ytchannelremote import YtChannelRemote


class CallBacks:
    # Static Attributes
    __tracked_channels: List[YtChannelRemote] = []
    __Users_channels: List = []

    @staticmethod
    def track_channel(update: Update, context: CallbackContext) -> None:
        channel_id = context.args[0]
        message_id = update.message.chat_id
        context.bot.send_message(message_id, text=channel_id)
        CallBacks.__tracked_channels.append(YtChannelRemote(channel_id))

    @staticmethod
    def check_channels() -> None:
        diff = []
        for channel in CallBacks.__tracked_channels:
            differences: dict = {}
            views = channel.views
            subs = channel.subs
            videos = channel.videos
            channel.update()

        print("checked")
        return None
