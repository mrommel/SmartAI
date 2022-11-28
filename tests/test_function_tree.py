import unittest

from genetic_algorithm.function_tree import FunctionTree, FunctionType


class FunctionTreeTestCase(unittest.TestCase):

	def test_deserialize_node_value(self):
		"""
			tree
		"""
		tree_val = '00000100000000001001001000011100101011000000100000110001001001101111'
		func = FunctionTree(tree_val)

		assert func.valid()

	def test_deserialize_node_variable(self):
		"""
			tree
		"""
		tree_val = '00010100000000001001001000011100101011000000100000110001001001101111'
		func = FunctionTree(tree_val, ['a'])

		assert func.valid()

	def test_deserialize_node_wrong_type(self):
		"""
			tree
		"""
		tree_val = '00110100000000001001001000011100101011000000100000110001001001101111'

		with self.assertRaises(Exception) as context:
			func = FunctionTree(tree_val)

			self.assertTrue('This is broken' in context.exception)

			assert func.valid()

	def test_deserialize_tree(self):
		"""
			tree
		"""
		tree_val = '00101100000000001001001000011100101011000000100000110001001001101111' \
					'00000100000000001001001000011100101011000000100000110001001001101111' \
					'00000100000000001001001000011100101011000000100000110001001001101111'
		func = FunctionTree(tree_val)

		assert func.valid()
		assert func.evaluate({}) == 6.2830

	def test_evaluate_node_value(self):
		"""
			tree
		"""
		tree_val = '00000100000000001001001000011100101011000000100000110001001001101111'
		func = FunctionTree(tree_val)

		assert func.evaluate({}) == 3.1415

	def test_evaluate_node_variable(self):
		"""
			tree
		"""
		tree_val = '00010000000000000000000000000000000000000000000000000000000000000001'
		func = FunctionTree(tree_val, ['a', 'b'])

		assert func.evaluate({'a': 3.1415, 'b': 0.0}) == 0.0

	def test_evaluate_tree_sum(self):
		"""
			tree
		"""
		tree_val = '00101100000000001001001000011100101011000000100000110001001001101111' \
					'00000100000000001001001000011100101011000000100000110001001001101111' \
					'00000100000000001001001000011100101011000000100000110001001001101111'
		func = FunctionTree(tree_val)

		assert func.evaluate({}) == 6.2830

	def test_evaluate_tree_mul(self):
		"""
			tree
		"""
		tree_val = '01001100000000001001001000011100101011000000100000110001001001101111' \
					'00000100000000001001001000011100101011000000100000110001001001101111' \
					'00000100000000001001001000011100101011000000100000110001001001101111'
		func = FunctionTree(tree_val)

		assert func.function_type == FunctionType.Multiplication
		assert func.evaluate({}) == 9.86902225

	def test_as_function_node_value(self):
		"""
			tree
		"""
		tree_val = '00000100000000001001001000011100101011000000100000110001001001101111'
		func = FunctionTree(tree_val, ['a'])

		assert func.as_function() == '3.142'

	def test_as_function_node_variable(self):
		"""
			tree
		"""
		tree_val = '00010100000000001001001000011100101011000000100000110001001001101111'
		func = FunctionTree(tree_val, ['a'])

		assert func.as_function() == 'a'

	def test_as_function_tree_sum(self):
		"""
			tree
		"""
		tree_val = '00101100000000001001001000011100101011000000100000110001001001101111' \
					'00000100000000001001001000011100101011000000100000110001001001101111' \
					'00000100000000001001001000011100101011000000100000110001001001101111'
		func = FunctionTree(tree_val)

		assert func.as_function() == '(3.142 + 3.142)'

	def test_as_function_tree_mul(self):
		"""
			tree
		"""
		tree_val = '01001100000000001001001000011100101011000000100000110001001001101111' \
					'00000100000000001001001000011100101011000000100000110001001001101111' \
					'00000100000000001001001000011100101011000000100000110001001001101111'
		func = FunctionTree(tree_val)

		assert func.as_function() == '(3.142 * 3.142)'
