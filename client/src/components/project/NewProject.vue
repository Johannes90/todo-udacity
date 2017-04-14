<template>
    <md-list-item>
        <md-input-container md-inline>
            <md-input 
                @keyup.enter.prevent.native="addProject" 
                v-model="name" 
                placeholder="Add project"
                autofocus></md-input>
        </md-input-container>
    </md-list-item>
</template>

<script>
    export default {
        data() {
            return {
                name: ''
            }
        },
        methods: {
            addProject() {
                let name = this.name;
                let user_id = parseInt(localStorage.getItem("current_user_id"))
                this.$store.dispatch('addProject', {
                    name,
                    user_id
                });
                this.name = ''
            }
        }
    }
</script>