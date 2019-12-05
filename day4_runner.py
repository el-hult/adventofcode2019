from day4_lib import moar_numbers

with open('inputs/day4.txt','r') as f:
    MY_INPUT = f.readline()
start, stop = [int(i) for i in MY_INPUT.split("-")]

print(f"Ans to A:{sum(1 for i in moar_numbers(start, stop, 'a'))}")  # 1063 is right
print(f"Ans to B:{sum(1 for i in moar_numbers(start, stop, 'b'))}")  # 686 is right
