const path = require('path');

module.exports = {
	root: path.resolve(__dirname, '../'),
	outputPath: path.resolve(__dirname, '../', 'build'),
	entryPath: path.resolve(__dirname, '../', 'src/index.jsx'),

	appPath: path.resolve(__dirname, '../app'),
	eslintPath: path.resolve(__dirname, '../.eslintrc.js')
};
