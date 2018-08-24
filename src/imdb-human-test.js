
// Usage:
// node imdb-human-test.js
// (run imdb-extract.js for both classes first)

const fs = require('fs');
const path = require('path');
const readline = require('readline');

const prompt = readline.createInterface(process.stdin, process.stdout);

const read = name => {
	return fs.readFileSync(path.join(__dirname, name)).toString();
}

let questions = {
	n: read('imdb-neg.txt').split('\n'),
	p: read('imdb-pos.txt').split('\n')
}

let iterations = 0,
	score = 0;

let text = '',
	classification = '';

console.log('Type p for positive, n for negative sentiment')

function chooseQuestion () {
	classification = Math.random() < 0.5 ? 'p' : 'n';
	// assumes pos and neg are equal length
	text = questions[classification][Math.floor(Math.random() * questions.p.length)];
}
chooseQuestion();
console.log(text);

prompt.setPrompt('p/n: ');
prompt.prompt();
prompt.on('line', answer => {
	iterations++;
	if (answer === classification) {
		score++;
		console.log(`Correct. Score: ${score}/${iterations}. Acc: ${score/iterations}\n`)
	} else {
		console.log(`Incorrect. Score: ${score}/${iterations}. Acc: ${score/iterations}\n`)
	}
	chooseQuestion();
	console.log(text);
	prompt.prompt();
}).on('close', () => process.exit(0));
