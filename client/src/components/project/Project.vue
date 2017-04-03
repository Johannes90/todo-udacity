<template>
    <md-list-item>
      
      <md-input-container md-inline>
      <router-link 
                :to="'/project/' + project.id" 
                class="md-icon-button md-list-action" 
                :class="`md-theme-${$material.currentTheme}`" 
                activeClass="md-toggle">
        <md-icon class="md-fab">list</md-icon>
      </router-link>
        <md-input 
        @blur.native="editProject(project)" 
        v-model="project.name"></md-input>
      </md-input-container>
    </md-list-item>
</template>

<script>
    export default {
        props: ['project'],
        methods: {
          editProject(project) {
            this.$store.dispatch('editProject', project)
          }
        }
    }
</script>