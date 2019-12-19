from collections import defaultdict
from queue import Queue

from day11_lib import PanelColor, EmergencyHullPaintingRobot, chargrid_to_str, plot_panels_and_robot

from util import get_program, Computer

p = get_program('inputs/day11.txt')

grid = defaultdict(lambda: PanelColor.Black)
brain = Computer(p, Queue(), Queue())
robot = EmergencyHullPaintingRobot(brain, grid)
robot.run_until_stop(verbose=False)
print(f"ans a:{len(robot.painted_coordinates)}")  # 1964 is just right!


grid = defaultdict(lambda: PanelColor.Black)
grid[(0, 0)] = PanelColor.White
brain = Computer(p, Queue(), Queue())
robot = EmergencyHullPaintingRobot(brain, grid)
robot.run_until_stop(verbose=False)
print(chargrid_to_str(plot_panels_and_robot(robot)))
print(f"ans b in image above")  # FKEKCFRK is right
