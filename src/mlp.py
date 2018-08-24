
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
from keras.layers import Activation
from keras import backend as K
from keras.utils.generic_utils import get_custom_objects

batch_size = 128
epochs = 20

def heaviside(x):
	x = x * 1000
	zero = tf.convert_to_tensor(0., dtype=x.dtype.base_dtype)
	one = tf.convert_to_tensor(1., dtype=x.dtype.base_dtype)
	x = tf.clip_by_value(x, zero, one)
	return x

get_custom_objects().update({'heaviside': Activation(heaviside)})

def run (dataset, layers, dropout):
	(x_train, y_train), (x_test, y_test), dim, num_classes, max_features = dataset

	model = Sequential()
	model.add(Dense(layers[0], input_dim=dim))
	model.add(Activation(heaviside))
	if dropout:
		model.add(Dropout(0.2))
	for i in range(1, len(layers)):
		model.add(Dense(layers[i]))
		model.add(Activation(heaviside))
		if dropout:
			model.add(Dropout(0.2))
	model.add(Dense(num_classes, activation='softmax'))

	model.summary()

	model.compile(
		loss='binary_crossentropy',
		optimizer=RMSprop(),
		metrics=['accuracy']
	)

	history = model.fit(
		x_train, y_train,
		batch_size=batch_size,
		epochs=epochs,
		verbose=1,
		validation_data=(x_test, y_test)
	)

	score = model.evaluate(x_test, y_test, verbose=0)
	print('Test loss:', score[0])
	print('Test accuracy:', score[1])
	return { "acc": score[1], "score": score[0] }
