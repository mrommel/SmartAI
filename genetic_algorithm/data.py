class SampleDataItem:
	def __init__(self, values: dict, expected: float):
		self.values = values
		self.expected = expected

	def __repr__(self):
		return f'Sample {self.values} => {self.expected}'


class SampleData:
	def __init__(self):
		self.items = []

	def add_values(self, values: dict, expected: float):
		self.items.append(SampleDataItem(values, expected))

	def add_item(self, item: SampleDataItem):
		self.items.append(item)

	def values(self, var_name: str) -> [float]:
		"""
			get all values of a certain var_name

			:param var_name: name of the variable
			:return: array with the values
		"""
		array = []

		for item in self.items:
			array.append(item.values[var_name])

		return array

	def expected_values(self) -> [float]:
		array = []

		for item in self.items:
			array.append(item.expected)

		return array

	def __repr__(self):
		return f'Sample data {self.items}'

