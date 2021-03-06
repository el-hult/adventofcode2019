from queue import Queue

from util import queue_to_list, thermal_environment_supervision_terminal, Computer

if __name__ == "__main__":
    p = thermal_environment_supervision_terminal()
    q1 = Queue()
    q2 = Queue()
    q1.put(1)
    c = Computer(p, q1, q2)
    c.run_until_stop()
    outputs = queue_to_list(q2)
    print(f"Ans A:{outputs[-2]}")  # 11049715

    q1 = Queue()
    q2 = Queue()
    q1.put(5)
    c = Computer(p, q1, q2)
    c.run_until_stop()
    outputs = queue_to_list(q2)
    print(f"Ans B:{outputs[-2]}")  # 2140710
