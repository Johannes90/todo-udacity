<template>
    <md-layout class="home" md-align="end" md-gutter="16">
        <md-layout md-flex="33">
            <h1 class="headline">Do more of the right things.</h1>
            <md-button class="md-raised md-primary" @click.native="$router.push('/register')">Sign Up</md-button>
            <md-button class="md-raised md-primary" @click.native="$router.push('/login')">Sign In</md-button>
        </md-layout>
    </md-layout>
        
        </md-layout>
    </md-layout>
</template>

<script>
export default {
  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .home {
        background-image: url("/static/images/desk.jpg");
        background-size: cover;
        height: 600px;
    },
    .home-button {
        height: 10px;
    }

</style>
