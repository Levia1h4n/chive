import Vue from 'vue'
import Router from 'vue-router'
import AppIndex from '@/components/home/AppIndex'
import Login from '@/components/Login'
// import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
  // mode: 'history', // remove hash flag '#' in URL, Hash is a default vue-router mode setting
  routes: [
    // {
    //   path: '/',
    //   name: 'HelloWorld',
    //   component: HelloWorld
    // }
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/index',
      name: 'AppIndex',
      component: AppIndex
    }
  ]
})
