import axios from 'axios';
import Vue from 'vue';





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
        axios.get('http://127.0.0.1:5000/todos')
        .then(function (response) {
            commit('SET_TODOS', response.data.todos);
        }); 
    },
    addTodo: ({commit}, { desc, project_id, user_id }) => {
        console.log({ desc, project_id, user_id });
        axios.post('http://127.0.0.1:5000/todos', {
            desc: desc,
            project_id: project_id,
            user_id: user_id
        })
        .then(function (response) {
            commit('ADD_TODO', {todo: response.data});
        });
    },
    deleteTodo: ({commit}, todo) => {
        let headers = {headers: { 'Content-Type': 'application/json', 'Authorization': "JWT " + localStorage.getItem("access_token")}};
        axios.delete('http://127.0.0.1:5000/todo/' + todo.id, headers)
        .then(function (response) {
            commit('DELETE_TODO', todo);
        });
    },
    editTodo: ({ commit }, todo) => {
        let headers = {headers: { 'Content-Type': 'application/json', 'Authorization': "JWT " + localStorage.getItem("access_token")}};
        axios.put('http://127.0.0.1:5000/todo/' + todo.id, {
            desc: todo.desc,
            done: todo.done
        }, headers).then(function (response) {
            console.log(todo)
            commit('EDIT_TODO', todo)
        });
    },
    completeTodo: ({ commit }, todo) => {
        axios.put('http://127.0.0.1:5000/todo/' + todo.id, {
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