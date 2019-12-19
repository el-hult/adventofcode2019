INPUT_PATH = 'inputs/day1.txt'

from day1_lib import calculate_fuel_consumption, calculate_fuel_consumption_plus_fuel_for_fuel

if __name__ == "__main__":
	total_fuel_a = 0
	total_fuel_b = 0
	with open(INPUT_PATH) as f:
		for mass_as_str in f:
			total_fuel_a += calculate_fuel_consumption(int(mass_as_str))
			total_fuel_b += calculate_fuel_consumption_plus_fuel_for_fuel(int(mass_as_str))

	print(f"Ans A:{total_fuel_a}")
	print(f"Ans B:{total_fuel_b}")



