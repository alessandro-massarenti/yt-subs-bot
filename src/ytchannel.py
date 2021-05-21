# !/usr/bin/env python

# Yt Api documentation
# https://developers.google.com/youtube/v3/docs

import os

from pyyoutube import Api as ytApi

api_key: str = os.environ['API_KEY']


# Class responsible of describing a yt channel

class YtChannel:
    # Static Attributes
    __yt_api_iface = ytApi(api_key=api_key)

    def __init__(self, channel_id: str):
        # Attributes
        self.__channel_id: str = channel_id
        self.__title: str = ""
        self.__subs_count: int = 0
        self.__views_count: int = 0
        self.__videos_count: int = 0

        # Initialization
        self.update()

    def update(self) -> None:
        # Get the api handle and channel data
        channel = YtChannel.__yt_api_iface.get_channel_info(channel_id=self.__channel_id, parts="statistics,snippet") \
            .items[0].to_dict()

        # Get Statistics info
        statistics = channel['statistics']
        self.__subs_count = statistics['subscriberCount']
        self.__views_count = statistics['viewCount']
        self.__videos_count = statistics['videoCount']

        # Get channel title
        if self.__title is "":
            snippet = channel['snippet']
            self.__title = snippet['title']

    def __repr__(self):
        return [self.title, self.subs, self.views, self.videos]

    # Getters
    @property
    def title(self) -> str:
        return self.__title

    @property
    def subs(self) -> int:
        return self.__subs_count

    @property
    def views(self) -> int:
        return self.__views_count

    @property
    def videos(self) -> int:
        return self.__videos_count
