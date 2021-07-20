# !/usr/bin/env python

# Class responsible of describing a yt channel

class YtChannel:
    _title: str = ""
    _subs_count: int = 0
    _views_count: int = 0
    _videos_count: int = 0

    def __init__(self, channel_id: str):
        # Attributes
        self._channel_id: str = channel_id

    # Getters
    @property
    def title(self) -> str:
        return self._title

    @property
    def subs(self) -> int:
        return self._subs_count

    @property
    def views(self) -> int:
        return self._views_count

    @property
    def videos(self) -> int:
        return self._videos_count
