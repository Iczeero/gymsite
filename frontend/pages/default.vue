<template>
    

  <div>
    <div class="top_row">
  
    </div>
      
    <header id="header">
      <div class="container">
  
        <nav id="primary-nav" class="dropdown cf">
          <ul class="dropdown menu">
            <li class='menu-button' id="main"><nuxt-link to="/">Главная</nuxt-link></li>
            <li class='menu-button' id="exr"><nuxt-link to="/exercises">Упражнения</nuxt-link></li>
            <li class='menu-button' id="progs"><nuxt-link to="/programs">Программы тренировок</nuxt-link></li>
            <li class='menu-button' id="about"><nuxt-link to="/about">О нас</nuxt-link></li>
            <li class='menu-button' id="login"><nuxt-link to="/auth/user">Вход</nuxt-link></li>
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
  body {
    font-family: 'Raleway', 'sans-serif';
    background-color: #fff;
  }
  
  ul {
    list-style: none;
    margin: 0;
    padding: 0;
  }
  
  p {
    font-size: 13px;
    color: #7a7a7a;
    line-height: 24px;
    left: 0.25px;
  }
  
  .top_row
  {
    display: inline-block;
    width: 100%;
    padding: 0px 0px;
  }
  
  .menu-button a {
    display: inline-block;
    background-color: #FFFFFF;
    color: #fff;
    width: 188px;
    font-size: 15px;
    border-radius:45px;
    box-shadow: 0 4px 4px rgba(0, 0, 0, 0.25);
    text-decoration: none;
    border: 1px solid #E2E2E2;
  }
  
  .menu li {
    float: left;
    margin-left: 30px;
  
    line-height: 100px;
  }
  
  #primary-nav li a {
    color: #121212;
    font-weight: bold;
    line-height: 100px;
    font-size: 15px;
    font-weight: 400;
    transition: all 0.5s;
    text-align: center;
  }
  
  #primary-nav li > a:hover,
  #primary-nav li.selected > a {
    color: #FFFFFF;
    background-color: #3F3F3F;
    border: 1px solid #3F3F3F;
    text-decoration: none;
  
  }
  
  .sub-footer
  {
    display: inline-block;
    position: absolute;
    bottom: 0;
    left: 0;
    background-color: #3F3F3F;
    padding: 40px 0px;
    width: 100%;
  }
  </style>

