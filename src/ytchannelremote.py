# !/usr/bin/env python

# Yt Api documentation
# https://developers.google.com/youtube/v3/docs

import os
from typing import List

from pyyoutube import Api as ytApi

from ytchannel import YtChannel

api_key: str = os.environ['API_KEY']


#
# Update Policy
# Write-trough
#
# Updater check every 30 seconds
# If Changed a signal is passed
#

# Yt Channel connected
class YtChannelRemote(YtChannel):
    # Static Attributes
    __yt_api_iface = ytApi(api_key=api_key)

    def __init__(self, channel_id: str):
        # Initialization
        super().__init__(channel_id)
        self._previous: List[bool] = [False, False, False]
        self.update()

    def update(self):
        # Get the api handle and channel data
        channel = YtChannelRemote.__yt_api_iface. \
            get_channel_info(channel_id=self._channel_id, parts="statistics,snippet") \
            .items[0].to_dict()

        self.__reset()
        # Get Statistics info
        statistics = channel['statistics']

        if self.subs != statistics['subscriberCount']:
            self._subs_count = statistics['subscriberCount']
            self._previous[0] = True

        if self.views != statistics['viewCount']:
            self._subs_count = statistics['viewCount']
            self._previous[1] = True

        if self.videos != statistics['videoCount']:
            self._subs_count = statistics['videoCount']
            self._previous[2] = True

        # Get channel title
        if self._title is "":
            snippet = channel['snippet']
            self._title = snippet['title']

        # ritorna i dati cambiati
        #
        return self._previous

    def __reset(self) -> None:
        for val in self._previous:
            val = False
