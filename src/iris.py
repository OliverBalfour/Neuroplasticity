
import random
import numpy as np

def onehot (len, n):
	arr = np.zeros(len)
	arr[n] = 1
	return arr

def load ():

	lines = [line.rstrip('\n') for line in open('iris-data.txt')]
	random.shuffle(lines)

	enum = {
		"Iris-setosa": 0,
		"Iris-versicolor": 1,
		"Iris-virginica": 2
	}

	for i in range(len(lines)):
		lines[i] = lines[i].split(',')
		lines[i] = (
			lines[i][:-1],
			onehot(3, enum[lines[i][-1]])
		)
		for j in range(len(lines[i][0])):
			lines[i][0][j] = float(lines[i][0][j])

	split = int(round(len(lines) / 4 * 3))

	x_train = np.array(list(map(lambda l: l[0], lines[:split])))
	y_train = np.array(list(map(lambda l: l[1], lines[:split])))
	x_test = np.array(list(map(lambda l: l[0], lines[split:])))
	y_test = np.array(list(map(lambda l: l[1], lines[split:])))

	dim = len(x_train[0])

	return (((x_train, y_train), (x_test, y_test), dim, 3, dim))
