import math
from enum import Enum

from genetic_algorithm.utils import bin2float, bin2int


class FunctionType(Enum):
	Number = 0
	Variable = 1
	Sum = 2
	Subtract = 3
	Multiplication = 4
	Divide = 5
	Sinus = 6
	Pow = 7
	Absolute = 8


def convert_int_to_function_type(int_value):
	try:
		function_type_from_int = FunctionType(int_value % len(FunctionType))
		return function_type_from_int
	except:
		return None


class WrongLengthException(Exception):
	def __init__(self, length):
		self.length = length

	def __repr__(self):
		return f'WrongLengthException: should be dividable by 68 but {self.length} is not'


class FunctionTree:

	def __init__(self, binary_representation: str, var_names=[]):
		if len(binary_representation) % 68 != 0:
			raise WrongLengthException(len(binary_representation))

		if len(binary_representation) == 68:
			self.function_type = convert_int_to_function_type(bin2int(binary_representation[0:4]))

			# if part is node then it must be Number or Variable
			if self.function_type not in [FunctionType.Number, FunctionType.Variable]:
				# raise Exception(f'wrong type: {self.function_type}')
				self.function_type = FunctionType.Number

			if self.function_type == FunctionType.Number:
				self.value = bin2float(binary_representation[-64:])
				self.variable_name = None

			if self.function_type == FunctionType.Variable:
				var_index = bin2int(binary_representation[-64:]) % len(var_names)
				self.value = None
				self.variable_name = var_names[var_index]

			self.left = None
			self.right = None
		else:
			# first 68 chars is the function
			self.function_type = convert_int_to_function_type(bin2int(binary_representation[0:4]))

			# not filled
			if self.function_type is None:
				raise Exception(f'wrong type: {binary_representation[0:4]}')

			# if part is node then it must NOT be Number or Variable
			if self.function_type in [FunctionType.Number, FunctionType.Variable]:
				# raise Exception(f'wrong type: {self.function_type}')
				self.function_type = FunctionType.Sum

			self.value = None
			self.variable_name = None

			# next 50% / last 50%
			remainder = len(binary_representation) - 68
			rest = binary_representation[-remainder:]
			size = int(len(rest) / 2)
			left_binary_representation = rest[0:size]
			right_binary_representation = rest[-size:]

			self.left = FunctionTree(left_binary_representation, var_names=var_names)
			self.right = FunctionTree(right_binary_representation, var_names=var_names)

	def valid(self) -> bool:
		if self.function_type is None:
			return False

		if self.function_type == FunctionType.Number and self.value is None:
			return False

		if self.function_type == FunctionType.Variable and self.variable_name is None:
			return False

		if self.function_type not in [FunctionType.Number, FunctionType.Variable]:
			if self.left is None or self.right is None:
				return False

		return True

	def as_function(self) -> str:
		if not self.valid():
			return '<not valid>'

		if self.function_type == FunctionType.Number:
			return f'{self.value:.4}'

		if self.function_type == FunctionType.Variable:
			return self.variable_name

		if self.function_type == FunctionType.Sum:
			return f'({self.left.as_function()} + {self.right.as_function()})'

		if self.function_type == FunctionType.Subtract:
			return f'({self.left.as_function()} - {self.right.as_function()})'

		if self.function_type == FunctionType.Multiplication:
			return f'({self.left.as_function()} * {self.right.as_function()})'

		if self.function_type == FunctionType.Divide:
			return f'({self.left.as_function()} / {self.right.as_function()})'

		if self.function_type == FunctionType.Sinus:
			return f'sin({self.left.as_function()})'

		if self.function_type == FunctionType.Pow:
			return f'({self.left.as_function()} ^ {self.right.as_function()})'

		if self.function_type == FunctionType.Absolute:
			return f'|{self.left.as_function()}|'

		raise Exception(f'not handled: {self.function_type}')

	def evaluate(self, values: dict) -> float:
		if self.function_type == FunctionType.Number:
			return self.value

		if self.function_type == FunctionType.Variable:
			return values[self.variable_name]

		left_val = self.left.evaluate(values)
		right_val = self.right.evaluate(values)

		if self.function_type == FunctionType.Sum:
			return left_val + right_val

		if self.function_type == FunctionType.Subtract:
			return left_val - right_val

		if self.function_type == FunctionType.Multiplication:
			return left_val * right_val

		if self.function_type == FunctionType.Divide:
			if right_val == 0.0:
				return math.nan

			return left_val / right_val

		if self.function_type == FunctionType.Sinus:
			if left_val == math.inf or left_val == -math.inf:
				return 0.0
			if isinstance(left_val, complex):
				return 0.0
			return math.sin(left_val)

		if self.function_type == FunctionType.Pow:
			try:
				tmp_val = pow(left_val, right_val)
				if isinstance(tmp_val, complex):
					return 0.0
				return tmp_val
			except:
				return 0.0

		if self.function_type == FunctionType.Absolute:
			return math.fabs(left_val)

		raise Exception(f'not handled: {self.function_type}')
