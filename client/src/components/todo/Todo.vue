<template>
  <md-list-item>
    <md-checkbox v-model="todo.done" @change="completeTodo(todo)"></md-checkbox>
    <md-input-container md-inline>
      <md-input @blur.native="editTodo(todo)" v-model="todo.desc" class="md-input-disabled" :disabled="lockTodos"></md-input>
        </md-input-container>
        <md-chip>{{ todo.created_by }}</md-chip>
        <md-chip>{{ todo.project }}</md-chip>
        <md-button @click.native=" deleteTodo(todo) " class="md-icon-button md-list-action">
          <md-icon class="md-fab">clear</md-icon>
        </md-button>
        <md-snackbar md-position="bottom center" ref="snackbar" md-duration="3000">
          <span>{{ message }}</span>
        </md-snackbar>
      </md-list-item>
</template>

<script>
  export default {
    props: [
      'todo'
    ],
    data() {
      return {
        message: ''
      }
    },
    methods: {
      deleteTodo(todo) {
        if (todo.created_by === localStorage.getItem("current_user")) {
            this.$store.dispatch('deleteTodo', todo).then(() => {
          });
        } else {
          this.message = "You are not the creator of this todo. Cannot delete.";
          this.$refs.snackbar.open();
        }
  
      },
      editTodo(todo) {
        this.$store.dispatch('editTodo', todo)
      },
      completeTodo(todo) {
        todo.done = !todo.done
        console.log(todo)
        this.$store.dispatch('completeTodo', todo)
      }
    },
    computed: {
      lockTodos() {
        return this.todo.created_by !== localStorage.getItem("current_user");
      }
      
    }
  }
</script>