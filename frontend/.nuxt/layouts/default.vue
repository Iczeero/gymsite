<template>
    

  <div>
    <div class="top_row">
  
    </div>
      
    <header id="header">
      <div class="container">
  
        <nav id="primary-nav" class="dropdown cf">
          <ul class="dropdown menu">
            <li class='menu-button' id="main"><NuxtLink to="/">Главная</NuxtLink></li>
            <li class='menu-button' id="exr"><NuxtLink to="/exercises">Упражнения</NuxtLink></li>
            <li class='menu-button' id="progs"><NuxtLink to="/programs">Программы тренировок</NuxtLink></li>
            <li class='menu-button' id="about"><NuxtLink to="/about">О нас</NuxtLink></li>
            <li class='menu-button' id="login"><NuxtLink to="/auth/user">Вход</NuxtLink></li>
          </ul>
        </nav>
  
      </div>
    </header>
      
  
  
  
      <section class="banner" id="top">
          <div class="container">
              <div class="mid_row">
                <Nuxt></Nuxt>
              </div>
          </div>
      </section>
  
  
      <div class="sub-footer">
          <p></p>
      </div>
    </div>
  </template>
  
  <style>
  @import url("~/static/main.css");
  </style>
