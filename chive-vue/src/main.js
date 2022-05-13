import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import Router from 'vue-router'

Vue.use(Router)

// 设置反向代理，前端请求默认发送到 http://localhost:4321/api
// var axios = require('axios')

// 全局注册，之后可在其他组件中通过 this.$axios 发送数据
Vue.prototype.$axios = axios
Vue.config.productionTip = false

// axios.defaults.baseURL = 'http://localhost:8080/'
axios.defaults.baseURL = '/api'

const app = new Vue({
  router: router,
  render: h => h(App),
  methods: {
    getApp () {
      return this.$children[0]
    }
  }
}).$mount('#app')
window.g_app = app.getApp()

// new Vue({
//   el: '#app',
//   router,
//   components: { App },
//   template: '<App/>',
//   methods: {
//     getApp () {
//       return this.$children[0]
//     }
//   }
// })
