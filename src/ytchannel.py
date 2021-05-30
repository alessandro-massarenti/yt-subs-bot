# !/usr/bin/env python

# Class responsible of describing a yt channel

class YtChannel:
    # Static Attributes
    __yt_api_iface = ytApi(api_key=api_key)

    def __init__(self, channel_id: str):
        # Attributes
        self._channel_id: str = channel_id
        self._title: str = ""
        self._subs_count: int = 0
        self._views_count: int = 0
        self._videos_count: int = 0

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
