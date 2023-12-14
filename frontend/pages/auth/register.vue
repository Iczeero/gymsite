<template>
  <div  id="form">
    <label id="form-label">Регистрация</label>
    <div id="form-text">
    <form @submit.prevent="submitForm">
      <div id="form-field">
        <label>Имя пользователя</label>
        <input type="text" v-model="register.username" />
      </div>
      <div id="form-field">
        <label>Электронная почта</label>
        <input type="text" v-model="register.email" />
      </div>
      <div id="form-field">
        <label>Пароль</label>
        <input type="password" v-model="register.password" />
      </div>
      <div id="form-field">
        <label>Подтверждение пароля</label>
        <input type="password" v-model="register.password2" />
      </div>
      <div id="form-button">
        <button type="submit">Зарегистрироваться</button>
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
      register: {
        username: '',
        email: '',
        password: '',
        password2: ''
      }
    }
  },
  methods: {
    async submitForm() {
      try {
        let response = await this.$axios.$post('auth/register', this.register)
        this.$router.replace({name: 'auth-login'})
      } catch (err) {
        console.log(err)
      }
    }
  }
}
</script>