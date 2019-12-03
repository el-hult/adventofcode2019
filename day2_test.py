from day2_lib import Computer
from nose.tools import assert_equals


def test_case0():
    state1 = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    c = Computer(state1)
    c.step()
    assert_equals(c.state, [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50])
    c.step()
    assert_equals(c.state, [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50])
    c.step()
    assert c.has_stopped


def test_case1():
    instate = [1, 0, 0, 0, 99]
    outstate = [2, 0, 0, 0, 99]
    c = Computer(instate)
    c.run_until_stop()
    assert_equals(c.state, outstate)


def test_case2():
    instate = [2, 3, 0, 3, 99]
    outstate = [2, 3, 0, 6, 99]
    c = Computer(instate)
    c.run_until_stop()
    assert_equals(c.state, outstate)


def test_case3():
    instate = [2, 4, 4, 5, 99, 0]
    outstate = [2, 4, 4, 5, 99, 9801]
    c = Computer(instate)
    c.run_until_stop()
    assert_equals(c.state, outstate)


def test_case4():
    instate = [1, 1, 1, 4, 99, 5, 6, 0, 99]
    outstate = [30, 1, 1, 4, 2, 5, 6, 0, 99]
    c = Computer(instate)
    c.run_until_stop()
    assert_equals(c.state, outstate)
