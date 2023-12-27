<template>
  <form class="w-50 mt-5 mx-auto">
    <div class="mb-3">
      <label for="exampleInputEmail1" class="form-label fw-bold">Email address</label>
      <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
      <div id="emailHelp" class="form-text fw-lighter">We'll never share your email with anyone else.</div>
    </div>
    <div class="mb-3">
      <label for="exampleInputPassword1" class="form-label fw-bold">Password</label>
      <input type="password" class="form-control" id="exampleInputPassword1">
    </div>
    <div class="d-flex flex-row justify-content-between align-items-center">
      <button type="submit" class="btn btn-dark">Submit</button>
      <router-link class="text-primary-emphasis pe-auto" to="/register">Register here</router-link>
    </div>
  </form>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {}
  }
}
</script>

<style scoped></style>
