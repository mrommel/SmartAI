from genetic_algorithm.function_tree import FunctionTree
from genetic_algorithm.individual import Individual
from genetic_algorithm.data import SampleDataItem, SampleData


class GeneFunction(Individual):
	"""
		Manage an individual gene function

		4 bits define the type
		64 bits define a number
	"""

	def __init__(self, length=68, bitstring_or_list=None, var_names: [] = None):
		super(GeneFunction, self).__init__(length, bitstring_or_list)

		binary_str = ''.join([str(b) for b in self.genes])
		self.function_tree = FunctionTree(binary_str, var_names)

	def gene_as_formula(self) -> str:
		return self.function_tree.as_function()

	def _error_for_data_item(self, data: SampleDataItem) -> float:
		"""
			get error for given values

			:param data: data item to test
			:return: error for given values
		"""
		val = self.function_tree.evaluate(data.values) - data.expected
		return val * val

	def error_for_data(self, data: SampleData) -> float:
		"""
			get error for given values

			:param data: data to test
			:return: error for given values
		"""
		error = 0.0

		for item in data.items:
			error += self._error_for_data_item(item)

		return error
