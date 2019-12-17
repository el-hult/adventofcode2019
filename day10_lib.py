import itertools
import logging
import math
from math import copysign, gcd
from operator import itemgetter
from typing import Hashable, Tuple, Dict

LOG = logging.getLogger(__name__)

ASTEROID_MARKER = "#"

NodeID = Hashable
Node = Dict
Edge = Tuple[NodeID, NodeID]


class Graph():
    def __init__(self):
        self.nodes: Dict[NodeID, Node] = dict()
        self.edges = set()

    def add_node(self, nid: Hashable):
        assert nid not in self.nodes.keys()
        self.nodes[nid] = dict()
        self.nodes[nid]['neighbors'] = {}

    def add_edge(self, e: Edge):
        assert len(e) == 2
        assert e not in self.edges, "edge already added!"
        n0 = self.nodes[e[0]]
        n1 = self.nodes[e[1]]
        n0['neighbors'][e[1]] = n1
        n1['neighbors'][e[0]] = n0
        self.edges.add(e)

    def __str__(self):
        return f"Graph with nodes:{list(self.nodes.keys())} and edges:{self.edges}"


def parse_map(s: str):
    asteroids = set()
    size = [0, 0]
    for idy, line in enumerate(s.strip().splitlines()):
        for idx, cell in enumerate(line):
            if cell == ASTEROID_MARKER:
                asteroids.add((idx, idy))
                size[0] = max(size[0], idx + 1)
                size[1] = max(size[1], idy + 1)
    return asteroids


def has_line_of_sight(a_from, a_to, asteroid_map):
    return n_between(a_from, a_to, asteroid_map) == 0


def n_between(a_from, a_to, asteroid_map):
    delta_x = a_to[0] - a_from[0]
    delta_y = a_to[1] - a_from[1]
    number_of_asteroids_between_from_and_to = 0

    if delta_y == 0:
        LOG.debug(f"{a_from} and {a_to} has same y-coordinate")
        step_dir = copysign(1, delta_x)
        LOG.debug(f"{step_dir=}")
        for x in range(1, abs(delta_x)):
            LOG.debug(f"Takes step of length {x}")
            intermediate_pos = (a_from[0] + step_dir * x, a_from[1])
            if intermediate_pos in asteroid_map:
                LOG.debug(f"There is an object at {intermediate_pos} between {a_from} and {a_to}.")
                number_of_asteroids_between_from_and_to += 1
    elif delta_x == 0:
        LOG.debug(f"{a_from} and {a_to} has same x-coordinate")
        step_dir = copysign(1, delta_y)
        LOG.debug(f"{step_dir=}")
        for y in range(1, abs(delta_y)):
            LOG.debug(f"Takes step of length {y}")
            intermediate_pos = (a_from[0], a_from[1] + step_dir * y)
            if intermediate_pos in asteroid_map:
                LOG.debug(f"There is an object at {intermediate_pos} between {a_from} and {a_to}.")
                number_of_asteroids_between_from_and_to += 1
    else:
        LOG.debug(f"Examining diagonal between {a_from} and {a_to}.")
        n_steps = gcd(delta_y, delta_x)
        step_len_y = delta_y / n_steps
        step_len_x = delta_x / n_steps
        for step in range(1, n_steps):
            intermediate_pos = (a_from[0] + step_len_x * step, a_from[1] + step_len_y * step)
            if intermediate_pos in asteroid_map:
                LOG.debug(f"There is an object at {intermediate_pos} between {a_from} and {a_to}.")
                number_of_asteroids_between_from_and_to += 1
    return number_of_asteroids_between_from_and_to

def find_best_location(asteroid_map):
    n_asteroids = len(asteroid_map)
    LOG.debug("Map:")
    LOG.debug(asteroid_map)
    LOG.debug(f"There is {n_asteroids} asteroids in the map.")
    los_graph = Graph()

    for a in asteroid_map:
        los_graph.add_node(a)

    for (from_, to_) in itertools.combinations(asteroid_map, 2):
        if has_line_of_sight(from_, to_, asteroid_map):
            LOG.debug(f"There is LOS between asteroid {from_} and {to_}")
            los_graph.add_edge((from_, to_))

    LOG.debug(los_graph)

    detector_count_per_asteroid = (
        (node_id, len(node_dict['neighbors']))
        for node_id, node_dict in los_graph.nodes.items()
    )
    best_asteroid, n_asteroids_in_line_of_sight = max(
        detector_count_per_asteroid,
        key=lambda t: t[1]
    )

    return best_asteroid, n_asteroids_in_line_of_sight

def angle_to(tup1,tup2):
    """The angle to tup2 from tup1, measured against 'straight up' clockwise, in radians.

    Tuples are given in a coordinate system with (0,0) top left, (1,0) is one step right, (0,1) is one step down,
    and (1,1) is down right.

    >>> angle_to((1,1),(1,0))/math.pi
    0.0
    >>> angle_to((1,1),(2,0))/math.pi
    0.25
    >>> angle_to((1,1),(1,2))/math.pi
    1.0
    >>> angle_to((1,1),(-1,-1))/math.pi
    1.75
    """
    x = tup2[0] - tup1[0]
    y = tup1[1] - tup2[1]
    angle_to_positive_x_axis = math.atan2(y,x)
    angle_to_straight_up = (math.pi/2) -angle_to_positive_x_axis
    positive_angle_to_straight_up = angle_to_straight_up % (2*math.pi)
    return positive_angle_to_straight_up


def find_nth_to_be_lasered(laser_pos,amap,n):
    amap = amap.copy()
    amap.remove(laser_pos)
    asdf = ((a,n_between(laser_pos,a,amap),angle_to(laser_pos,a)) for a in amap)
    asdf_sorted_by_angle = sorted(asdf,key=itemgetter(2))
    asdf_sorted_by_depth_and_angle = sorted(asdf_sorted_by_angle,key=itemgetter(1))
    listigt = [t[0] for t in asdf_sorted_by_depth_and_angle]
    return listigt[n-1]