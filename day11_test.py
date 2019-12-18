from collections import defaultdict
from queue import Queue

import nose

from computer import get_program, Computer
from day11_lib import PanelColor, EmergencyHullPaintingRobot, RotDir
from util import queue_from_iterable


def test1():
    def test_run(robot):
        expected_camera_readings = queue_from_iterable([0, 0, 0, 0, 1, 0, 0])
        instruction_list = queue_from_iterable([1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0])
        while not expected_camera_readings.empty():
            nose.tools.assert_equals(robot.use_camera(), expected_camera_readings.get())

            color_instr = PanelColor(instruction_list.get(timeout=1))
            robot.paint(color_instr)
            turn_instr = RotDir(instruction_list.get(timeout=1))
            robot.turn(turn_instr)
            robot.move_forward()

    grid = defaultdict(lambda: PanelColor.Black)
    p = get_program('inputs/day11.txt')

    test_brain = Computer(p, Queue(), Queue())
    test_robot = EmergencyHullPaintingRobot(test_brain, grid)
    test_run(test_robot)
