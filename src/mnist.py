
import keras
from keras.datasets import mnist

def load ():

	# the data, split between train and test sets
	(x_train, y_train), (x_test, y_test) = mnist.load_data()
	dim = 28**2
	num_classes = 10

	x_train = x_train.reshape(60000, dim)
	x_test = x_test.reshape(10000, dim)
	x_train = x_train.astype('float32')
	x_test = x_test.astype('float32')
	x_train /= 255
	x_test /= 255

	# convert class vectors to binary class matrices
	y_train = keras.utils.to_categorical(y_train, num_classes)
	y_test = keras.utils.to_categorical(y_test, num_classes)

	return (((x_train, y_train), (x_test, y_test), dim, num_classes, dim))
