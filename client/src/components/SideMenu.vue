<template>
    <md-layout md-flex="30">
      <md-list>
        <md-subheader>Navigation</md-subheader>
            <md-list-item>
                <router-link 
                to="/inbox" 
                class="md-button" 
                :class="`md-theme-${$material.currentTheme}`" 
                activeClass="md-toggle">
                  <md-icon>move_to_inbox</md-icon> <span>Inbox</span>
                </router-link>
            </md-list-item>
            <md-list-item>
              <md-icon>folder</md-icon> 
              <span>Projects</span>
              <md-list-expand>
                <md-list>
                    <appProject class="md-inset" v-for="project in projects" :project="project" :key="projects.id"></appProject>
                </md-list>
            </md-list-expand>
            </md-list-item>
            <appNewProject></appNewProject>
          </md-list>
  </md-layout>
</template>

<script>
import newProject from './project/NewProject'
import Project from './project/Project'
export default {
    computed: {
            projects() {
                return this.$store.getters.projects;
            }
        },
    components: {
        appNewProject: newProject,
        appProject: Project
    }
}
</script>
<style>
</style>