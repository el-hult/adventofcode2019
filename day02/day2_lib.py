from util import Program, Computer


def compute_computer_output(program: Program, noun: int, verb: int) -> int:
    initial_state = program.copy()
    initial_state[1] = noun
    initial_state[2] = verb
    cmp = Computer(initial_state,None,None)
    cmp.run_until_stop()
    return cmp._state[0]
