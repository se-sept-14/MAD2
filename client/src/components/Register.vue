<template>
  <form class="mx-auto mt-5 w-50">
    <div class="mb-3">
      <label for="inputEmail" class="form-label fw-bold">Email address</label>
      <input type="email" class="form-control" id="inputEmail" aria-describedby="emailHelp">
    </div>
    <div class="mb-3">
      <label for="inputUsername" class="form-label fw-bold">Username</label>
      <input type="text" class="form-control" id="inputUsername" aria-describedby="usernameHelp">
    </div>
    <div class="mb-3">
      <label for="inputPassword" class="form-label fw-bold">Password</label>
      <input type="password" class="form-control" id="inputPassword">
    </div>
    <div class="mb-3">
      <label for="inputPasswordAgain" class="form-label fw-bold">Password Again</label>
      <input type="password" class="form-control" id="inputPasswordAgain">
    </div>
    <button type="submit" class="btn btn-dark">Submit</button>
  </form>
</template>

<script>
export default {
  name: "Register",
  data() {
    return {}
  }
}
</script>

<style scoped></style>
