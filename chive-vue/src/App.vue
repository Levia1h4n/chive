<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <!-- <router-view /> -->
    <!-- </div> -->
    <!-- <Header>
        <TopBar></TopBar>
      </Header> -->
    <router-view></router-view>
    <!-- <TopMenu ref="topMenu"></TopMenu> -->
  </div>
</template>

<script>
// import TopMenu from './components/TopMenu'

export default {
  name: 'App',
  components: {
    // TopMenu
  }
}
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
