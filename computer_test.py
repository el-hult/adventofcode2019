import io
from contextlib import redirect_stdout

import nose.tools as n

from computer import get_test_program
from day2_lib import Computer
from util import manage_input


def test_day2_test1():
    state1 = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    c = Computer(state1)
    c.step()
    n.assert_equals(c.state, [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50])
    c.step()
    n.assert_equals(c.state, [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50])
    c.step()
    assert c.has_stopped


def test_day2_test2():
    instate = [1, 0, 0, 0, 99]
    outstate = [2, 0, 0, 0, 99]
    c = Computer(instate)
    c.run_until_stop()
    n.assert_equals(c.state, outstate)


def test_day2_test3():
    instate = [2, 3, 0, 3, 99]
    outstate = [2, 3, 0, 6, 99]
    c = Computer(instate)
    c.run_until_stop()
    n.assert_equals(c.state, outstate)


def test_day2_test4():
    instate = [2, 4, 4, 5, 99, 0]
    outstate = [2, 4, 4, 5, 99, 9801]
    c = Computer(instate)
    c.run_until_stop()
    n.assert_equals(c.state, outstate)


def test_day2_test5():
    instate = [1, 1, 1, 4, 99, 5, 6, 0, 99]
    outstate = [30, 1, 1, 4, 2, 5, 6, 0, 99]
    c = Computer(instate)
    c.run_until_stop()
    n.assert_equals(c.state, outstate)


def test_day5_test1():
    """Make sure the TEST program loads"""
    p = get_test_program()
    assert type(p) is list
    assert all(type(i) == int for i in p)


def test_day5_test2():
    p = get_test_program()
    c = Computer(p)
    f = io.StringIO()
    with manage_input([1]):
        with redirect_stdout(f):
            c.run_until_stop()
    outputs = [int(i) for i in f.getvalue().split()]
    diagnostic_codes = outputs[:-1]
    n.assert_equals(diagnostic_codes,[0, 0, 0, 0, 0, 0, 0, 0, 0])