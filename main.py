import os
from config import *
import sys
from datetime import datetime



def simple_log(message: str):
    with open('log.txt', 'a+', encoding='utf-8') as log_file:
        log_file.write(f'{datetime.now()} -' + message + '\n')


try:
    import trigger
    trigger.wake_up_trigger()
    simple_log(f"WORK")
except Exception as e:
    simple_log(str(e))
finally:
    sys.exit(0)

