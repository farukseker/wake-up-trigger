import pathlib
import datetime

BASE_DIR = pathlib.Path(__file__).resolve().parent
VENV_DIR = BASE_DIR / 'Scripts'

MESSAGE = f"MainFrame START | {datetime.datetime.now()}"

WEBHOOK_TARGET = ""

