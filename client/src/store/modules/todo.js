import axios from 'axios';

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
    'DELETE_TODO' (state, { todo }) {
        let index = state.todos.indexOf(todo)
        state.todos.splice(index,1);
    }
}

const actions = {
    initTodos: ({commit}) => {
        axios.get('http://127.0.0.1:5000/todos')
        .then(function (response) {
            commit('SET_TODOS', response.data.todos);
        }); 
    },
    addTodo: ({commit}, desc) => {
        axios.post('http://127.0.0.1:5000/todos', {
            desc: desc.newTodo
        })
        .then(function (response) {
            console.log(response.data)
            commit('ADD_TODO', {todo: response.data});
        });
    },
    deleteTodo: ({commit}, todo) => {
        console.log(todo.id)
        axios.delete('http://127.0.0.1:5000/todo/' + todo.id)
        .then(function (response) {
            commit('DELETE_TODO', { todo: todo });
        })
    }
}

const getters = {
    todos: state => {
        return state.todos;
    }
}

export default {
    state,
    mutations,
    actions,
    getters
}