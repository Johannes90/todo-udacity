import axios from 'axios';
import Vue from 'vue';
import jwtDecode from 'jwt-decode';

const state = {
    isLoggedIn: !!localStorage.getItem('access_token')
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
            console.log(response);
        });
    },
    login: ({commit}, user) => {
        axios.post('http://127.0.0.1:5000/auth', {
            username: user.email,
            password: user.password
        })
        .then(function (response) {
            let token = response.data.access_token;
            localStorage.setItem("current_user_id", jwtDecode(token).identity);
            localStorage.setItem("access_token", token);
            localStorage.setItem("current_user", user.email);
            user.router.push('/inbox');
            commit('LOGIN_SUCCESS');
        });
    },
    logout: ({commit}) => {
        localStorage.removeItem("access_token");
        localStorage.removeItem("current_user_id");
        commit('LOGOUT');
    }

}

const getters = {
    isLoggedIn: state => {
        return state.isLoggedIn;
    }
}


export default {
    state,
    mutations,
    actions,
    getters
}