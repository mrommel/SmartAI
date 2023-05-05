import numpy as np

from network import Network, FCLayer, ActivationLayer, tanh, tanh_prime, mse_prime, mse

# https://towardsdatascience.com/math-neural-network-from-scratch-in-python-d6da9f29ce65
if __name__ == "__main__":
	# training data
	x_train = np.array([[[0.1, 0.5]], [[0.7, 0.2]], [[0, 0]], [[0.1, 0.1]]])
	y_train = np.array([[[0.6]], [[0.9]], [[0]], [[0.2]]])

	x_test = np.array([[[0.1, 0.3]], [[0.0, 0.1]], [[0.5, 0.4]], [[0.0, 1.0]]])
	y_test = np.array([[[0.4]], [[0.1]], [[0.9]], [[1.0]]])

	# network
	net = Network()
	net.add(FCLayer(2, 8))
	net.add(ActivationLayer(tanh, tanh_prime))
	net.add(FCLayer(8, 1))
	net.add(ActivationLayer(tanh, tanh_prime))

	# train
	net.use(mse, mse_prime)
	net.train(x_train, y_train, epochs=1000, learning_rate=0.1)

	# test
	out = net.predict(x_test[0:4])
	print("\n")
	print("predicted values : ")
	print(out, end="\n")
	print("true values : ")
	print(y_test[0:4])
