from telegram import Update
from telegram.ext import CallbackContext
from event import subscribe


def handle_sub_counter_updated_event(update: Update, context: CallbackContext, testo):
    # manda il messaggio con gli iscritti
    context.bot.send_message(update.message.chat_id, text=testo)


def setup_message_event_handlers():
    subscribe("sub_counter_updated", handle_sub_counter_updated_event)
