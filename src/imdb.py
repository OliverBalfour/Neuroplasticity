
from keras.datasets import imdb
from keras.preprocessing import sequence

def load ():
	max_features = 20000
	maxlen = 80  # cut texts after this number of words (among top max_features most common words)

	(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)

	x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
	x_test = sequence.pad_sequences(x_test, maxlen=maxlen)

	return (((x_train, y_train), (x_test, y_test), maxlen, 1, max_features))
