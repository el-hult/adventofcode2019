from typing import Literal, List, Callable

ops = {
    1: 'add',
    2: 'multiply',
    99: 'stop'
}

Program = List[int]
State = List[int]


class Computer():
    def __init__(self, state: State):
        self.state = state.copy()
        self.initial_state = state.copy()
        self.current_pos = 0

    @property
    def has_stopped(self):
        return ops[self.state[self.current_pos]] == 'stop'

    def step(self):
        op = ops[self.state[self.current_pos]]
        if op == 'add':
            a = self.state[self.state[self.current_pos + 1]]
            b = self.state[self.state[self.current_pos + 2]]
            c = self.state[self.current_pos + 3]
            self.state[c] = a + b
            self.current_pos += 4
        elif op == 'multiply':
            a = self.state[self.state[self.current_pos + 1]]
            b = self.state[self.state[self.current_pos + 2]]
            c = self.state[self.current_pos + 3]
            self.state[c] = a * b
            self.current_pos += 4
        elif op == 'stop':
            pass
        else:
            raise ValueError("Not valid opcode")

    def run_until_stop(self):
        while not self.has_stopped:
            self.step()


def compute_computer_output(program: Program, noun: int, verb: int) -> int:
    initial_state = program.copy()
    initial_state[1] = noun
    initial_state[2] = verb
    cmp = Computer(initial_state)
    cmp.run_until_stop()
    return cmp.state[0]
