from itertools import combinations
from operator import itemgetter

from day10.day10_lib import find_best_location, parse_map, Graph, has_line_of_sight, n_between, angle_to, \
    find_nth_to_be_lasered

input1 = """
.#..#
.....
#####
....#
...##
""".strip()

input1_countmap="""
.7..7
.....
67775
....7
...87
""".strip()

input2 = """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####"""

input3=""".#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##"""

def test0():
    """Parse a simple map"""
    asteroid_map = parse_map(input1)
    true_map = {(1, 0), (4, 0), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (4, 3), (3, 4), (4, 4)}
    assert asteroid_map == true_map



def test1():
    """Compute correct number of neighbors for a specific map"""
    asteroid_map = parse_map(input1)
    los_graph = Graph()

    for a in asteroid_map:
        los_graph.add_node(a)

    for (from_, to_) in combinations(asteroid_map, 2):
        if has_line_of_sight(from_,to_,asteroid_map):
            los_graph.add_edge((from_, to_))

    detector_count_per_asteroid = [
        (node_id,len(node_dict['neighbors']))
        for node_id,node_dict in los_graph.nodes.items()
    ]
    outdata = [['.'] * 5 for _ in range(5)]
    for (x,y),c in detector_count_per_asteroid:
        outdata[y][x] = c
    outmap = "\n".join(
        map(lambda s: "".join(map(lambda c: str(c),s))
            ,outdata)
    )
    assert outmap ==input1_countmap


def test2():
    """Draw correct conclusions about the smallest map"""
    asteroid_map = parse_map(input1)
    pos,detectables = find_best_location(asteroid_map)
    assert (3, 4)==pos
    assert 8==detectables


def test3():
    asteroid_map = parse_map(input2)
    pos,detectables = find_best_location(asteroid_map)
    assert (5, 8)==pos
    assert 33==detectables

def test4():
    asteroid_map = parse_map(input3)
    pos,detectables = find_best_location(asteroid_map)
    assert (11, 13)==pos
    assert 210==detectables

def test5():
    asteroid_map = parse_map(input3)
    laser_station = (11, 13)
    asteroid_map.remove(laser_station)
    asdf = ((a,n_between(laser_station,a,asteroid_map),angle_to(laser_station,a)) for a in asteroid_map)
    asdf_sorted_by_angle = sorted(asdf,key=itemgetter(2))
    asdf_sorted_by_depth_and_angle = sorted(asdf_sorted_by_angle,key=itemgetter(1))
    listigt = [t[0] for t in asdf_sorted_by_depth_and_angle]
    assert listigt[1-1]==(11,12)
    assert listigt[2-1]==(12,1)
    assert listigt[3-1]==(12,2)
    assert listigt[10-1]==(12,8)
    assert listigt[20-1]==(16,0)
    assert listigt[50-1]==(16,9)
    assert listigt[100-1]==(10,16)
    assert listigt[199-1]==(9,6)
    assert listigt[200-1]==(8,2)
    assert listigt[201-1]==(10,9)
    assert listigt[299-1]==(11,1)
    assert len(listigt)==299

def test6():

    asteroid_map = parse_map(input3)
    laser_station = (11, 13)
    n = 200

    twohudrefth = find_nth_to_be_lasered(laser_station,asteroid_map,n)
    assert twohudrefth==(8,2)


