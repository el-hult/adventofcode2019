import logging
from queue import Queue
LOG = logging.getLogger(__name__)

def queue_to_list(queue: Queue):
    out = []
    while not queue.empty():
        out.append(queue.get())
    return out
