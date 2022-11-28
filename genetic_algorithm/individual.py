# coding: utf-8
"""
Individual class
"""
import random


class Individual(object):
	"""
		Manage an individual
	"""

	def __init__(self, length=64, bitstring_or_list=None):
		"""
			Initialize a new Individual
		"""
		self._fitness = 0
		self.repr = None
		self.default_length = length
		if not bitstring_or_list:
			# random array of bytes
			self.genes = [random.getrandbits(1) for _ in range(self.default_length)]
		else:
			if isinstance(bitstring_or_list, str):
				self.genes = [int(b) for b in bitstring_or_list]
			elif isinstance(bitstring_or_list, list):
				self.genes = bitstring_or_list

	@property
	def gene(self, idx):
		"""
			Return gene at index idx
		"""
		return self.genes[idx]

	@gene.setter
	def gene(self, idx, value):
		"""
			Set a new gene at index idx
		"""
		self.genes[idx] = value

	@property
	def size(self):
		"""
			Return gene length
		"""
		return len(self.genes)

	def __repr__(self):
		return ''.join([str(b) for b in self.genes])
