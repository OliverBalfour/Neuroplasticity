
from keras.models import Sequential
from keras.layers import Dense, Embedding, MaxPooling1D
from keras.layers import LSTM

def run (dataset, layers, dropout):
	(x_train, y_train), (x_test, y_test), dim, num_classes, max_features = dataset
	batch_size = 32
	epochs = 8

	dropout = 0.2 if dropout else 0

	model = Sequential()

	model.add(Embedding(max_features, 128))

	# if mnist, use 1D max pooling to nontuple speed at the expense of performance
	# and only use 2 epochs (RNN training on MNIST is reaaally slow...)
	if dim == 784:
		model.add(MaxPooling1D(pool_size=3, padding='valid'))
		epochs = 2

	for i in range(len(layers)):
		model.add(LSTM(layers[i], dropout=dropout, recurrent_dropout=dropout))
	model.add(Dense(num_classes, activation='sigmoid'))

	model.summary()

	model.compile(
		loss='binary_crossentropy',
		optimizer='adam',
		metrics=['accuracy']
	)

	model.fit(
		x_train, y_train,
		batch_size=batch_size,
		epochs=8,
		validation_data=(x_test, y_test)
	)
	score = model.evaluate(
		x_test, y_test,
		batch_size=batch_size
	)

	return { "acc": score[1], "score": score[0] }
