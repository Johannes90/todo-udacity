<template>
    <md-layout md-flex="25">
      <md-list>
        <md-subheader>Navigation</md-subheader>
        <router-link 
            to="/inbox" 
            class="md-button" 
            :class="`md-theme-${$material.currentTheme}`" 
            activeClass="md-toggle">
            <md-list-item>
              <md-icon>move_to_inbox</md-icon> <span>Inbox</span>
            </md-list-item>
        </router-link>
        <router-link 
            to="/projects" 
            class="md-button" 
            :class="`md-theme-${$material.currentTheme}`" 
            activeClass="md-toggle">
                <md-list-item>
                  <md-icon>folder</md-icon> <span>Projects</span>
                </md-list-item>
        </router-link>
      </md-list>
  </md-layout>
</template>

<style>
    .router-link {
        style: none;
    } 
</style>