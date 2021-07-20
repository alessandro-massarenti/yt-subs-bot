# !/usr/bin/env python

# Class responsible of handling callbacks

from typing import List

from telegram import Update
from telegram.ext import CallbackContext

from ytchannelremotetelegram import YtChannelRemoteTelegram


class CallBacks:
    # Static Attributes
    __tracked_channels: List[YtChannelRemoteTelegram] = []

    @staticmethod
    def track_channel(update: Update, context: CallbackContext) -> None:
        """
        Aggiunge un canale alla lista dei tracciati
        e aggiunge l'utente alla lista degli interessati al canale
        :param update:
        :param context:
        :return:
        """
        channel_id = context.args[0]
        message_id = update.message.chat_id

        # Se il canale non è mai stato tracciato lo aggiunge alla lista dei tracciati
        if channel_id not in CallBacks.__tracked_channels:
            CallBacks.__tracked_channels.append(YtChannelRemoteTelegram(channel_id))

        for canale in CallBacks.__tracked_channels:
            print(canale)

        context.bot.send_message(message_id, text=channel_id)

    @staticmethod
    def check_channels() -> None:
        names = []
        count = 0
        for channel in CallBacks.__tracked_channels:
            subs = channel.subs
            channel.update()

            print(subs)

            names.append({channel.title: channel.subs})

        print(names)
        return None
