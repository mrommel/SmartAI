# SmartAI

Python project to demonstrate the use of generic networks / AI to approximate a function / formula.

## Sample

Given x and y with a couple of values and a hidden mathematical relation: x * y

```
data = SampleData()
data.add_values(values={'x': 4.0, 'y': 3.0}, expected=12.0)
data.add_values(values={'x': 27.0, 'y': 2.0}, expected=54.0)
data.add_values(values={'x': 1.0, 'y': 18.0}, expected=18.0)
data.add_values(values={'x': 5.0, 'y': 10.0}, expected=50.0)
data.add_values(values={'x': 12.0, 'y': 4.5}, expected=54.0)
data.add_values(values={'x': 1.5, 'y': 4.5}, expected=6.75)
data.add_values(values={'x': 25.4, 'y': 5.0}, expected=127.0)
data.add_values(values={'x': 20.0, 'y': 17.5}, expected=350.0)
```

Then the genetic network is created:

```
# Configure the algorithm:
population_size = 25
genome_length = 1 * 68 + 2 * 68 + 4 * 68 + 8 * 68
ga = GeneticAlgorithm(fitness_function)
ga.generate_binary_population(size=population_size, genome_length=genome_length)
```

Please note that the size of each gene is 68 (4 for the type and 64 for the value). 
Since the function is built from a binary tree, each level has twice the number of genes:
1 + 2 + 4 + 8 + ... x 68 genes.

When the network is running for 1000 iterations.

```
# Run 1000 iteration of the algorithm
# You can call the method several times and adjust some parameters
# (e.g. number_of_pairs, selective_pressure, mutation_rate,
# allow_random_parent, single_point_cross_over)
ga.run(1000)
```

The best genome is very likely to return the mathematical relationship:

```
best_genome, best_fitness = ga.get_best_genome()
best_function = tree_function(best_genome)

print(f'best formula: {formula_function(best_genome)}')
print(f'best fitness: {best_fitness}')
```

![best gene function](https://github.com/mrommel/SmartAI/blob/main/screenshots/best_fitness.png?raw=true)

One could even create a diagram:

![diagram](https://github.com/mrommel/SmartAI/blob/main/screenshots/figure.png?raw=true)


## Links

* https://github.com/bosr/ga-tut/blob/master/driver.py
* https://www.geeksforgeeks.org/binarytree-module-in-python/
* https://github.com/chovanecm/python-genetic-algorithm