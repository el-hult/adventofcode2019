
from day12.day12_lib import parse_particles, apply_gravity, travel_with_velocity, ps_to_str, \
    naive_recurrence_check, better_recurrence_check

test_input = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""

after_0 = """pos=<x= -1, y=  0, z=  2>, vel=<x=  0, y=  0, z=  0>
pos=<x=  2, y=-10, z= -7>, vel=<x=  0, y=  0, z=  0>
pos=<x=  4, y= -8, z=  8>, vel=<x=  0, y=  0, z=  0>
pos=<x=  3, y=  5, z= -1>, vel=<x=  0, y=  0, z=  0>"""

after_1 = """pos=<x=  2, y= -1, z=  1>, vel=<x=  3, y= -1, z= -1>
pos=<x=  3, y= -7, z= -4>, vel=<x=  1, y=  3, z=  3>
pos=<x=  1, y= -7, z=  5>, vel=<x= -3, y=  1, z= -3>
pos=<x=  2, y=  2, z=  0>, vel=<x= -1, y= -3, z=  1>"""


def test():
    ps = parse_particles(test_input)
    ps_to_str(ps) == after_0
    apply_gravity(ps)
    travel_with_velocity(ps)
    # print(ps_to_str(ps))
    ps_to_str(ps) == after_1


def test2():
    ps = parse_particles(test_input)
    i = naive_recurrence_check(ps)
    assert i == 2772


def test2b():
    ps = parse_particles(test_input)
    i = better_recurrence_check(ps)
    assert i == 2772  , i


input3 = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""


def test3():
    ps = parse_particles(input3)
    i = better_recurrence_check(ps)
    assert i == 4_686_774_924
