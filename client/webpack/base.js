const paths = require('./paths.js');

module.exports = {
	context: paths.root,
	entry: paths.entryPath,
	output: {
		path: paths.outputPath,
		filename: '[name]-[hash].js'
	},
	resolve: {
		modules: ['src','node_modules'],
		extensions: ['*','.js','.jsx','.css','.scss'],
		alias: {
			app: paths.appPath
		}
	},
	plugins: [],
	module: {
		rules: [{
			test: /\.(js|jsx)$/,
			loader: 'babel-loader',
			exclude:  /(node_modules)/
		},
		{
			test: /\.(woff2|ttf|woff|eot)$/,
			use: [
				{
					loader: 'file-loader'
				}
			]
		}]
	}
};
