import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/components/Home'
import About from '@/components/About'
import Upload from '@/components/Upload'
import CannyFile from '@/components/CannyFile'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/about',
      name: 'About',
      component: About
    },
    {
      path: '/upload',
      name: 'Upload',
      component: Upload
    },
    {
      path: '/cannyFile',
      name: 'CannyFile',
      component: CannyFile
    }
  ]
})
