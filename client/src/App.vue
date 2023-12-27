<script>
import Navbar from './components/Navbar.vue'

export default {
  name: "App",
  data() {
    return {}
  },
  components: {
    Navbar
  }
}
</script>

<template>
  <div>
    <Navbar />

    <div class="container p-4">
      <router-view></router-view>
    </div>
  </div>
</template>

<style scoped>
</style>
