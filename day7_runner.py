import itertools

from computer import get_program
from day7_lib import calc_amp, calc_amp_with_feedback

if __name__ == "__main__":
    p = get_program("inputs/day7.txt")

    all_possible_phase_settings = itertools.permutations(range(5))
    a_max, max_config = max(
        ((calc_amp(p, phase_config), phase_config) for phase_config in all_possible_phase_settings),
        key=lambda s: s[0])
    print(f"The maximal amplitude that 5 amps can give is: {a_max}")



    amplification_and_settings = (
        (calc_amp_with_feedback(p, phase_config), phase_config)
        for phase_config in
        itertools.permutations(range(5, 10))
    )
    a_max, max_config = max(amplification_and_settings, key=lambda s: s[0])
    print(f"With feedback the max becomes {a_max}")
