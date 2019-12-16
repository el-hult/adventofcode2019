import logging
from itertools import zip_longest, chain
from queue import Queue
LOG = logging.getLogger(__name__)

def queue_to_list(queue: Queue):
    out = []
    while not queue.empty():
        out.append(queue.get())
    return out


def grouper(iterable, n, fillvalue=None):
    """Collect data into fixed-length chunks or blocks"
    Stolen from https://docs.python.org/3.8/library/itertools.html
    """
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def flatten(list_of_lists):
    """Flatten one level of nesting
    Stolen from https://docs.python.org/3.8/library/itertools.html
    """
    return chain.from_iterable(list_of_lists)