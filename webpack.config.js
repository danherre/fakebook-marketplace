const path = require('path');

module.exports = {
  mode: 'development',
  entry: './fbmarketplace/js/main.jsx',
  output: {
    path: path.join(__dirname, '/fbmarketplace/static/js/'),
    filename: 'bundle.js',
  },
  module: {
    rules: [
      {
        // Test for js or jsx files
        test: /\.jsx?$/,
        loader: 'babel-loader',
        options: {
          presets: ['@babel/preset-env', '@babel/preset-react'],
        },
      },
    ],
  },
  resolve: {
    extensions: ['.js', '.jsx'],
  },
};
