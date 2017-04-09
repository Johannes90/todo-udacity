import axios from 'axios';
import Vue from 'vue';
import jwtDecode from 'jwt-decode';

const state = {
    isLoggedIn: !!localStorage.getItem('access_token'),
    current_user: '',
    users: [],
    passwordWrong: false
}

const mutations = {
    'SET_USERS' (state, users) {
        state.users = users;
    },
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
    },
    'REGISTER' (state, user) {
        state.users.push(user);
    }
}

const actions = {
    initUsers: ({commit}) => {
        axios.get('http://127.0.0.1:5000/users')
        .then(function (response) {
            commit('SET_USERS', response.data.users);
        }); 
    },
    register: ({commit}, user) => {
        axios.post('http://127.0.0.1:5000/register', {
            username: user.username,
            password: user.password
        })
        .then(function (response) {
            commit('REGISTER', response.data)
            console.log(response);
        });
    },
    login: ({commit}, user) => {
        console.log(user.password)
        axios.post('http://127.0.0.1:5000/auth', {
            username: user.username,
            password: user.password
        })
        .then(function (response) {
            console.log(response);
            let token = response.data.access_token;
            localStorage.setItem("current_user_id", jwtDecode(token).identity);
            localStorage.setItem("access_token", token);
            localStorage.setItem("current_user", user.username);
            commit('LOGIN_SUCCESS');
            Promise.resolve(response.data);
        }).catch(function (error) {
            Promise.reject(error);
        });
    },
    logout: ({commit}) => {
        localStorage.removeItem("access_token");
        localStorage.removeItem("current_user_id");
        localStorage.removeItem("current_user");
        commit('LOGOUT');
    },
    googleSignUp: ({commit}, user) => {
        console.log(user.username)
        console.log(user.id_token)
        axios.post('http://127.0.0.1:5000/google-sign', {
            username: user.username,
            id_token: user.id_token
        })
    }

}

const getters = {
    isLoggedIn: state => {
        return state.isLoggedIn;
    },
    current_user: state => {
        return state.current_user;
    },
    users: state => {
        return state.users.sort(function (a,b) {
            return a.id - b.id
        });
    }
}


export default {
    state,
    mutations,
    actions,
    getters
}