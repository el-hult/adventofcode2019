import operator
from itertools import groupby, tee, starmap
from typing import Literal


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def has_six_digits(i: int):
    return 100_000 <= i <= 999_999


def is_nondecreasing_sequence(i: int):
    pairs = pairwise(str(i))
    goes_up = starmap(operator.le, pairs)
    nondecreasing = all(goes_up)
    return nondecreasing


def one_pair_is_not_triplet(i: int):
    return 2 in {sum(1 for _ in g) for _, g in groupby(str(i))}


def has_pair(i: int):
    pairs = pairwise(str(i))
    is_equal = starmap(operator.eq, pairs)
    return any(is_equal)


def moar_numbers(start_inclusive, stop_inclusive, part=Literal['a', 'b']):
    current = start_inclusive
    check_extra = part == 'b'
    while current <= stop_inclusive:
        current_fulfils_spec = (
                has_six_digits(current) and
                is_nondecreasing_sequence(current) and
                has_pair(current) and
                (not check_extra or one_pair_is_not_triplet(current))
        )
        if current_fulfils_spec:
            yield current
        current += 1


with open('inputs/day4.txt','r') as f:
    MY_INPUT = f.readline()
start, stop = [int(i) for i in MY_INPUT.split("-")]

print(f"Ans to A:{sum(1 for i in moar_numbers(start, stop, 'a'))}")  # 1063 is right
print(f"Ans to B:{sum(1 for i in moar_numbers(start, stop, 'b'))}")  # 686 is right
