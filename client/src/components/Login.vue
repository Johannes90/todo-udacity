<template>
    <md-layout md-align="center">
        <form class="form" novalidate @submit.stop.prevent="submit">
            <h1>Login</h1>
            <md-input-container>
                <label>Email Address</label>
                <md-input placeholder="Email" v-model="email"></md-input>
            </md-input-container>
            <md-input-container>
                <label>Password</label>
                <md-input type="password" v-model="password"></md-input>
            </md-input-container>
            <md-button class="md-raised md-warn" @click.native="$router.push('/')">Cancel</md-button>
            <md-button class="md-raised md-primary">Login with Google</md-button>
            <md-button class="md-raised md-primary">Login</md-button>
            <p>Need an account? <router-link to="/register">Sign Up here</router-link>.</p>
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
        }
    }
</script>

<style>
    .form {
        margin-top: 100px;
        width: 500px;
    }
</style>