<template>
    <div>

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