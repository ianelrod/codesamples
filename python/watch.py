import sys
import time
import logging
from re import *
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

path = "/flag"
count = -56

logging.basicConfig(level=logging.INFO, format='%(message)s')

event_handler = LoggingEventHandler()
observer = Observer()
observer.schedule(event_handler, path)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
