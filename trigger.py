from config import *
import datetime
from discord import SyncWebhook


def wake_up_trigger():
    webhook = SyncWebhook.from_url(WEBHOOK_TARGET)
    webhook.send(f"MainFrame START | {datetime.datetime.now()}")



