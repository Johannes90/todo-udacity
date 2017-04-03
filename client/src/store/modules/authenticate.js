import axios from 'axios';
import Vue from 'vue';
import jwtDecode from 'jwt-decode';

const state = {
    isLoggedIn: !!localStorage.getItem('access_token'),
    current_user: ''
}

const mutations = {
    'LOGIN_PENDING' (state) {
        state.pending = true;
    },
    'LOGIN_SUCCESS' (state) {
        state.isLoggedIn = true;
        state.current_user = localStorage.getItem("current_user");
        state.pending = false;
    },
    'LOGOUT' (state) {
        state.isLoggedIn = false;
        state.current_user = ''
    }
}

const actions = {
    register: ({commit}, user) => {
        axios.post('http://127.0.0.1:5000/register', {
            username: user.username,
            password: user.password
        })
        .then(function (response) {
            console.log(response);
        });
    },
    login: ({commit}, user) => {
        axios.post('http://127.0.0.1:5000/auth', {
            username: user.username,
            password: user.password
        })
        .then(function (response) {
            let token = response.data.access_token;
            localStorage.setItem("current_user_id", jwtDecode(token).identity);
            localStorage.setItem("access_token", token);
            localStorage.setItem("current_user", user.username);
            commit('LOGIN_SUCCESS');
        });
    },
    logout: ({commit}) => {
        localStorage.removeItem("access_token");
        localStorage.removeItem("current_user_id");
        localStorage.removeItem("current_user");
        commit('LOGOUT');
    }

}

const getters = {
    isLoggedIn: state => {
        return state.isLoggedIn;
    },
    current_user: state => {
        return state.current_user;
    }
}


export default {
    state,
    mutations,
    actions,
    getters
}