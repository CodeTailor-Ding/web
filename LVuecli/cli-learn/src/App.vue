<template>
  <div id="app">
    <left-bar></left-bar>
  </div>
</template>

<script>
import leftBar from './components/leftBar.vue'

export default {
  name: 'App',
  components: {
    leftBar,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
</style>
