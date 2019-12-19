from day3_lib import *
from nose.tools import assert_equals


def test_case0():
    input = \
        """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""
    output = 159
    grid, coords = process_inputs(parse_problem_input(input))
    ans = get_min_dist_to_crossing(coords)
    assert_equals(ans, output)


def test_moar():
    assert_equals(get_min_dist_to_crossing([(Crossing(10,10,0,0))]), 20)


def test_moar_neg():
    assert_equals(get_min_dist_to_crossing([Crossing(-10,10,0,0)]),20)


def test_case00():
    input = \
        """R8,U5,L5,D3
U7,R6,D4,L4"""
    output = 6
    grid, coords = process_inputs(parse_problem_input(input))
    ans = get_min_dist_to_crossing(coords)
    assert_equals(ans, output)


def test_printer():
    input = \
        """R8,U5,L5,D3
U7,R6,D4,L4"""
    output = """...........
.2222222...
.2.....2...
.2..111X11.
.2..1..2.1.
.2.2X222.1.
.2..1....1.
.2.......1.
.o11111111.
..........."""
    grid, _ = process_inputs(parse_problem_input(input))
    assert_equals(grid.pretty_print(), output)


def test_case1():
    input = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    output = 135
    _, coords = process_inputs(parse_problem_input(input))
    ans = get_min_dist_to_crossing(coords)
    assert_equals(ans, output)


def test_parse_1():
    assert_equals(parse_single_input("U92"), (CardinalDirection.U, 92))


def test_parse_2():
    assert_equals(parse_line("R7,D30,L83,U83"), [
        (CardinalDirection.R, 7),
        (CardinalDirection.D, 30),
        (CardinalDirection.L, 83),
        (CardinalDirection.U, 83),
    ])


def test_parse_d():
    assert_equals(parse_problem_input("R7,D30\nL83,U83"), ([
                                                               (CardinalDirection.R, 7),
                                                               (CardinalDirection.D, 30)], [
                                                               (CardinalDirection.L, 83),
                                                               (CardinalDirection.U, 83),
                                                           ]))
