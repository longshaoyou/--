module.exports = {
  lintOnSave: false,
  devServer: {
    open: true,
    port: 8080,
    proxy: {
      // "/api": {
      //   target: "http://127.0.0.1:8899",
      //   ws: true,
      //   changeOrigin: true,
      //   pathRewrite: {
      //     "^/api": "",
      //   },
      // },
      // "/files": {
      //   target: "http://127.0.0.1/files",
      //   ws: true,
      //   changeOrigin: true,
      // },
    },
  },
};