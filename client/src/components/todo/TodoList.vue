<template>
        <md-list>
            <appNewTodo></appNewTodo>
            <appTodo v-for="todo in todos" :todo="todo" :key="todos.id"></appTodo>
        </md-list>
</template>

<script>
    import Todo from './Todo.vue';
    import NewTodo from "./NewTodo.vue";

    export default {
        components: {
            appTodo: Todo,
            appNewTodo: NewTodo
        },
        computed: {
            todos() {
                return this.$store.getters.todos;
            },
        }
    }
</script>

<style>
    .md-list {
        width: 100%;
    }
</style>