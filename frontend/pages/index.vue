<template>
<div>
  <div class="myPrograms"> 
    <div v-if="isAuthenticated">
      <div class="block-label">
      <a>Ваши программы тренировок!</a>
      </div>
      <div class="block-label">
      <a>Ваши упражнения!</a>
    </div>
    </div>
  <div v-else>
    <div class="block-label">
      <a>У нас тут тренировки!</a>
    </div>
    <div class="block-label">
      <a>У нас тут упражнения!</a>
    </div>
  </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'IndexPage',
  computed:{
    isAuthenticated(){
      return this.$auth.loggedIn
    },
  }
}
</script>

<style>
.block-label
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
    text-align: center;
}
</style>
