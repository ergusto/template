const webpack = require('webpack'),
	BundleTracker = require('webpack-bundle-tracker'),
	config = require('./base.js'),
	paths = require('./paths.js');

config.entry = [
	'react-hot-loader/patch',
	'webpack-dev-server/client?http://localhost:3000',
	'webpack/hot/only-dev-server',

	paths.appPath
];

config.output.publicPath = 'http://localhost:3000/static/build';

config.devtool = 'inline-source-map';

config.module.rules = config.module.rules.concat([
	{
		test: /\.jsx?$/,
		include: paths.appPath,
		use: ['react-hot-loader/webpack', 'babel-loader']
	},
	{
		test: /\.(css|scss)$/,
		use: [
			'style-loader',
			{
				loader: 'css-loader',
				options: {
					sourceMap: true,
					localsConvention: 'camelCase',
					modules: {
						localIdentName: '[local]___[hash:base64:5]',
					}
				}
			},
			'sass-loader'
		]
	}
]);

config.plugins = config.plugins.concat([
	new webpack.HotModuleReplacementPlugin(),
	new webpack.NamedModulesPlugin(),
	new webpack.NoEmitOnErrorsPlugin(),
	new BundleTracker({ filename: './client/webpack/stats/local.json' }),
]);

config.devServer = {
	host: '0.0.0.0', 
	port: 3000,
	historyApiFallback: true,
	headers: {
		"Access-Control-Allow-Origin": "*",
		"Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
		"Access-Control-Allow-Headers": "X-Requested-With, content-type, Authorization"
	},
	compress: true,
	hot: true
};

module.exports = config;
