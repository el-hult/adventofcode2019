from queue import Queue

import nose.tools

from util import queue_to_list


def test_1():
    q1 = Queue()
    q1.put(1)
    q1.put(3)
    q1.put("hej")
    l = queue_to_list(q1)
    nose.tools.assert_equals([1,3,"hej"],l)
