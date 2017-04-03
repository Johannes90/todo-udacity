<template>
    <md-list-item>
        <md-input-container md-inline class="addTodo">
            <md-input v-model="desc" placeholder="Add a new todo and press enter" autofocus required></md-input>
        </md-input-container>
        <md-input-container :class="{ 'md-input-invalid': noProject }">
            <label for="project">Choose Project</label>
            <md-select name="project" v-model="project_id" required>
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
                project_id: '',
                noProject: false
            }
        },
        methods: {
            addTodo() {
                let desc = this.desc;
                let project_id = this.project_id
                let user_id = parseInt(localStorage.getItem("current_user_id"))
                if (project_id === '') {
                    this.noProject = true
                } else {
                    this.$store.dispatch('addTodo', {
                        desc: desc,
                        project_id: project_id,
                        user_id: user_id
                    });
                    this.desc = '';
                    this.project_id = '';
                }
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