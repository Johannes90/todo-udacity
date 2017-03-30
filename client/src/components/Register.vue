<template>
    <md-layout md-align="center">
        <form class="form" novalidate @submit.stop.prevent="submit">
            <h1>Sign Up Now</h1>
            <md-input-container>
                <label>Email Address</label>
                <md-input placeholder="Email" v-model="email"></md-input>
            </md-input-container>
            <md-input-container>
                <label>Password</label>
                <md-input type="password" v-model="password"></md-input>
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
                email: '',
                password: ''
            };
        },
        methods: {
            register() {
                this.$store.dispatch('register', {
                    email: this.email,
                    password: this.password
                }).then(() => {
                    this.$store.dispatch('login', {
                        email: this.email,
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