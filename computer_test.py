from queue import Queue

import nose.tools as n

from computer import Computer, thermal_environment_supervision_terminal, basic_operation_of_system_test, \
    run_siso_program
from util import queue_to_list


def test_day2_test1():
    state1 = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    c = Computer(state1, None, None)
    c.step()
    n.assert_equals(c.state, [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50])
    c.step()
    n.assert_equals(c.state, [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50])
    c.step()
    assert c.has_stopped


def test_day2_test2():
    instate = [1, 0, 0, 0, 99]
    outstate = [2, 0, 0, 0, 99]
    c = Computer(instate, None, None)
    c.run_until_stop()
    n.assert_equals(c.state, outstate)


def test_day2_test3():
    instate = [2, 3, 0, 3, 99]
    outstate = [2, 3, 0, 6, 99]
    c = Computer(instate, None, None)
    c.run_until_stop()
    n.assert_equals(c.state, outstate)


def test_day2_test4():
    instate = [2, 4, 4, 5, 99, 0]
    outstate = [2, 4, 4, 5, 99, 9801]
    c = Computer(instate, None, None)
    c.run_until_stop()
    n.assert_equals(c.state, outstate)


def test_day2_test5():
    instate = [1, 1, 1, 4, 99, 5, 6, 0, 99]
    outstate = [30, 1, 1, 4, 2, 5, 6, 0, 99]
    c = Computer(instate, None, None)
    c.run_until_stop()
    n.assert_equals(c.state, outstate)


def test_day5_test1():
    """Make sure the TEST program loads"""
    p = thermal_environment_supervision_terminal()
    assert type(p) is list
    assert all(type(i) == int for i in p)


def test_day5_test2():
    """TEST program runs okay"""
    p = thermal_environment_supervision_terminal()
    inval = 1
    q1 = Queue()
    q1.put(inval)
    q2 = Queue()
    c = Computer(p, q1, q2)
    c.run_until_stop()
    outputs = queue_to_list(q2)
    diagnostic_codes = outputs[:-1]
    n.assert_equals(diagnostic_codes, [0, 0, 0, 0, 0, 0, 0, 0, 0])


def test_day5_test3():
    """Is 1 equal to 8? (position_mode)"""
    output_code= run_siso_program([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 1)
    n.assert_equals(output_code, 0)


def test_day5_test4():
    """Is 9 less equal to 8? (position_mode)"""
    output_code= run_siso_program([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 9)
    n.assert_equals(output_code, 0)


def test_day5_test5():
    """Is 8 equal to 8? (immediate_mode)"""
    output_code= run_siso_program([3, 3, 1108, -1, 8, 3, 4, 3, 99], 8)
    n.assert_equals(output_code, 1)


def test_day5_test6():
    """Is 3 less than 8? (immediate_mode)"""
    output_code = run_siso_program([3, 3, 1107, -1, 8, 3, 4, 3, 99], 3)
    n.assert_equals(output_code, 1)

def test_day5_test7():
    """Jump test zero? (position mode)"""
    p = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
    inval = 0
    output_code = run_siso_program(p, inval)
    n.assert_equals(output_code, 0)

def test_day5_test8():
    """Jump test nonzero? (position mode)"""
    p = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
    inval = 999
    output_code = run_siso_program(p, inval)
    n.assert_equals(output_code, 1)


def test_day5_test9():
    """Jump test zero? (immediate mode)"""
    p = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
    inval = 0
    output_code = run_siso_program(p, inval)
    n.assert_equals(output_code, 0)


def test_day5_test10():
    """Jump test nonzero? (immediate mode)"""
    p = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
    inval = 999
    output_code = run_siso_program(p, inval)
    n.assert_equals(output_code, 1)

p_larger = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,    1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,    999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
def test_day5_test11():
    """Complicated check is less than 8"""
    output_code = run_siso_program(p_larger, 7)
    n.assert_equals(output_code, 999)

def test_day5_test12():
    """Complicated check is equal to 8"""
    output_code = run_siso_program(p_larger, 8)
    n.assert_equals(output_code, 1000)

def test_day5_test13():
    """Complicated check is greater than  8"""
    output_code = run_siso_program(p_larger, 200)
    n.assert_equals(output_code, 1001)

def test_day9_test1():
    """Can copy self?"""
    prog = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    q2 = Queue()
    c = Computer(prog, None, q2)
    c.run_until_stop()
    outputs = queue_to_list(q2)
    n.assert_equals(outputs, prog)


def test_day9_test2():
    """Can output a 16-digit number?"""
    prog = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
    q2 = Queue()
    c = Computer(prog, None, q2)
    c.run_until_stop()
    output = queue_to_list(q2)[0]
    output_n_digit = len(str(output))
    n.assert_equals(output_n_digit, 16)


def test_day9_test3():
    """output the large number in the middle"""
    prog = [104, 1125899906842624, 99]
    q2 = Queue()
    c = Computer(prog, None, q2)
    c.run_until_stop()
    output = queue_to_list(q2)[0]
    n.assert_equals(output, 1125899906842624)


def test_day9_test4():
    """Make sure the TEST program loads"""
    p = basic_operation_of_system_test()
    assert type(p) is list
    assert all(type(i) == int for i in p)

def test_day9_test5():
    """Can change relative base"""
    q = Queue()
    c = Computer([109,19,204,-34],None,q)
    c.relative_base = 2000
    c._state[1985] = 1234
    c.step()
    c.step()
    n.assert_equals(q.get(),1234)