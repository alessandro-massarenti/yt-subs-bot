from signaling.event import subscribe


def handle_views_changed_event(views):
    """
    Handles the event of the view counter changed
    :param views:
    :return:
    """
    print("sono cambiate le viewvs " + str(views))


def handle_subs_changed_event(subs):
    print("subs", subs)


def setup_printing_event_handlers():
    subscribe("views_changed", handle_views_changed_event)
    subscribe("subs_changed", handle_subs_changed_event)
