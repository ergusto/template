var path = require('path');

module.exports = {
	context: path.resolve(__dirname, '..'),
	entry: '../app',
	output: {
		path: path.resolve('./static/build/'),
		filename: '[name]-[hash].js'
	},
	resolve: {
		alias: {
			app: path.resolve(__dirname, '../app')
		}
	},
	plugins: [],
	module: {
		rules: [{
			test: /\.scss$/,
			use: ['style-loader', 'css-loader', 'sass-loader']
		}]
	}
};
