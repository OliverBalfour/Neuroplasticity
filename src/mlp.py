
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop

batch_size = 128
epochs = 20

def run (dataset, layers, dropout):
	(x_train, y_train), (x_test, y_test), dim, num_classes, max_features = dataset

	model = Sequential()
	model.add(Dense(layers[0], activation='relu', input_dim=dim))
	if dropout:
		model.add(Dropout(0.2))
	for i in range(1, len(layers)):
		model.add(Dense(layers[i], activation='relu'))
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
