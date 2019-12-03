import unittest

from day1_lib import calculate_fuel_consumption, calculate_fuel_consumption_plus_fuel_for_fuel


class TestCases(unittest.TestCase):
	def test_one(self):
		for test_i,(inval, outval) in enumerate(zip(
			[12,14,1969,100756],
			[2,2,654,33583]
			)):
			assert calculate_fuel_consumption(inval) == outval, f"Case {test_i}: input{inval}"

	def test_two(self):
		for test_i,(inval, outval) in enumerate(zip(
			[14,1969,100756],
			[2,966,50346]
			)):
			assert calculate_fuel_consumption_plus_fuel_for_fuel(inval) == outval, f"Case {test_i}: input{inval}"