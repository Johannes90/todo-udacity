import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Inbox from '@/components/Inbox'
import Projects from '@/components/Projects'
import ProjectView from '@/components/project/ProjectView'
import Register from '@/components/Register'
import Login from '@/components/Login'
import store from '../store/store';

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
            component: Inbox,
            beforeEnter: (to, from, next) => {
                if(store.getters.isLoggedIn) {
                    next();
                } else {
                    next('/login');
                }
            }
        },
        {
            path: '/register',
            name: 'Register',
            component: Register
        },
        {
            path: '/login',
            name: 'login',
            component: Login
        },    
        {
            path: '/project',
            name: 'Project',
            component: Projects,
            children: [
                {path:':id', component: ProjectView}
            ],
            beforeEnter: (to, from, next) => {
                if(store.getters.isLoggedIn) {
                    next();
                } else {
                    next('/login');
                }
            }
        } 
    ]
})
