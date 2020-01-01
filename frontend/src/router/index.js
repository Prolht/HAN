import Vue from 'vue'
import Router from 'vue-router'
import IndexPage from '@/pages/IndexPage'
import SearchPage from '@/pages/SearchPage'
import SinglePage from '@/pages/SinglePage'
import ListPage from '@/pages/ListPage'
// import CecLabelPage from '@/pages/LabelPage/CecLabelPage'
import PageNotFound from '@/pages/PageNotFound'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Index',
      component: IndexPage
    },
    {
      path: '/search',
      name: 'Search',
      component: SearchPage
    },
    {
      path: '/characters/:',
      name: 'SinglePage', // 单个汉字 复用search接口
      component: SinglePage,
    },
    {
      path: '/list',
      name: 'ListPage',
      component: ListPage,
    },
    {
      path: '*',
      name: 'PageNotFound',
      component: PageNotFound,
    },
  ],
  scrollBehavior (to, from, savedPosition) {
    return { x: 0, y: 0 }
  },
})

export default router
