<template>
  <div id="app">
    <appHeader></appHeader>
    <router-view></router-view>
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
      this.$store.dispatch('initProjects');
      this.$store.dispatch('initUsers');
    }
  }
</script>

<style>
</style>
