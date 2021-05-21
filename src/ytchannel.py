# !/usr/bin/env python

# https://developers.google.com/youtube/v3/docs

from pyyoutube import Api as ytApi
import os

api_key: str = os.environ['API_KEY']


class YtChannel:
    # def __init__(self, channel_name):
    #     self.__channel_name = channel_name
    #     self.__data = []
    #     self.__update()
    #
    # def __update(self):
    #     self.__data_s = urllib.request.urlopen(
    #         "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" +
    #         self.__channel_name +
    #         "&key=" +
    #         api_key).read()
    #
    # @property
    # def subs(self):
    #     return json.loads(self.__data_s)["items"][0]["statistics"]["subscriberCount"]
    #
    # @property
    # def views(self):
    #     return json.loads(self.__data_s)["items"][0]["statistics"]["viewCount"]

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
        self.__update()

    def __update(self):
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

    # Getters
    @property
    def title(self):
        return self.__title

    @property
    def subs(self):
        return self.__subs_count

    @property
    def views(self):
        return self.__views_count

    @property
    def videos(self):
        return self.__videos_count
