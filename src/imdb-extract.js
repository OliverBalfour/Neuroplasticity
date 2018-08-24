
// Usage:
// node imdb-extract.js /path/to/aclImdb/test/neg/ imdb-neg.txt
// node imdb-extract.js /path/to/aclImdb/test/pos/ imdb-pos.txt
// (you will need to download the IMDb review dataset linked in the paper and extract it first)

const fs = require('fs');
const path = require('path');

const count = 500;
let compiled = [],
	c = 0;

fs.readdirSync(process.argv[2]).filter((el, i) => i < count).forEach(file => {
	const name = path.join(process.argv[2], file);
	fs.readFile(name, (err, data) => {
		if (err) throw err;
		compiled.push(data.toString().replace(/\n/g, ' ').replace(/<br \/>/g, ' '));
		c++;
		if (c === count) {
			fs.writeFile(path.join(__dirname, process.argv[3]), compiled.join('\n'), err => {
				if (err) throw err;
				console.log('Done');
			});
		}
	});
});
