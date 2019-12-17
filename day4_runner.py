from day4_lib import moar_numbers
from util import read_file

INPUT_PATH = 'inputs/day4.txt'
MY_INPUT = read_file(INPUT_PATH)
start, stop = [int(i) for i in MY_INPUT.split("-")]
print(f"Ans to A:{sum(1 for i in moar_numbers(start, stop, 'a'))}")  # 1063 is right
print(f"Ans to B:{sum(1 for i in moar_numbers(start, stop, 'b'))}")  # 686 is right
