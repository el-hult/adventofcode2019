from typing import List, Union

ops_and_nargs = {
    1: ('add',3),
    2: ('multiply',3),
    3: ('input',1),
    4: ('output',1),
    99: ('stop',0),
}
"""Opcodes and the number of arguments they take"""

Program = List[int]
State = List[int]


def get_test_program() -> Program:
    """Retrieves the Thermal Environment Supervision Terminal program"""
    with open("inputs/day5.txt") as f:
        s = f.readline()
    p = [int(i) for i in s.split(",")]
    return p


class Computer():
    def __init__(self, input_: Union[State, Program]):
        self.state = input_.copy()
        self.instr_pntr = 0
        """Instruction pointer"""

    @property
    def has_stopped(self):
        opcode = self.state[self.instr_pntr]
        op,_ = ops_and_nargs[opcode % 100]
        return op == 'stop'

    def step(self):
        opcode = self.state[self.instr_pntr]
        op,nargs = ops_and_nargs[opcode%100]

        # Determine parameter modes
        modes =[int(i) for i in str(opcode)[-3::-1]]
        modes = modes+[0]*(nargs-len(modes) )
        if op in ['add','multiply']:
            modes[2] = 1
        elif op in ['input']:
            modes[0] = 1

        # Parse arguments
        args = []
        for i, parameter_mode in enumerate(modes):
            if parameter_mode == 1:
                args.append(self.state[self.instr_pntr + i + 1])
            elif parameter_mode == 0:
                args.append(self.state[self.state[self.instr_pntr + i + 1]])
            else:
                raise ValueError("Invalid parameter mode")

        if op == 'add':
            a,b,c = args
            self.state[c] = a + b
            self.instr_pntr += (nargs+1)
        elif op == 'multiply':
            a,b,c = args
            self.state[c] = a * b
            self.instr_pntr += (nargs+1)
        elif op == 'input':
            a = args[0]
            in_val = int(input("Input: "))
            self.state[a] = in_val
            self.instr_pntr += (nargs+1)
        elif op == 'output':
            a = args[0]
            print(a)
            self.instr_pntr += (nargs+1)
        elif op == 'stop':
            pass
        else:
            raise ValueError("Not valid opcode")

    def run_until_stop(self):
        while not self.has_stopped:
            self.step()
