import logging
from collections import defaultdict
from queue import Queue

from day13.lib import BLOCK, tile_ids, Breakout
from util import get_program, Computer, grouper, queue_to_list

LOG = logging.getLogger(__name__)


def solve_part_one():
    p = get_program('../inputs/day13.txt')
    c = Computer(p, Queue(), Queue())
    c.run_until_stop()
    all_outputs = queue_to_list(c.output_queue)
    all_outputs = all_outputs[:-1] # skip the final "program terminated"-output

    screen = defaultdict(int)
    for x, y, tile_id in grouper(all_outputs, 3):

        assert tile_id in tile_ids, f"invalid code: {tile_id}"
        screen[(x, y)] = tile_id

    return sum(1 for tid in screen.values() if tid == BLOCK)

def solve_part_two():
    b= Breakout()
    b.run(use_ai=True, show_output=False)
    return b.score

if __name__ == "__main__":
    logging.basicConfig(level=logging.WARN)
    print(solve_part_one())  # 270   is correct
    print(solve_part_two())  # 12535 is correct
