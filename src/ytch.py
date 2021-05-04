# !/usr/bin/env python

import urllib.request
import json
import config


class YtCh:

    def __init__(self, channel_name):
        self.__data = urllib.request.urlopen(
            "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + channel_name + "&api_key=" + config.api_key).read()

    @property
    def subs(self):
        return json.loads(self.__data)["items"][0]["statistics"]["subscriberCount"]
