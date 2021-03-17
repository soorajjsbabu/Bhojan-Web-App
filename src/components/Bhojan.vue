<template>
  <div class="mainpage">
    <toolbar :value="true"
         :position="position"
         :height="64"
         :width="64"
         :color="color">
         
        </toolbar>
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
import Vue from 'vue'
import Toolbar from 'vue-js-toolbar'
Vue.use(Toolbar)

export default {
  name: 'Bhojan',
  props: {
    msg: String
  },
  data () {
    return {
      toggled: true,
      position: 'top',
      color: '#000000'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
