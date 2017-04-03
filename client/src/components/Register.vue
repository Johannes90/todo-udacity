<template>
    <md-layout md-align="center">
        <form class="form" novalidate @submit.stop.prevent="submit">
            <h1>Sign Up Now</h1>
            <md-input-container>
                <label>Username</label>
                <md-input v-model="username" required></md-input>
            </md-input-container>
            <md-input-container>
                <label>Password</label>
                <md-input type="password" v-model="password" required></md-input>
            </md-input-container>
            <md-button class="md-raised md-warn" @click.native="$router.push('/')">Cancel</md-button>
            <md-button class="md-raised md-primary">Sign Up with Google</md-button>
            <md-button class="md-raised md-primary" @click.native="register()">Sign Up</md-button>
            <p>Already have an account?
                <router-link to="/login">Login here</router-link>.</p>
        </form>
    </md-layout>
</template>

<script>
    export default {
        data() {
            return {
                username: '',
                password: ''
            };
        },
        methods: {
            register() {
                this.$store.dispatch('register', {
                    username: this.username,
                    password: this.password
                }).then(() => {
                    this.$store.dispatch('login', {
                        username: this.username,
                        password: this.password
                    });
                }).then(() => {
                    this.$router.push("/inbox")
                });
            }
        }
    }
</script>

<style>
    .form {
        margin-top: 100px;
        width: 500px;
    }
</style>