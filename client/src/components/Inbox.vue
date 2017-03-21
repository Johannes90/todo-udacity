<template>
    <md-layout md-flex>
        <appNewTodo></appNewTodo>
        <appTodoList></appTodoList>
    </md-layout>
</template>

<script>
    import TodoList from "./TodoList.vue"
    import NewTodo from "./NewTodo.vue"

    export default {
        components: {
            appTodoList: TodoList,
            appNewTodo: NewTodo
        }
    }
</script>