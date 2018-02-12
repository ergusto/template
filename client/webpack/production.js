var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

var config = require('./base.js');

config.output.path = path.resolve('./static/dist/');

config.module.rules = config.module.rules.concat([{
	test: /\.jsx?$/,
	use: [{
		loader: 'babel-loader',
		options: {
			presets: ['es2015', 'stage-0', 'react']
		}
	}]
}]);

config.plugins = config.plugins.concat([
	new BundleTracker({ filename: './client/webpack/stats.production.json' }),

	new webpack.DefinePlugin({
		'process.env': {
			NODE_ENV: JSON.stringify('production')
		}
	}),

	new webpack.optimize.UglifyJsPlugin({
		compressor: {
			warnings: false
		}
	})
]);

module.exports = config;
