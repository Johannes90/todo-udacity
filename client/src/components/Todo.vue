<template>
    <md-list-item>
      <span>{{ todo.desc }}</span>
      <md-button @click.native="editTodo(todo)" class="md-icon-button md-list-action">
        <md-icon class="md-fab">create</md-icon>
      </md-button>
      <md-button @click.native="deleteTodo(todo)" class="md-icon-button md-list-action">
        <md-icon class="md-fab">clear</md-icon>
      </md-button>
      <md-divider></md-divider>
    </md-list-item>
</template>

<script>
    export default {
        props: ['todo'],
        methods: {
          deleteTodo(todo) {
            this.$store.dispatch('deleteTodo', todo)
          }
        }
    }
</script>