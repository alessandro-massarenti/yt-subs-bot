# !/usr/bin/env python

from yt_api.ytchannelremote import YtChannelRemote


class YtChannelRemoteTelegram(YtChannelRemote):
    def __init__(self, channel_id: str):
        super().__init__(channel_id)
        self.subscribers = list()

    def add_subscriber(self, message_id):
        """ Aggiunge una conversazione alla lista delle conversazioni interessate a questo canale yt"""
        self.subscribers.append(message_id)

    def remove_subscriber(self, message_id):
        """ Aggiunge una conversazione alla lista delle conversazioni interessate a questo canale yt"""
        self.subscribers.remove(message_id)
