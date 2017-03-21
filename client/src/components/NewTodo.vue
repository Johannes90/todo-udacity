<template>
    <md-layout>
        <md-input-container md-inline class="addTodo">
            <md-input @keyup.enter.prevent.native="addTodo" v-model="newTodo" placeholder="Add a new todo"></md-input>
        </md-input-container>
        <md-button @click.native.prevent="addTodo" class="md-icon-button md-raised md-mini md-primary">
            <md-icon>add</md-icon>
        </md-button>
    </md-layout>
</template>

<script>
    export default {
        data() {
            return {
                newTodo: ''
            }
        },
        methods: {
            addTodo() {
                let newTodo = this.newTodo;
                console.log(newTodo);
                this.$store.dispatch('addTodo',{newTodo});
                this.newTodo = ''
            }
        }
    }
</script>
<style>
    .addTodo {width: 90%;}
</style>