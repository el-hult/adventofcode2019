from enum import IntEnum
from operator import itemgetter
from threading import Thread

from computer import Computer


class RotDir(IntEnum):
    Left90Deg = 0
    Right90Deg = 1


class Dir(IntEnum):
    Up = 0
    Right = 1
    Down = 2
    Left = 3


class PanelColor(IntEnum):
    Black = 0
    White = 1


direction_marker = {
    Dir.Up: "^",
    Dir.Left: "<",
    Dir.Right: ">",
    Dir.Down: "v",
}


class EmergencyHullPaintingRobot:
    def __init__(self, brain: Computer, panel_grid):
        self.direction = Dir.Up
        self.position = (0, 0)
        self.grid = panel_grid
        self.brain = brain
        self.painted_coordinates = set()

    def move_forward(self):
        pos = self.position
        if self.direction == Dir.Up:
            new_pos = (pos[0], pos[1] + 1)
        elif self.direction == Dir.Right:
            new_pos = (pos[0] + 1, pos[1])
        elif self.direction == Dir.Down:
            new_pos = (pos[0], pos[1] - 1)
        elif self.direction == Dir.Left:
            new_pos = (pos[0] - 1, pos[1])
        else:
            raise RuntimeError
        self.position = new_pos

    def turn(self, rd: RotDir):
        old_dir = self.direction
        diff = 1 if rd == RotDir.Right90Deg else -1
        new_dir = Dir((old_dir + diff) % 4)
        self.direction = new_dir

    def paint(self, c: PanelColor):
        self.grid[self.position] = c
        self.painted_coordinates.add(self.position)

    def use_camera(self) -> PanelColor:
        return self.grid[self.position]

    def run_until_stop(self,verbose=False):
        brain_thread = Thread(target=self.brain.run_until_stop)
        brain_thread.start()
        while brain_thread.is_alive():
            self.brain.input_queue.put(self.use_camera())
            color_instr = PanelColor(self.brain.output_queue.get(timeout=1))
            self.paint(color_instr)
            turn_instr = RotDir(self.brain.output_queue.get(timeout=1))
            self.turn(turn_instr)
            self.move_forward()

            if verbose:
                print("==========================================")
                print(chargrid_to_str(plot_panels_and_robot(self)))
                print("==========================================")

        if not self.brain.has_stopped:
            raise RuntimeError


def plot_panels_and_robot(robot):
    grid = robot.grid
    robot_marker = direction_marker[robot.direction]
    robot_x = robot.position[0]
    robot_y = robot.position[1]
    if len(grid.keys()) == 0:
        return [['.']]
    xmax = max(max(map(itemgetter(0), grid.keys())),robot_x)
    xmin = min(min(map(itemgetter(0), grid.keys())),robot_x)
    ymax = max(max(map(itemgetter(1), grid.keys())),robot_y)
    ymin = min(min(map(itemgetter(1), grid.keys())),robot_y)

    n_lines = ymax - ymin + 1
    n_cols = xmax - xmin + 1
    output_grid = [['.'] * n_cols for _ in range(n_lines)]
    for k, v in grid.items():
        x, y = k
        v = '.' if v == PanelColor.Black else '#'
        output_grid[ymax - y][x - xmin] = v
    output_grid[ymax - robot_y][robot_x - xmin] = robot_marker
    return output_grid


def chargrid_to_str(list_of_list_of_char):
    return "\n".join(map(lambda l: "".join(l), list_of_list_of_char))