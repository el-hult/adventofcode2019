from typing import Literal, List, Callable

from computer import Computer, Program


def compute_computer_output(program: Program, noun: int, verb: int) -> int:
    initial_state = program.copy()
    initial_state[1] = noun
    initial_state[2] = verb
    cmp = Computer(initial_state)
    cmp.run_until_stop()
    return cmp.state[0]
