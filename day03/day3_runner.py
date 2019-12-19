from day3_lib import *

from util import read_file

INPUT_PATH = 'inputs/day3.txt'

if __name__ == "__main__":
    file = read_file(INPUT_PATH)

    lines = parse_problem_input(file)
    _,coords = process_inputs(lines)
    ans_a = get_min_dist_to_crossing(coords)
    ans_b = get_min_line_dist_to_crossing(coords)

    print(f"Answer to part A: {ans_a}")
    print(f"Answer to part B: {ans_b}")