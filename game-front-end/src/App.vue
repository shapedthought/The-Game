<template>
  <main>  
    <router-view></router-view>
  </main>
</template>

<script>

export default {
  name: 'App',
  components: {
  }
}
</script>

<style>
body{
  font-family:Arial, Helvetica, sans-serif;
  background-color: #e7e7e7;
}
h1 {
  text-align: center;
}
.card {
  background-color: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  margin-top: 100px;
  margin-left: auto;
  margin-right: auto;
  border-radius: 15px;
  padding: 1rem;
  text-align: center;
  width: 80%;
  max-width: 40rem;
}
.btn {
  all: unset;
  display: block;
  margin: 10px auto;
  font-family:Arial, Helvetica, sans-serif;
  color: white;
  font-size: 20px;
  padding: 5px 10px;
  background: #dc3545;
  cursor: pointer;
  border-radius: 5px;
}
.btn:hover, .btn:focus, .btn:active {
  background: #bd2e3c;
}
input {
  width: 90%;
  padding: 9px 10px;
  font-size: 15px;
  margin: 8px 0;
  border: 1px solid rgb(216, 216, 216);
  border-radius: 4px
}
.center-text {
  text-align: center;
}
img { 
  display: block;
  margin: auto;
  cursor: pointer;
  margin-top: 100px;
  border: 1px solid rgb(141, 141, 141);
  border-radius: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  transition: transform .2s;
}
img:hover {
  transform: scale(1.1)
}

</style>
