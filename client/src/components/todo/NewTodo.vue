<template>
    <md-list-item>
        <md-input-container md-inline class="addTodo">
            <md-input 
                @keyup.enter.prevent.native="addTodo" 
                v-model="desc" 
                placeholder="Add a new todo and press enter"
                autofocus></md-input>
        </md-input-container>
        <md-input-container class="project-dd">
        <label for="project">Choose Project</label>
        <md-select name="project" v-model="project_id">
            <md-option v-for="project in projects" :value="project.id" :key="project.id">{{ project.name }}</md-option>
        </md-select>
        </md-input-container>
        <md-button @click.native.prevent="addTodo(desc)" class="md-icon-button md-list-action">
            <md-icon class="md-fab">send</md-icon>
        </md-button>
    </md-list-item>
</template>

<script>
    export default {
        data() {
            return {
                desc: '',
                project_id: 0
            }
        },
        methods: {
            addTodo() {
                let desc = this.desc;
                let project_id = this.project_id
                this.$store.dispatch('addTodo', {desc: desc, project_id: project_id});
                this.desc = '';
                this.project_id = 0;
            }
        },
        computed: {
            projects() {
                return this.$store.getters.projects;
            }
        }
    }
</script>

<style>
  .project-dd {
    max-width: 200px;
  }
</style>