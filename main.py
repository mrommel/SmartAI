import math
import random
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

from genetic_algorithm.data import SampleData
from genetic_algorithm.gene_function import GeneFunction
from genetic_algorithm.genetic_algorithm import GeneticAlgorithm

"""
	prepare data
"""
random.seed(datetime.now().timestamp())

data = SampleData()

# x * y
# best formula found: ((-2.03e-08 ^ -1.519e+254) + (x * y)) + (sin(1.74e-15) - (1.515e-168 + 1.167e-245))
# -2.03e-08 ^ -1.519e+254 => 0.0 (inf is evaluated to zero)
# (sin(1.74e-15) - (1.515e-168 + 1.167e-245)) => 0.0
data.add_values(values={'x': 4.0, 'y': 3.0}, expected=12.0)
data.add_values(values={'x': 27.0, 'y': 2.0}, expected=54.0)
data.add_values(values={'x': 1.0, 'y': 18.0}, expected=18.0)
data.add_values(values={'x': 5.0, 'y': 10.0}, expected=50.0)
data.add_values(values={'x': 12.0, 'y': 4.5}, expected=54.0)
data.add_values(values={'x': 1.5, 'y': 4.5}, expected=6.75)
data.add_values(values={'x': 25.4, 'y': 5.0}, expected=127.0)
data.add_values(values={'x': 20.0, 'y': 17.5}, expected=350.0)

# x * sin(y) + 0.5
# best formula found: (sin((-6.012e-248 + -4.833e+148)) + (sin(y) * |x|))
# sin((-6.012e-248 + -4.833e+148)) => 0.48779520519
# data.add_values(values={'x': 4.0, 'y': 3.0}, expected=1.06448003223947)
# data.add_values(values={'x': 27.0, 'y': 2.0}, expected=25.0510305242934)
# data.add_values(values={'x': 1.0, 'y': 18.0}, expected=-0.250987246771676)
# data.add_values(values={'x': 5.0, 'y': 10.0}, expected=-2.22010555444685)
# data.add_values(values={'x': 12.0, 'y': 4.5}, expected=-11.2303614119812)
# data.add_values(values={'x': 1.5, 'y': 4.5}, expected=-0.966295176497646)
# data.add_values(values={'x': 25.4, 'y': 5.0}, expected=-23.8566765764437)
# data.add_values(values={'x': 20.0, 'y': 17.5}, expected=-19.0125201093632)

var_names = ['x', 'y']


def gene_str(gene):
	return '1' if gene else '0'


def tree_function(genome):
	binary_str = ''.join(list(map(gene_str, genome)))
	return GeneFunction(length=len(binary_str), bitstring_or_list=binary_str, var_names=var_names)


# define function that will be used to evaluate the fitness
def fitness_function(genome):
	tree = tree_function(genome)
	error_val = tree.error_for_data(data)
	if error_val == 0.0:
		return 0.0

	tmp_val = 1.0 / error_val  # this defines the fitness: 1/error

	if isinstance(tmp_val, complex):
		return 0.0

	if math.isnan(tmp_val):
		return 0.0

	return tmp_val


# get formula from genome
def formula_function(genome):
	return tree_function(genome).gene_as_formula()


if __name__ == "__main__":
	# Configure the algorithm:
	population_size = 25
	genome_length = 1 * 68 + 2 * 68 + 4 * 68 + 8 * 68
	ga = GeneticAlgorithm(fitness_function)
	ga.generate_binary_population(size=population_size, genome_length=genome_length)
	# How many pairs of individuals should be picked to mate
	ga.number_of_pairs = 5
	# Selective pressure from interval [1.0, 2.0]
	# the lower value, the less will the fitness play role
	ga.selective_pressure = 1.6
	# mutation rate: 10%
	ga.mutation_rate = 0.1
	# If two parents have the same genotype, ignore them and generate TWO random parents
	# This helps to prevent premature convergence
	ga.allow_random_parent = True  # default True
	# Use single point crossover instead of uniform crossover
	ga.single_point_cross_over = False  # default False

	# Run 1000 iteration of the algorithm
	# You can call the method several times and adjust some parameters
	# (e.g. number_of_pairs, selective_pressure, mutation_rate,
	# allow_random_parent, single_point_cross_over)
	ga.run(1000)

	best_genome, best_fitness = ga.get_best_genome()
	best_function = tree_function(best_genome)

	print(f'best formula: {formula_function(best_genome)}')
	print(f'best fitness: {best_fitness}')

	# If you want, you can have a look at the population:
	# population = ga.population
	# and the fitness of each element:
	fitness_vector = ga.get_fitness_vector()
	# print(fitness_vector)

	fig = plt.figure()

	# syntax for 3-D projection
	ax = plt.axes(projection='3d')

	# Creating color map
	cmap = plt.get_cmap('hot')

	sx = np.outer(np.linspace(0, 25, 25), np.ones(25))
	sy = sx.copy().T  # transpose
	sz = np.arange(25 * 25).reshape(25, 25)  # create an array and form it into matrix

	for ix in range(0, 25):
		for iy in range(0, 25):
			vals = {'x': float(ix), 'y': float(iy)}
			tmp_z = best_function.function_tree.evaluate(vals)
			sz[ix, iy] = tmp_z

	# Creating plot
	surf = ax.plot_surface(sx, sy, sz, rstride=1, cstride=1, alpha=0.8, cmap=cmap)

	# defining axes
	z = data.expected_values()
	x = data.values('x')
	y = data.values('y')
	ax.scatter(x, y, z)
	ax.set_xlabel('X-axis')
	ax.set_xlim(0, 25)
	ax.set_ylabel('Y-axis')
	ax.set_ylim(0, 25)
	ax.set_zlabel('Z-axis')

	# syntax for plotting
	ax.set_title('3d Scatter plot of given values and approx surface')
	plt.show()
