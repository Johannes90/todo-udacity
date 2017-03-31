<template>
    <md-list-item>
      <md-checkbox v-model="todo.done" @change="completeTodo(todo)"></md-checkbox>
      <md-input-container md-inline>
        <md-input 
        @blur.native="editTodo(todo)" 
        v-model="todo.desc"></md-input>
      </md-input-container>
      <md-chip>{{ todo.created_by }}</md-chip>
      <md-chip>{{ todo.project }}</md-chip>
      <md-button @click.native="deleteTodo(todo)" class="md-icon-button md-list-action">
        <md-icon class="md-fab">clear</md-icon>
      </md-button>
    </md-list-item>
</template>

<script>
    export default {
        props: [
          'todo'
          ],
        methods: {
          deleteTodo(todo) {
            this.$store.dispatch('deleteTodo', todo)
          },
          editTodo(todo) {
            this.$store.dispatch('editTodo', todo)
          },
          completeTodo(todo) {
            todo.done = !todo.done
            console.log(todo)
            this.$store.dispatch('completeTodo', todo)
          }
        }
    }
</script>