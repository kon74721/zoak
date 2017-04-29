var HtmlPlugin = require("html-webpack-plugin");

module.exports = {
    entry: "./src/index.js",
    output: {
        path: "./build",
        filename: "bundle.js",
        sourcePrefix: ""
    },
    plugins: [
        new HtmlPlugin({
            template: "./src/index.html",
            inject: "body"
        })
    ],
    devServer: {
        contentBase: "./build"
    },
    module: {
        unknownContextCritical: false,
        loaders: [
            { test: /\.css$/, loader: "style!css" },
            {
                test: /\.(png|gif|jpg|jpeg)$/,
                loader: "file-loader"
            },
            { test: /Cesium\.js$/, loader: "script" }
        ]
    }
};
