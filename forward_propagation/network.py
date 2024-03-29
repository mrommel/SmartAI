import numpy as np

# activation function and its derivative
def tanh(x):
	return np.tanh(x)

def tanh_prime(x):
	return 1-np.tanh(x)**2

# loss function and its derivative
def mse(y_true, y_pred):
	return np.mean(np.power(y_true-y_pred, 2))

def mse_prime(y_true, y_pred):
	return 2*(y_pred-y_true)/y_true.size

class Layer:
	"""Base class"""
	def __init__(self):
		self.input = None
		self.output = None

	def forward_propagation(self, input):
		"""computes the output Y of a layer for a given input X"""
		raise NotImplementedError

	def backward_propagation(self, output_error, learning_rate):
		"""computes dE/dX for a given dE/dY (and update parameters if any)"""
		raise NotImplementedError


class FCLayer(Layer):
	"""inherit from base class Layer"""
	def __init__(self, input_size, output_size):
		"""
			@param input_size: number of input neurons
			@param output_size: number of output neurons
		"""
		super().__init__()
		self.weights = np.random.rand(input_size, output_size) - 0.5
		self.bias = np.random.rand(1, output_size) - 0.5

	def forward_propagation(self, input_data):
		"""returns output for a given input"""
		self.input = input_data
		self.output = np.dot(self.input, self.weights) + self.bias
		return self.output

	def backward_propagation(self, output_error, learning_rate):
		"""computes dE/dW, dE/dB for a given output_error=dE/dY. Returns input_error=dE/dX."""
		input_error = np.dot(output_error, self.weights.T)
		weights_error = np.dot(self.input.T, output_error)
		# dBias = output_error

		# update parameters
		self.weights -= learning_rate * weights_error
		self.bias -= learning_rate * output_error
		return input_error


class ActivationLayer(Layer):
	"""inherit from base class Layer"""
	def __init__(self, activation, activation_prime):
		super().__init__()
		self.activation = activation
		self.activation_prime = activation_prime

	def forward_propagation(self, input_data):
		"""returns the activated input"""
		self.input = input_data
		self.output = self.activation(self.input)
		return self.output

	def backward_propagation(self, output_error, learning_rate):
		"""
			Returns input_error=dE/dX for a given output_error=dE/dY.
			learning_rate is not used because there is no "learnable" parameters.
		"""
		return self.activation_prime(self.input) * output_error


class Network:
	def __init__(self):
		self.layers = []
		self.loss = None
		self.loss_prime = None

	def add(self, layer):
		"""add layer to network"""
		self.layers.append(layer)

	def use(self, loss, loss_prime):
		"""set loss to use"""
		self.loss = loss
		self.loss_prime = loss_prime

	def predict(self, input_data):
		"""predict output for given input"""
		# sample dimension first
		samples = len(input_data)
		result = []

		# run network over all samples
		for i in range(samples):
			# forward propagation
			output = input_data[i]
			for layer in self.layers:
				output = layer.forward_propagation(output)
			result.append(output)

		return result

	def train(self, x_train, y_train, epochs, learning_rate):
		"""train the network"""
		# sample dimension first
		samples = len(x_train)

		# training loop
		for i in range(epochs):
			err = 0
			for j in range(samples):
				# forward propagation
				output = x_train[j]
				for layer in self.layers:
					output = layer.forward_propagation(output)

				# compute loss (for display purpose only)
				err += self.loss(y_train[j], output)

				# backward propagation
				error = self.loss_prime(y_train[j], output)
				for layer in reversed(self.layers):
					error = layer.backward_propagation(error, learning_rate)

			# calculate average error on all samples
			err /= samples
			print('epoch %d/%d   error=%f' % (i+1, epochs, err))