<template>
    <md-toolbar>
    <router-link 
            to="/" 
            class="md-button" 
            :class="`md-theme-${$material.currentTheme}`" 
            activeClass="md-toggle">
      <md-icon>check circle</md-icon>
      <h2 class="md-title" style="flex: 1">TODO</h2>
    </router-link>
    </md-toolbar>
</template>

<script>
    export default {

    }
</script>