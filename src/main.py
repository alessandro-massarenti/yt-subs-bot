# !/usr/bin/env python

from yt_api.ytchannelremote import YtChannelRemote
from signaling.telegram_listener import setup_telegram_event_handlers
from signaling.printing_listener import setup_printing_event_handlers
from yt_api.updater import Updater

import signal
import time


class GracefulKiller:
    kill_now = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, *args):
        self.kill_now = True


def main() -> None:
    mountaintime = YtChannelRemote('UCC84ggiZXVyXtlNgerfPVcg')

    # setup event handlers
    setup_telegram_event_handlers()
    setup_printing_event_handlers()

    yt_updater = Updater(4, mountaintime.update)
    yt_updater.start()

    killer = GracefulKiller()
    while not killer.kill_now:
        time.sleep(1)
        print("keeping the program alive")

    yt_updater.cancel()


if __name__ == '__main__':
    main()
