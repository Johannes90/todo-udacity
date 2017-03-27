import Vue from 'vue';
import Vuex from 'vuex';

import todos from './modules/todo';
import projects from './modules/project'

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        todos,
        projects
    }
})