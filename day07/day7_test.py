import itertools

from day7_lib import calc_amp, calc_amp_with_feedback
from nose.tools import assert_equals

test_program_1 = [int(i) for i in "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0".split(",")]
test_program_2 = [int(i) for i in "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0".split(",")]
test_program_3 = [int(i) for i in "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32," \
                                  "31,31,4,31,99,0,0,0".split(",")]
test_program_4 = [int(i) for i in "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0," \
                                  "0,5".split(",")]
test_program_5 = [int(i) for i in "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1," \
                                  "12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6," \
                                  "99,0,0,0,0,10".split(",")]


def test_1():
    a_max, max_comfig = max(
        ((calc_amp(test_program_1, phase_config), phase_config) for phase_config in itertools.permutations(range(5))),
        key=lambda s: s[0])
    assert_equals(a_max, 43210)
    assert_equals(list(max_comfig), [4, 3, 2, 1, 0])


def test_2():
    a_max, max_comfig = max(
        ((calc_amp(test_program_2, phase_config), phase_config) for phase_config in itertools.permutations(range(5))),
        key=lambda s: s[0])
    assert_equals(a_max, 54321)
    assert_equals(list(max_comfig), [0, 1, 2, 3, 4])


def test_3():
    a_max, max_comfig = max(
        ((calc_amp(test_program_3, phase_config), phase_config) for phase_config in itertools.permutations(range(5))),
        key=lambda s: s[0])
    assert_equals(a_max, 65210)
    assert_equals(list(max_comfig), [1, 0, 4, 3, 2])


def test_4():
    amplification_and_settings = (
        (calc_amp_with_feedback(test_program_4, phase_config), phase_config)
        for phase_config in
        itertools.permutations(range(5, 10))
    )
    a_max, max_config = max(amplification_and_settings, key=lambda s: s[0])
    assert_equals(a_max, 139629729)
    assert_equals(list(max_config), [9, 8, 7, 6, 5])


def test_5():
    amplification_and_settings = (
        (calc_amp_with_feedback(test_program_5, phase_config), phase_config)
        for phase_config in
        itertools.permutations(range(5, 10))
    )
    a_max, max_config = max(amplification_and_settings, key=lambda s: s[0])
    assert_equals(a_max, 18216)
    assert_equals(list(max_config), [9, 7, 8, 5, 6])
