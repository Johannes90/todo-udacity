import axios from 'axios';
import Vue from 'vue';
import { authCall, noAuthCall } from '@/config/api_config'

const state = {
    projects: []
}

const mutations = {
    'SET_PROJECTS' (state, projects) {
        state.projects = projects;
    },
    'ADD_PROJECT' (state, { project }) {
        state.projects.push(project);
    },
    'EDIT_PROJECT' (state, project) {
        Vue.set(state.projects, state.projects.indexOf(project), project)
    },
    'DELETE_PROJECT' (state, project) {
        let index = state.projects.indexOf(project)
        state.projects.splice(index,1);
    }
}

const actions = {
    initProjects: ({ commit }) => {
        noAuthCall.get('/projects')
        .then(function (response) {
            commit('SET_PROJECTS', response.data.projects);
        });
    },
    addProject: ({ commit }, project) => {
        authCall.post('/projects', {
            name: project.name,
            user_id: project.user_id
        })
        .then(function (response) {
            console.log(response)
            commit('ADD_PROJECT', {project: response.data});
        });
    },
    editProject: ({ commit }, project) => {
        authCall.put('/project/' + project.id, {
            name: project.name,
            user_id: project.user_id
        }).then(function (response) {
            commit('EDIT_PROJECT', project)
        });
    }   
}


const getters = {
    projects: state => {
        return state.projects.sort(function (a,b) {
            return a.id - b.id
        });
    },
    projectById: state => (project_id) => {
        return state.projects.find(project => project.id === project_id)
    }
}

export default {
    state,
    mutations,
    actions,
    getters
}