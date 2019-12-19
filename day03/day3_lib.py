from dataclasses import dataclass
from enum import Enum
from typing import Literal, Tuple, List, Dict, Union

# noinspection PyArgumentList
CardinalDirection = Enum('Turn', ['R', 'L', 'U', 'D'])

Instruction = Tuple[CardinalDirection, int]
Instructions = List[Instruction]
ProblemInput = Tuple[Instructions, Instructions]
Coordinate = Tuple[int, int]

LINE1 = '1'
LINE2 = '2'


@dataclass
class Breadcrumb:
    line_id: Literal[LINE1, LINE2]
    len_from_central_port: int

    def __str__(self):
        return self.line_id


@dataclass
class Crossing:
    x_coord: int
    y_coord: int
    line_1_len_from_central_port: int
    line_2_len_from_central_port: int

    def __str__(self):
        return 'X'


# I cannot understand how to reference the value of a Literal[x] so I'm defining constants for them too.
# Seems really idiotic, and un-idiomatic.
CentralPort = Literal['o']
Empty = Literal['.']
CENTRAL_PORT = 'o'
EMPTY = '.'
GridEntry = Union[Breadcrumb, Crossing, CentralPort, Empty]


class InfiniteGrid():
    """A wrapper for a python dict that is two-indexed and has a default value of EMPTY"""

    def __init__(self):
        self.d: Dict[Tuple[int, int], GridEntry] = {}

    def __setitem__(self, key, value: GridEntry):
        assert len(key) == 2
        self.d[key] = value

    def __getitem__(self, item) -> GridEntry:
        assert len(item) == 2
        return self.d.get(item, EMPTY)

    def pretty_print(self):
        """A pretty printer for troubleshooting purposes"""
        xmin = min(map(lambda z: z[0], self.d.keys()))
        xmax = max(map(lambda z: z[0], self.d.keys()))
        ymin = min(map(lambda z: z[1], self.d.keys()))
        ymax = max(map(lambda z: z[1], self.d.keys()))
        out_rows: List[str] = []
        for y in range(ymax + 1, ymin - 2, -1):
            row = ""
            for x in range(xmin - 1, xmax + 2):
                val = self[x, y]
                row += str(val)
            out_rows.append(row)
        return "\n".join(out_rows)


def step(x: int, y: int, cd: CardinalDirection) -> (int, int):
    if cd == CardinalDirection.U:
        return x, y + 1
    elif cd == CardinalDirection.D:
        return x, y - 1
    elif cd == CardinalDirection.R:
        return x + 1, y
    elif cd == CardinalDirection.L:
        return x - 1, y
    else:
        raise ValueError


def process_inputs(ls: ProblemInput) -> (InfiniteGrid, List[Coordinate]):
    grid = InfiniteGrid()
    crossings: List[Crossing] = []
    grid[0, 0] = CENTRAL_PORT

    dist = y = x = 0
    for cd, steps in ls[0]:
        for _ in range(steps):
            x, y = step(x, y, cd)
            dist += 1
            if grid[x, y] != CENTRAL_PORT:
                grid[x, y] = Breadcrumb(LINE1, dist)

    line2len = y = x = 0
    for cd, steps in ls[1]:
        for _ in range(steps):
            x, y = step(x, y, cd)
            line2len += 1
            if type(grid[x, y]) == Breadcrumb and grid[x, y].line_id == LINE1:
                line1len = grid[x, y].len_from_central_port
                c = Crossing(x, y, line1len, line2len)
                grid[x, y] = c
                crossings.append(c)
            elif grid[x, y] == CENTRAL_PORT:
                pass
            else:
                grid[x, y] = Breadcrumb(LINE2, line2len)
    return grid, crossings


def get_min_dist_to_crossing(crosses: List[Crossing]) -> int:
    return min(map(lambda s: abs(s.x_coord) + abs(s.y_coord), crosses))


def get_min_line_dist_to_crossing(crosses: List[Crossing]) -> int:
    return min(map(lambda s: s.line_1_len_from_central_port + s.line_2_len_from_central_port, crosses))


def parse_single_input(s: str) -> Instruction:
    return CardinalDirection[s[0]], int(s[1:])


def parse_line(s: str) -> List[Instruction]:
    return list(map(parse_single_input, s.split(",")))


def parse_problem_input(s: str) -> ProblemInput:
    ls = s.splitlines()
    assert len(ls) == 2
    return parse_line(ls[0]), parse_line(ls[1])
