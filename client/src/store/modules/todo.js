import axios from 'axios';
import Vue from 'vue';
import { authCall, noAuthCall } from '@/config/api_config'


const state = {
    todos: []
};

const mutations = {
    'SET_TODOS' (state, todos) {
        state.todos = todos;
    },
    'ADD_TODO' (state, { todo })  {
        state.todos.push(todo)
    },
    'DELETE_TODO' (state, todo) {
        let index = state.todos.indexOf(todo)
        state.todos.splice(index,1);
    },
    'EDIT_TODO' (state, todo) {
        Vue.set(state.todos, state.todos.indexOf(todo), todo)
    },
    'COMPLETE_TODO' (state, todo) {
        Vue.set(state.todos, state.todos.indexOf(todo), todo)
    }
}

const actions = {
    initTodos: ({commit}) => {
        noAuthCall.get('/todos')
        .then(function (response) {
            commit('SET_TODOS', response.data.todos);
        }); 
    },
    addTodo: ({commit}, { desc, project_id, user_id }) => {
        authCall.post('/todos', {
            desc: desc,
            project_id: project_id,
            user_id: user_id
        })
        .then(function (response) {
            commit('ADD_TODO', {todo: response.data});
        });
    },
    deleteTodo: ({commit}, todo) => {
        authCall.delete('/todo/' + todo.id)
        .then(function (response) {
            commit('DELETE_TODO', todo);
        });
    },
    editTodo: ({ commit }, todo) => {
        authCall.put('/todo/' + todo.id, {
            desc: todo.desc,
            done: todo.done
        }).then(function (response) {
            console.log(todo)
            commit('EDIT_TODO', todo)
        });
    },
    completeTodo: ({ commit }, todo) => {
        authCall.put('/todo/' + todo.id, {
            desc: todo.desc,
            done: todo.done
        }).then(function (response) {
            console.log(todo)
            commit('COMPLETE_TODO', todo)
        });
    }
}

const getters = {
    todos: state => {
        return state.todos.sort(function (a,b) {
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