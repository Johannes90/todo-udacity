<template>
    <md-toolbar>
        <router-link to="/" class="md-button" :class="`md-theme-${$material.currentTheme}`">
            <md-icon>check circle</md-icon>
        </router-link>
        <h2 class="md-title" style="flex: 1">TODO</h2>
        <router-link v-if="isLoggedIn" to="/inbox" class="md-button" :class="`md-theme-${$material.currentTheme}`">
            <md-icon>face</md-icon>
            <span>{{ current_user }}</span>
        </router-link>
        <md-button class="md-button" v-if="isLoggedIn" @click.native="logout">
            <span>Logout</span>
        </md-button>
    </md-toolbar>
</template>

<script>
    export default {
        data() {
            return {
                
            }
        },
        computed: {
            isLoggedIn() {
                return this.$store.getters.isLoggedIn;
            },
            current_user() {
                return this.$store.getters.current_user;
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