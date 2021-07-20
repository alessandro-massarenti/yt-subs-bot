# !/usr/bin/env python

# Yt Api documentation
# https://developers.google.com/youtube/v3/docs

import os
from pyyoutube import Api as ytApi
from yt_api.ytchannel import YtChannel

from signaling.event import post_event

api_key: str = os.environ['API_KEY']

#
# If Changed a signal is passed
#

# Yt Channel connected
class YtChannelRemote(YtChannel):
    # Static Attributes
    __yt_api_iface = ytApi(api_key=api_key)

    def __init__(self, channel_id: str):
        # Initialization
        super().__init__(channel_id)
        self.update()

    def update(self):
        """
        Se nota che qualcosa in YT è cambiato lancia un evento relativo al dato cambiato
        :return:
        """

        # Get the api handle and channel data

        channel = YtChannelRemote.__yt_api_iface. \
            get_channel_info(channel_id=self._channel_id, parts="statistics,snippet") \
            .items[0].to_dict()

        # Get Statistics info
        statistics = channel['statistics']
        print(statistics)

        if self.subs != statistics['subscriberCount']:
            self._subs_count = statistics['subscriberCount']
            post_event("subs_changed", self.subs)

        if self.views != statistics['viewCount']:
            self._views_count = statistics['viewCount']
            post_event("views_changed", self.views)

        if self.videos != statistics['videoCount']:
            self._videos_count = statistics['videoCount']
            post_event("videos_changed", self.videos)

        # Get channel title
        if self._title is "":
            snippet = channel['snippet']
            self._title = snippet['title']
