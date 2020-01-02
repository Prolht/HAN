<template>
  <div id="app">
    <router-view/>
  </div>
</template>
<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  margin: 0
}
html, body {
  margin: 0;
  padding: 0;
  background:url(..\static\index.jpg) no-repeat;
  background-size:100% 100%;
  height:100%;
}
.clearfix::after, .clearfix::before {
    content:" ";
    display:table;
}
.clearfix::after {
    clear:both;
}
</style>
