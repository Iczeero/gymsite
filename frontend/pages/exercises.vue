<template>
  <div>
    <div v-for="exercise in exercises" :key="exercise.id">
      <button class="exercise" @click="showModal(exercise)">{{ exercise.name }}</button>
    </div>
    <div v-if="isModalVisible" class="modal" @click="closeModalOutside">
      <div class="modal-content" @click.stop>
        <span class="close" @click="closeModal">&times;</span>
        <h2>{{ selectedExercise.name }}</h2>
        <p>{{ selectedExercise.description }}</p>
        <input v-if="isAuthenticated && isChecked(selectedExercise)" type="checkbox" v-model="selectedExercise.checked" @change="updateCheckedStatus(selectedExercise)">
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      exercises: [],
      isModalVisible: false,
      selectedExercise: {},
      isLoggedIn: false,
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
    }
  },
  methods: {
    async fetchExercises() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/exercis');
        this.exercises = response.data;
      } catch (error) {
        console.error('Ошибка при получении данных об упражнениях:', error);
      }
    },
    
    showModal(exercise) {
      this.selectedExercise = exercise;
      this.isModalVisible = true;
    },
    closeModal() {
      this.isModalVisible = false;
    },
    closeModalOutside(event) {
      if (event.target.classList.contains('modal')) {
        this.isModalVisible = false;
      }
    },



    async isChecked(exercise) {
      const response = await axios.get('http://127.0.0.1:8000/user_exercises');
      this.userExercises = response.data;
      if (this.userExercises) {
        return this.userExercises.some(userExercise => userExercise.exercise_id === exercise.id && userExercise.is_checked);
      }
      return false;
    },
    
  },
};
</script>

<style>
/* Стили для модального окна */
.exercise
{
  display: inline-block;
    background-color: #FFFFFF;
    color: rgba(0, 0, 0);
    width: 75em;
    font-size: 15px;
    border-radius:45px;
    box-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
    margin: 1em;
    border: 1px solid #E2E2E2;
    margin-left: auto;
    margin-right: auto;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: white;
  border-radius: 45px;
  padding: 20px;
  width: 50em;
  position: relative;
  text-align: center;
}

.close {
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 24px;
  cursor: pointer;
}
</style>