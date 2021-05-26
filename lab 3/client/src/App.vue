<template>
  <div id="app">
  <b-navbar toggleable="lg" type="dark" variant="dark">
    <b-navbar-brand href="/actors">Actors</b-navbar-brand>
    <b-navbar-brand href="/movies">Movies</b-navbar-brand>
    <b-navbar-brand href="/directors">Directors</b-navbar-brand>
  </b-navbar>
    <router-view/>
  </div>
</template>

<style>
#app {
  margin-top: 60px
}
</style>
