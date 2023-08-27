import os
from config import *
import sys
from datetime import datetime



def simple_log(message: str):
    with open('log.txt', 'a+', encoding='utf-8') as log_file:
        log_file.write(f'{datetime.now()} - ' + message + '\n')


try:
    import trigger
    if len(sys.argv) > 1:
        if sys.argv[1] == 'idle':
            trigger.send_message(f'MainFrame system went to IDLE load | {datetime.now()}')
        if sys.argv[1] == 'locked':
            trigger.send_message(f'MainFrame system went to LOCKED | {datetime.now()}')
        if sys.argv[1] == 'unlocked':
            trigger.send_message(f'MainFrame system went to UNLOCKED | {datetime.now()}')
    else:
        trigger.wake_up_trigger()
    simple_log(f"WORK")
    simple_log(str(sys.argv))
except Exception as e:
    simple_log('ERR: '+ str(e))
finally:
    sys.exit(0)

