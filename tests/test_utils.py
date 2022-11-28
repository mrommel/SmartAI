import unittest

from genetic_algorithm.function_tree import FunctionTree
from genetic_algorithm.utils import bin2float, float2bin, bin2int, int2bin


class UtilsTestCase(unittest.TestCase):

	def test_float2bin(self):
		"""
			test float2bin
		"""
		val = float2bin(3.1415)

		assert val == '0100000000001001001000011100101011000000100000110001001001101111'

	def test_bin2float(self):
		"""
			test bin2float
		"""
		val = bin2float('0100000000001001001000011100101011000000100000110001001001101111')

		assert val == 3.1415

	def test_float_conversion(self):
		assert bin2float(float2bin(23475.43)) == 23475.43
		assert float2bin(bin2float('01101111'), 8) == '01101111'

	def test_int2bin(self):
		"""
			test float2bin
		"""
		val = int2bin(32, 8)

		assert val == '00100000'


	def test_bin2int(self):
		"""
			test bin2int
		"""
		val = bin2int('00100000')

		assert val == 32

	def test_int_conversion(self):
		assert bin2int(int2bin(342)) == 342
		assert int2bin(bin2int('0100000010001001010001001001101111')) == '100000010001001010001001001101111'


