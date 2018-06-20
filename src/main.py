
import mnist
import imdb
import wdbc
import iris

datasets = [{
	"name": "MNIST",
	"data": mnist.load()
}, {
	"name": "IMDb",
	"data": imdb.load()
}, {
	"name": "WDBC",
	"data": wdbc.load()
}, {
	"name": "Iris",
	"data": iris.load()
}]

import mlp
import ann
import rnn

models = [
	{
		"name": "ANN 32",
		"run": ann.run,
		"layers": (32,),
	}, {
		"name": "ANN 256",
		"run": ann.run,
		"layers": (256,),
	}, {
		"name": "ANN 2·256",
		"run": ann.run,
		"layers": (256,256),
	}, {
		"name": "ANN 2·512",
		"run": ann.run,
		"layers": (512,512),
	}, {
		"name": "MLP 32",
		"run": mlp.run,
		"layers": (32,),
	}, {
		"name": "MLP 256",
		"run": mlp.run,
		"layers": (256,),
	}, {
		"name": "MLP 2·256",
		"run": mlp.run,
		"layers": (256,256),
	}, {
		"name": "MLP 2·512",
		"run": mlp.run,
		"layers": (512,512),
	}, {
		"name": "RNN 32",
		"run": rnn.run,
		"layers": (32,),
	}, {
		"name": "RNN 128",
		"run": rnn.run,
		"layers": (128,),
	}
]

results = []
for model in models:
	print('Starting experimentation for model ' + model["name"])

	for dataset in datasets:
		print('Training ' + model["name"] + ' on ' + dataset["name"])
		cont = input('Continue? (y/n): ')
		if cont == 'y':
			for i in range(2):
				res = model["run"](dataset["data"], model["layers"], i == 1);
				results.append({
					"model": model["name"] + ('-D' if i == 1 else ''),
					"dataset": dataset["name"],
					"results": res
				})

	print('Ending experimentation for model ' + model["name"])

print('\nResults:')
for result in results:
	print('\tmodel: ' + result["model"] + '\tdataset: ' + result["dataset"] + '\taccuracy: ' + str(result["results"]["acc"]))
print('\n')
