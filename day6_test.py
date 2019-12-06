from nose.tools import assert_equals

from day6_lib import make_tree_from_adj_list, calculate_hops, all_descendants_BFS

input_ = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""
orbits_ = [p.split(")") for p in input_.splitlines()]


def test_bfs():
    ns = all_descendants_BFS(make_tree_from_adj_list(orbits_))
    n_names = [n.name for n in ns]
    assert_equals(n_names, ['COM', 'B', 'C', 'G', 'D', 'H', 'E', 'I', 'F', 'J', 'SAN', 'K', 'L', 'YOU'])


def test_part2():
    com_object = make_tree_from_adj_list(orbits_)
    hops = calculate_hops(com_object)
    assert_equals(hops,4)
