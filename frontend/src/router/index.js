import Vue from 'vue'
import Router from 'vue-router'
import IndexPage from '@/pages/IndexPage'
import SearchPage from '@/pages/SearchPage'
import SinglePage from '@/pages/SinglePage'
import ListPage from '@/pages/ListPage'
import EditPage from '@/pages/EditPage'
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
      path: '/character',
      name: 'SinglePage',
      component: SinglePage,
    },
    {
      path: '/list',
      name: 'ListPage',
      component: ListPage,
    },
    {
      path: '/edit',
      name: 'EditPage',
      component: EditPage,
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
