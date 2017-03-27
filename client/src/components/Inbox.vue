<template>
    <md-layout md-gutter>
        <sideMenu></sideMenu>
        <md-layout md-flex>
            <appTodoList></appTodoList>
        </md-layout>
    </md-layout>
</template>

<script>
    import TodoList from "./todo/TodoList.vue"
    import SideMenu from './SideMenu.vue';
    export default {
        components: {
            appTodoList: TodoList,
            sideMenu: SideMenu
        }
    }
</script>