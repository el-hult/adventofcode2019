from day10_lib import find_best_location, find_nth_to_be_lasered, parse_map

from util import read_file

innn = read_file('inputs/day10.txt')
asteroid_map = parse_map(innn)
pos, detectables = find_best_location(asteroid_map)
print("Part A!")
print(detectables)
ass = find_nth_to_be_lasered(pos, asteroid_map, 200)
print("Part B!")
print(ass[0] * 100 + ass[1])
