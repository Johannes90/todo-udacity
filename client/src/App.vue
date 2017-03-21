<template>
  <div id="app">
    <appHeader></appHeader>
    <md-layout md-gutter>
      <sideMenu></sideMenu>
      <router-view></router-view>
    </md-layout>
  </div>
</template>

<script>
  import Header from './components/Header.vue';
  import SideMenu from './components/SideMenu.vue';
  export default {
    name: 'app',
    components: {
      appHeader: Header,
      sideMenu: SideMenu,
    },
    created() {
      this.$store.dispatch('initTodos');
    }
  }
</script>

<style>
</style>
