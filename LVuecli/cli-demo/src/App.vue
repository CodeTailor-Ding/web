<template>
  <hh titleText="创建第一个vue"></hh>
  <ss></ss>
  <ff></ff>
</template>

<script>
  import Header from "./components/Header.vue"
  import Footer from "./components/Footer.vue"
  import Sidebar from "./components/Sidebar.vue"

  export default {
    name: 'App',
    components: {
      hh: Header,
      ff: Footer,
      ss: Sidebar
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
    margin-top: 60px;
  }
</style>
