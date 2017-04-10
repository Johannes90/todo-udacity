<template>
    <md-layout md-gutter>
        <sideMenu></sideMenu>
        <md-layout md-flex>
            <md-list>
                <appTodo v-for="todo in todos" :todo="todo" :key="todo.id"></appTodo>
            </md-list>
        </md-layout>
    </md-layout>
</template>

<script>
    import {
        mapGetters
    } from 'vuex'
    import Todo from '@/components/todo/Todo.vue'
    import NewTodo from '@/components/todo/NewTodo.vue'
    import sideMenu from '@/components/SideMenu.vue'
    
    export default {
        computed: {
            todos() {
                console.log(this.$store.getters.projectById(parseInt(this.$route.params.id)).todos)
                return this.$store.getters.projectById(parseInt(this.$route.params.id)).todos
            }
        },
        components: {
            appTodo: Todo,
            appNewTodo: NewTodo,
            sideMenu
        }
    }
</script>