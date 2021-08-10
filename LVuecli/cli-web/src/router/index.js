import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'IndexPage',
    component: () => import('../components/IndexPage.vue'),
    children: [
      {
        // 当 /trade 匹配成功，
        // trade 会被渲染在 Index 的 <router-view> 中
        path: '',
        name: 'trade',
        component: () => import('../components/trade.vue')
      },
      {
          path: '/quotations',
          name: 'quotations',
          component: () => import('../components/quotations.vue')
      },
      {
          path: '/banc',
          name: 'banc',
          component: () => import('../components/banc.vue')
      },
      {
          path: '/my',
          name: 'my',
          component: () => import('../components/my.vue')
      },
    ]
  },
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
