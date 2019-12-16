from queue import Queue

from computer import get_day5_program, Computer
from util import queue_to_list

if __name__ == "__main__":
    p = get_day5_program()
    q1 = Queue()
    q2 = Queue()
    q1.put(1)
    c = Computer(p,q1,q2)
    c.run_until_stop()
    outputs = queue_to_list(q2)
    print(f"Ans A:{outputs[-1]}")

    q1 = Queue()
    q2 = Queue()
    q1.put(5)
    c = Computer(p, q1, q2)
    c.run_until_stop()
    outputs = queue_to_list(q2)
    print(f"Ans B:{outputs[-1]}")