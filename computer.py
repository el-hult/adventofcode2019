from collections import defaultdict
from enum import IntEnum
from queue import Queue
from typing import List, Union

from util import queue_from_iterable, queue_to_list, read_file


class ParameterMode(IntEnum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


pos = ParameterMode.POSITION
imm = ParameterMode.IMMEDIATE
rel = ParameterMode.RELATIVE
ops_metadata = {
    1: ('add', 3, (pos, pos, imm)),
    2: ('multiply', 3, (pos, pos, imm)),
    3: ('input', 1, (imm,)),
    4: ('output', 1, (pos,)),
    5: ('jump-if-true', 2, (pos, pos)),
    6: ('jump-if-false', 2, (pos,pos)),
    7: ('less-than', 3, (pos, pos, imm)),
    8: ('equals', 3, (pos, pos, imm)),
    9: ('adjust-relative-base', 1, (pos,)),
    99: ('stop', 0, ()),
}
"""Opcodes and the number of arguments they take"""

Program = List[int]
State = List[int]

BOOST_TESTMODE = 1


def get_program(fname: str) -> Program:
    s=read_file(fname)
    p = [int(i) for i in s.split(",")]
    return p


def thermal_environment_supervision_terminal() -> Program:
    """Retrieves the Thermal Environment Supervision Terminal program, aka TEST"""
    return get_program('inputs/day5.txt')


def basic_operation_of_system_test() -> Program:
    """the BOOST program"""
    return get_program('inputs/day9.txt')


class Computer():
    def __init__(self, initial_state: Union[State, Program], input_queue: Queue, output_queue: Queue):
        self._state = defaultdict(int)
        for pos, val in enumerate(initial_state):
            self._state[pos] = val
        self.instr_pntr = 0
        self.relative_base = 0
        """Instruction pointer"""
        self.input_queue = input_queue
        self.output_queue = output_queue

    @property
    def has_stopped(self):
        opcode = self._state[self.instr_pntr]
        op, _,_ = ops_metadata[opcode % 100]
        return op == 'stop'

    @property
    def state(self):
        max_adress = max(self._state.keys())
        min_adress = min(self._state.keys())
        assert min_adress == 0
        outlist = [0] * (max_adress + 1)
        for k, v in self._state.items():
            outlist[k] = v
        return outlist

    def step(self):
        opcode = self._state[self.instr_pntr]
        op, nargs, modes = ops_metadata[opcode % 100]

        # Determine parameter modes
        modes = list(modes) #makes a copy of the tuple....
        provided_modes = [ParameterMode(int(i)) for i in str(opcode)[-3::-1]]
        modes[:len(provided_modes)] = provided_modes

        # Parse arguments
        params = []
        for parameter_idx, parameter_mode in enumerate(modes):
            raw_param_value = self._state[self.instr_pntr + parameter_idx + 1]
            if parameter_mode == ParameterMode.IMMEDIATE:
                params.append(raw_param_value)
            elif parameter_mode == ParameterMode.POSITION:
                params.append(self._state[raw_param_value])
            elif parameter_mode == ParameterMode.RELATIVE:
                params.append(self._state[self.relative_base + raw_param_value])
            else:
                raise ValueError("Invalid parameter mode")

        # Fix argument parsing for the case with outputs to relative position...
        if op in ['add','multiply','input','less-than','equals'] and modes[-1] == ParameterMode.RELATIVE:
            params[-1] = self.relative_base + raw_param_value


        if op == 'add':
            a, b, c = params
            self._state[c] = a + b
            self.instr_pntr += (nargs + 1)
        elif op == 'multiply':
            a, b, c = params
            self._state[c] = a * b
            self.instr_pntr += (nargs + 1)
        elif op == 'input':
            a = params[0]
            in_val = int(self.input_queue.get())
            self._state[a] = in_val
            self.instr_pntr += (nargs + 1)
        elif op == 'jump-if-true':
            if params[0] != 0:
                self.instr_pntr = params[1]
            else:
                self.instr_pntr += (nargs + 1)
        elif op == 'jump-if-false':
            if params[0] == 0:
                self.instr_pntr = params[1]
            else:
                self.instr_pntr += (nargs + 1)
        elif op == 'less-than':
            a, b, c = params
            self._state[c] = int(a < b)
            self.instr_pntr += (nargs + 1)
        elif op == 'equals':
            a, b, c = params
            self._state[c] = int(a == b)
            self.instr_pntr += (nargs + 1)
        elif op == 'output':
            a = params[0]
            self.output_queue.put(a)
            self.instr_pntr += (nargs + 1)
        elif op == 'adjust-relative-base':
            a = params[0]
            self.relative_base += a
            self.instr_pntr += (nargs + 1)
        elif op == 'stop':
            pass
        else:
            raise ValueError("Not valid opcode")

    def run_until_stop(self):
        while not self.has_stopped:
            self.step()


def run_siso_program(prog,inval):
    q1 = queue_from_iterable([inval])
    q2 = Queue()
    c = Computer(prog, q1, q2)
    c.run_until_stop()
    outputs = queue_to_list(q2)
    outval = outputs[0]
    return outval