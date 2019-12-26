import logging
from collections import namedtuple, defaultdict
from enum import IntEnum
from operator import itemgetter
from queue import Queue
from threading import Thread
from typing import Optional

from util import get_program, Computer, ComputerSignals, chargrid_to_str, my_sign

LOG = logging.getLogger(__name__)

EMPTY = 0
WALL = 1
BLOCK = 2
HORZ_PDL = 3
BLL = 4
tile_ids = [EMPTY, WALL, BLOCK, HORZ_PDL, BLL]
symbols = {
    EMPTY: "\u2591",
    WALL: "\u2588",
    BLOCK: "\u2592",
    HORZ_PDL: "\u2550",
    BLL: "0",
}
Pos = namedtuple("Pos", "x y")


class JoystickPosition(IntEnum):
    left = -1
    mid = 0
    right = 1


class Breakout:
    def __init__(self):
        p = get_program('../inputs/day13.txt')
        p[0] = 2 # insert two coins in the slot machine
        self.brain = Computer(p, Queue(), Queue())
        self.screen = defaultdict(int)
        self.ball_position = None
        self.paddle_position: Optional[Pos] = None
        self.prev_ball_position: Optional[Pos] = None
        self.score = 0

    def run(self, use_ai: bool, show_output: bool):
        brain_thread = Thread(target=self.brain.run_until_stop)
        brain_thread.start()
        BRAIN_IS_RUNNING = True
        while BRAIN_IS_RUNNING:
            while not self.brain.output_queue.empty():
                x = self.brain.output_queue.get(timeout=1)
                if x == ComputerSignals.input_needed:
                    if use_ai:
                        p = self.predict_ball_position()
                        i = self.compute_best_move(p)
                        LOG.info(f"Made move: {i}")
                    else:
                        raw = input("input direction (-1 left, 0 stay, 1 right)")
                        i = int(raw)
                    assert i in [-1, 0, 1]
                    self.brain.input_queue.put(i)

                elif x == ComputerSignals.program_terminated:
                    BRAIN_IS_RUNNING = False
                    LOG.info("Program finished")

                else:
                    y = self.brain.output_queue.get(timeout=1)
                    pos = Pos(x, y)
                    z = self.brain.output_queue.get(timeout=1)
                    if x == -1 and y == 0:
                        self.score = z
                    else:
                        assert z in [*tile_ids, -1], f"Unexpected output from brain: {z}"
                        self.screen[pos] = z
                        if z == BLL:
                            self.prev_ball_position = self.ball_position
                            self.ball_position = pos
                        elif z == HORZ_PDL:
                            self.paddle_position = pos

            if show_output:
                print(self.rendered_game)

        brain_thread.join(1) # the brain thread should be dead now...
        if brain_thread.is_alive():
            raise RuntimeError

        if not self.brain.has_stopped:
            raise RuntimeError

        if show_output:
            print("Game Over!")
            print(f"Final score: {self.score}")

    @property
    def rendered_game(self):
        grid = self.screen
        if len(grid.keys()) == 0:
            return [[' ']]
        xmax = max(map(itemgetter(0), grid.keys()))
        xmin = min(map(itemgetter(0), grid.keys()))
        ymax = max(map(itemgetter(1), grid.keys()))
        ymin = min(map(itemgetter(1), grid.keys()))

        n_lines = ymax - ymin + 1
        n_cols = xmax - xmin + 1
        output_grid = [[' '] * n_cols for _ in range(n_lines)]
        for k, v in grid.items():
            x, y = k
            output_grid[ymax - y][x - xmin] = symbols[v]
        out = (f"Score: {self.score}")
        output_grid_up_down = output_grid[::-1]
        out += "\n" + (chargrid_to_str(output_grid_up_down))
        return out

    def compute_best_move(self, target_pos: Optional[Pos]) -> JoystickPosition:
        if target_pos is None:
            return JoystickPosition.mid
        elif self.ball_position.x == self.paddle_position.x and self.ball_position.y == self.paddle_position.y - 1:
            # Special case to avoid diagonal-bounces, which can be a move with gauaranteed failure failure-move
            return JoystickPosition.mid
        else:
            diff = target_pos.x - self.paddle_position.x
            return JoystickPosition(my_sign(diff))

    def predict_ball_position(self):
        """Calculate the x-position of where the ball will be, one step ahead. Ignore bounces"""
        if self.ball_velocity is None or self.ball_position is None:
            return None

        LOG.debug(f"Paddle is now at x={self.paddle_position}")
        LOG.debug(f"Ball is now at x={self.ball_position}")
        x_dir, y_dir = self.ball_velocity
        ball_next_pos = Pos(self.ball_position[0] + x_dir, self.ball_position[1] + y_dir)
        LOG.debug(f"Predicted ball position is: {ball_next_pos}")
        return ball_next_pos

    @property
    def ball_velocity(self):
        if self.ball_position is None or self.prev_ball_position is None:
            return None
        x_dir = self.ball_position[0] - self.prev_ball_position[0]
        y_dir = self.ball_position[1] - self.prev_ball_position[1]
        return (x_dir, y_dir)