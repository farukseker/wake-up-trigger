from config import *
from discord import SyncWebhook


def wake_up_trigger():
    webhook = SyncWebhook.from_url(WEBHOOK_TARGET)
    webhook.send(MESSAGE)


def send_message(message):
    webhook = SyncWebhook.from_url(WEBHOOK_TARGET)
    webhook.send(message)


