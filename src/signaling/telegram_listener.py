from signaling.event import subscribe


def handle_views_changed_event(views):
    # send a welcome email
    print("sono cambiate le viewvs ecc ecc " + str(views))


def setup_telegram_event_handlers():
    subscribe("views_changed", handle_views_changed_event)
