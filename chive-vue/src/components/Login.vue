<template>
  <div>
    Username:
    <input
      type="text"
      v-model="loginForm.username"
      placeholder="Please enter user name"
    />
    <br /><br />
    Password:
    <input
      type="password"
      v-model="loginForm.password"
      placeholder="Please enter password"
    />
    <br /><br />
    <button v-on:click="login">登录</button>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      loginForm: {
        username: '',
        password: ''
      },
      responseResult: []
    }
  },
  methods: {
    login () {
      console.log(
        'username: ',
        this.loginForm.username,
        '\npassword: ',
        this.loginForm.password
      )
      //   console.log(this.loginForm.password)
      this.$axios
        .post('/login', {
          username: this.loginForm.username,
          password: this.loginForm.password
        })
        .then(successResponse => {
          if (successResponse.data.code === 200) {
            this.$router.replace({ path: '/index' })
          }
        })
        .catch(failResponse => {})
    }
  }
}
</script>
