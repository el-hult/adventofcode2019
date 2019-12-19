from math import floor


def calculate_fuel_consumption(mass: int) -> int:
    fuel_needed = floor(mass / 3) - 2
    return fuel_needed


def calculate_fuel_consumption_plus_fuel_for_fuel(mass: int) -> int:
    fuel_needed = 0
    newly_added_mass = calculate_fuel_consumption(mass)
    while newly_added_mass > 0:
        fuel_needed += newly_added_mass
        newly_added_mass = calculate_fuel_consumption(newly_added_mass)
    return fuel_needed
