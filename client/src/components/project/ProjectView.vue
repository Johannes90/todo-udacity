<template>
    <md-layout>
        <md-list>
            <appTodo v-for="todo in todos" :todo="todo" :key="todo.id"></appTodo>
        </md-list>
    </md-layout>
</template>

<script>
import { mapGetters } from 'vuex'
import Todo from '@/components/todo/Todo.vue'
import NewTodo from '@/components/todo/NewTodo.vue'

    export default {
        computed: {
            todos() {
                return this.$store.getters.projectById(parseInt(this.$route.params.id)).todos
            }
        },
        components: {
            appTodo: Todo,
            appNewTodo: NewTodo
        }
    }
</script>