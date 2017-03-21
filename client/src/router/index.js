import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Inbox from '@/components/Inbox'
import Projects from '@/components/Projects'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {
          path: '/',
          name: 'Hello',
          component: Home
        },
        {
            path: '/inbox',
            name: 'Inbox',
            component: Inbox
        },  
        {
            path: '/projects',
            name: 'Projects',
            component: Projects
        } 
    ]
})
