<template>
    <div  id="form">
      <label id="form-label">Добавить упражнение</label>
      <div id="form-text">
      <form @submit.prevent="submitForm">
        <div id="form-field">
          <label>Название</label>
          <input type="text" v-model="exercis.name" />
        </div>
        <div id="form-field">
          <label>Описание</label>
          <input type="text" v-model="exercis.discription" />
        </div>
        <div id="form-field">
          <label>Тип</label>
          <input type="text" v-model="exercis.group"/>
        </div>
        <div id="form-field">
          <label>Изображение</label>
          <input type="text" v-model="exercis.img"/>
        </div>
        <div id="form-button">
          <button type="submit">Добавить</button>
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
  

    
  
    data() {
      return {
        exercis: {
          name: '',
          discription: '',
          group: '',
          img: '',
        }
      }
    },
    methods: {
      async submitForm() {
        try {
          let response = await this.$axios.$post('addExercise', this.exercis)
        } catch (err) {
          console.log(err)
        }
      }
    }
  }
  </script>