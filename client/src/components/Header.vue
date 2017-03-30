<template>
    <md-toolbar>
        <router-link to="/" class="md-button" :class="`md-theme-${$material.currentTheme}`" activeClass="md-toggle">
            <md-icon>check circle</md-icon>
        </router-link>
        <h2 class="md-title" style="flex: 1">TODO</h2>
        <md-button class="md-button" v-if="isLoggedIn" @click.native="logout">
            <span>Logout</span>
        </md-button>
    </md-toolbar>
</template>

<script>
    export default {
        computed: {
            isLoggedIn() {
                return this.$store.getters.isLoggedIn;
            }
        },
        methods: {
            logout() {
                this.$store.dispatch('logout');
                this.$router.push('/');
            }
        }
    }
</script>