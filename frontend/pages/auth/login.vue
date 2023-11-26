<template>
  <div  id="form">
    <label id="form-label">Вход</label>
    <div id="form-text">
    <form @submit.prevent="submitForm" >
      <div id="form-field">
        <label>Логин</label>
        <input type="text" v-model="login.email" />
      </div>
      <div id="form-field">
        <label>Пароль</label>
        <input type="password" v-model="login.password" />
      </div>
      <div id="form-button">
        <button type="submit">Войти</button>
        <li><nuxt-link to="/auth/register">Зарегистрироваться</nuxt-link></li>
      </div>
    </form>
    </div>
  </div>
</template>

<style>
@import url("~/static/main.css");
</style>

<script>
export default {

middleware: ['auth'],
auth: 'guest',

data() {
  return {
    login: {
      email: '',
      password: ''
    }
  }
},
methods: {
  async submitForm() {
    try {
      let response = await this.$auth.loginWith('local', { data: this.login })
      this.$router.replace({name: 'auth-user'})
    } catch (err) {
      console.log(err)
    }
  }
}
}
</script>

