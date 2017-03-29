import axios from 'axios';
import Vue from 'vue';

const state = {
    isLoggedIn: !!localStorage.getItem('token')
}

const mutations = {
    'LOGIN_PENDING' (state) {
        state.pending = true;
    },
    'LOGIN_SUCCESS' (state) {
        state.isLoggedIn = true;
        state.pending = false;
    },
    'LOGOUT' (state) {
        state.isLoggedIn = false;
    }
}

const actions = {
    register: ({commit}, user) => {
        axios.post('http://127.0.0.1:5000/register', {
            username: user.email,
            password: user.password
        })
        .then(function (response) {
            commit('LOGIN_SUCCESS');
            console.log(response);
        });
    }
}


export default {
    state,
    mutations,
    actions
}