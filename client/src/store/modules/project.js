import axios from 'axios';
import Vue from 'vue';

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
        axios.get('http://127.0.0.1:5000/projects')
        .then(function (response) {
            commit('SET_PROJECTS', response.data.projects);
        });
    },
    addProject: ({ commit }, name) => {
        axios.post('http://127.0.0.1:5000/projects', {
            name: name
        })
        .then(function (response) {
            commit('ADD_PROJECT', {project: response.data});
        });
    },
    editProject: ({ commit }, project) => {
        axios.put('http://127.0.0.1:5000/project/' + project.id, {
            name: project.name
        }).then(function (response) {
            commit('EDIT_PROJECT', project)
        });
    },
    deleteProject: ({ commit }, project) => {
        axios.delete('http://127.0.0.1:5000/project/' + project.id)
        .then(function (response) {
            commit('DELETE_PROJECT', project);
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