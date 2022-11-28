import unittest

from genetic_algorithm.function_tree import FunctionType, convert_int_to_function_type


class FunctionTypeTestCase(unittest.TestCase):

	def test_parsing(self):
		assert convert_int_to_function_type(0) == FunctionType.Number
		assert convert_int_to_function_type(1) == FunctionType.Variable
		assert convert_int_to_function_type(2) == FunctionType.Sum
		assert convert_int_to_function_type(3) == FunctionType.Subtract
		assert convert_int_to_function_type(4) == FunctionType.Multiplication
		assert convert_int_to_function_type(5) == FunctionType.Divide
		assert convert_int_to_function_type(6) == FunctionType.Sinus
		assert convert_int_to_function_type(7) == FunctionType.Pow
		assert convert_int_to_function_type(8) == FunctionType.Absolute

