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



export default {
    state,
    mutations
}