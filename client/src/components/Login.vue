<template>
    <md-layout md-align="center">
        <form class="form" novalidate @submit.prevent="login">
            <h1>Login</h1>
            <md-input-container :class="{ 'md-input-invalid': errors.has('username') }">
                <label>Username</label>
                <md-input v-validate data-vv-rules="required" v-model="username" data-vv-name="username" required></md-input>
                <span class="md-error" v-show="errors.has('username')">{{ errors.first('username') }}</span>
            </md-input-container>
            <md-input-container md-has-password :class="{ 'md-input-invalid': errors.has('password') }">
                <label>Password</label>
                <md-input type="password" v-validate data-vv-rules="required" v-model="password" data-vv-name="password" required></md-input>
                <span class="md-error" v-show="errors.has('password')">{{ errors.first('password') }}</span>
            </md-input-container>
            <md-button class="md-raised md-warn" @click.native="$router.push('/')">Cancel</md-button>
            <md-button class="md-raised md-primary">Login with Google</md-button>
            <md-button class="md-raised md-primary" type="submit">Login</md-button>
            <p>Need an account?
                <router-link to="/register">Sign Up here</router-link>.</p>
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
            login() {
                this.$validator.validateAll();
                if (!this.errors.any()) {
                    this.$store.dispatch('login', {
                        username: this.username,
                        password: this.password
                    }).then(() => {
                        this.$router.push("/inbox")
                    });
                }
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