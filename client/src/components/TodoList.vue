<template>
        <md-list>
            <appTodo v-for="todo in todos" :todo="todo" :key="todos.id"></appTodo>
        </md-list>
</template>

<script>
    import Todo from './Todo.vue';

    export default {
        data() {
            return {
                
            }
        },
        components: {
            appTodo: Todo
        },
        computed: {
            todos() {
                return this.$store.getters.todos;
            }
        }
    }
</script>

<style>
    .md-list {
        width: 100%;
    }
</style>