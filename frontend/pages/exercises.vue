<template>
    <div class="container">
      <div class="content" v-if="isAuthenticated">
        {{ user?.exerсises }}  
      </div>
      <div v-else>
        <ul>
            <li v-for="exercise in exercises" :key="exercise.id">
                {{ exercise.name }} - {{ exercise.description }}  <input type="checkbox" v-model="isChecked" @change="updateIsChecked" />
            </li>
    </ul>
      </div>
    </div>
  </template>

<script>
import axios from 'axios';
export default {
    
    data() {
    return {
        exercises: [] // Массив для хранения данных из базы данных
    };
  },
  created() {
    this.fetchExercises();
  },

  

    computed:{
    isAuthenticated(){
      return this.$auth.loggedIn
    },

    user(){
      return this.$auth.user
    },

    
},

methods: {
    async fetchExercises() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/exercis');
        this.exercises = response.data;
      } catch (error) {
        console.error('Ошибка при получении данных об упражнениях:', error);
      }
    }
},

}
</script>

<style>
@import url("~/static/main.css");
</style>