<template>
  <div id="app">
    <br>
    <img alt="Vue logo" src="./assets/Logo.jpg">
    <Bhojan msg="Bhojan"/>
  </div>
</template>

<script>
import Bhojan from './components/Bhojan.vue'

export default {
  name: 'App',
  components: {
    Bhojan
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
img{
  max-width: 15%;
}
</style>
