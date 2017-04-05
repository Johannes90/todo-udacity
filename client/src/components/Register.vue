<template>
    <md-layout md-align="center">
        <form class="form" novalidate @submit.prevent="register">
            <h1>Sign Up Now</h1>
            <md-input-container :class="{ 'md-input-invalid': errors.has('username') }">
                <label>Username</label>
                <md-input v-validate data-vv-rules="required|userExists" v-model="username" data-vv-name="username" required></md-input>
                <span class="md-error" v-show="errors.has('username')">{{ errors.first('username') }}</span>
            </md-input-container>
            <md-input-container md-has-password :class="{ 'md-input-invalid': errors.has('password') }">
                <label>Password</label>
                <md-input type="password" v-validate data-vv-rules="required" v-model="password" data-vv-name="password" required></md-input>
                <span class="md-error" v-show="errors.has('password')">{{ errors.first('password') }}</span>
            </md-input-container>
            <md-button class="md-raised md-warn" @click.native="$router.push('/')">Cancel</md-button>
            <md-button class="md-raised md-primary">Sign Up with Google</md-button>
            <md-button class="md-raised md-primary" type="submit">Sign Up</md-button>
            <p>Already have an account?
                <router-link to="/login">Login here</router-link>.</p>
        </form>
        <md-snackbar v-show="errors.has('username')" md-position="bottom center" ref="snackbar" md-duration="3000">
          <span>{{ errors.first('username') }}</span>
        </md-snackbar>
    </md-layout>
</template>

<script>
    import { Validator } from 'vee-validate';

    export default {
        data() {
            return {
                username: '',
                password: ''
            };
        },
        methods: {
            register() {
                this.$validator.validateAll();
                if (!this.errors.any()) {
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
        },
        created() {
            Validator.extend('userExists', {
                    getMessage: (field) => {
                    'User already exists'
                },
                validate: (value) => {
                    let users = this.$store.getters.users;
                    console.log(value);
                    console.log(!users.some(user => user.username == value));
                    return !users.some(user => user.username == value);
                }
            });
        }
    }
</script>

<style>
    .form {
        margin-top: 100px;
        width: 500px;
    }
</style>