import Vue from 'vue'
import Router from 'vue-router'

import Admin from './components/Admin'
import TestAdmin from './components/TestAdmin'
import Login from './components/Login'
import HelloWorld from './components/HelloWorld'
// import Kchart from './components/Kchart'

Vue.use(Router)

export default new Router({
  mode: 'history', // remove hash flag '#' in URL, Hash is a default vue-router mode setting
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    // {
    //   path: '/kchart',
    //   name: 'Kchart',
    //   component: Kchart
    // },
    {
      path: '/testadmin',
      name: 'TestAdmin',
      component: TestAdmin
    },
    {
      path: '/admin',
      name: 'Admin',
      component: Admin
    }
  ]
})
