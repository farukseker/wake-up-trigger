import pathlib
import datetime
import os


def ENV(key: str):
    try:
        return os.environ.get(key)
    except:
        return None


BASE_DIR = pathlib.Path(__file__).resolve().parent
VENV_DIR = BASE_DIR / 'Scripts'


MESSAGE = f"MainFrame START | {datetime.datetime.now()}"

WEBHOOK_TARGET = ENV('WEBHOOK_TARGET')


