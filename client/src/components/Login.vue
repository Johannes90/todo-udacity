<template>
    <md-layout md-align="center">
        <form class="form" novalidate @submit.prevent="login">
            <h1>Login</h1>
            <md-input-container :class="{ 'md-input-invalid': errors.has('username') }">
                <label>Email</label>
                <md-input v-validate data-vv-rules="required|userNotExists|email" v-model="username" data-vv-name="username" required></md-input>
                <span class="md-error" v-show="errors.has('username')">{{ errors.first('username') }}</span>
            </md-input-container>
            <md-input-container md-has-password :class="{ 'md-input-invalid': errors.has('password') }">
                <label>Password</label>
                <md-input type="password" v-validate data-vv-rules="required" v-model="password" data-vv-name="password" required></md-input>
                <span class="md-error" v-show="errors.has('password')">{{ errors.first('password') }}</span>
            </md-input-container>
            <md-button class="md-raised md-warn" @click.native="$router.push('/')">Cancel</md-button>
            <g-signin-button :params="googleSignInParams" @success="onSignInSuccess" @error="onSignInError" class="md-button md-raised md-primary md-theme-default">
                Sign in with Google
            </g-signin-button>
            <md-button class="md-raised md-primary" type="submit">Login</md-button>
            <p>Need an account?
                <router-link to="/register">Sign Up here</router-link>.</p>
        </form>
        <md-snackbar md-position="bottom center" ref="snackbar" md-duration="3000">
            <span v-for="error in errors.all()"> {{ error }} </span>
        </md-snackbar>
        <md-snackbar md-position="bottom center" ref="password" md-duration="3000">
            <span> Wrong password! </span>
        </md-snackbar>
    </md-layout>
</template>

<script>
    import {
        Validator
    } from 'vee-validate';
    export default {
        data() {
            return {
                username: '',
                password: '',
                googleSignInParams: {
                    client_id: process.env.GOOGLE_CLIENT_ID
                },
                googleError: ''
            };
        },
        methods: {
            login() {
                this.$validator.validateAll().then(() => {
                    this.$store.dispatch('login', {
                            username: this.username,
                            password: this.password
                        })
                        .then(() => {
                            if (this.$store.getters.isLoggedIn) {
                                this.$router.push("/inbox");
                            } else {
                                console.log('rejected')
                                this.$refs.password.open();
                            }
                        });
                }).catch(() => {
                    this.$refs.snackbar.open();
                });
            },
            onSignInSuccess(googleUser) {
                const username = googleUser.getBasicProfile().getEmail()
                const id_token = googleUser.getAuthResponse().id_token;
                if (this.$store.getters.users.some(user => user.username == username)) {
                    this.$store.dispatch('login', {
                        username,
                        password: id_token
                    }).then(() => {
                        this.$router.push({name: 'Inbox'});
                    });
                } else {
                    this.$store.dispatch('googleSignUp', {
                        username,
                        id_token
                    }).then(() => {
                        this.$store.dispatch('login', {
                            username,
                            password: id_token
                        });
                    }).then(() => {
                        this.$router.push({name: 'Inbox'});
                    });
                }
    
            },
            onSignInError(error) {
                this.googleError = error.error;
                this.$refs.googleSign.open();
            }
        },
        created() {
            Validator.extend('userNotExists', {
                getMessage: (field) => `We could not find this ${field}.`,
                validate: (value) => {
                    let users = this.$store.getters.users;
                    return users.some(user => user.username == value);
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