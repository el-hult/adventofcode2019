from day04.day4_lib import moar_numbers

from util import read_input_file

MY_INPUT = read_input_file('day4.txt')
start, stop = [int(i) for i in MY_INPUT.split("-")]
print(f"Ans to A:{sum(1 for i in moar_numbers(start, stop, 'a'))}")  # 1063 is right
print(f"Ans to B:{sum(1 for i in moar_numbers(start, stop, 'b'))}")  # 686 is right
