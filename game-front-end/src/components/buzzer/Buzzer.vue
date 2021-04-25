<template>
      <div>
        <!-- Title -->
        <div>
          <router-link class="hidden-color" to="admin">Admin</router-link>
        </div>
        <!-- <div>
          <div>
            <h1>The Game!</h1>
          </div>
        </div> -->

        <!-- Entry point -->
        <div v-if="showInput">
          <div>
            <div class="card" >
              <label for="name" class="form-label">Contestant Name</label>
              <input
                name="name"
                type="text"
                id="nameInput"
                required
                v-model="name"
              />
              <button class="btn" v-on:click="setName">Submit</button>
            </div>
          </div>
        </div>

        <!-- The Buzzer -->
        <div v-if="showPlay">
          <div>
            <img src='./buzzer.png' v-on:click="sendMessage">
          </div>
        </div>
<!-- v-on:click="sendMessage" -->
        <!-- Lost -->
        <div v-if="showLose">
          <div>
            <h2 class="center-text">
              Sorry Too late!
            </h2>
          </div>
        </div>

        <!-- Win -->
        <div v-if="showWin">
          <div>
            <h2 class="center-text">&#127881; Winner &#127881;</h2>
          </div>
        </div>
      </div>
</template>

<script>

export default {
  name: 'Buzzer',
   data() {
        return {
            connection: null,
            logIn: false,
            showWin: false, 
            showLose: false, 
            name: "Please Enter Name",
            showInput: true,
            showPlay: false,
           
        }
    },
    methods: {
        setName() {
            this.showInput = false
            this.showPlay = true
        },
        sendMessage(){
            this.connection.send(this.name)
        },
        checkWin(event){
            if(event.data == this.name) {
                this.showWin = true
                this.showPlay = false
            } else {
                this.showLose = true
                this.showPlay = false
            }
        },
        resetGame(event){
            if(event.data == "reset") {
                this.showWin = false
                this.showLose = false
                this.showPlay = true
            }
        }
    },
    created() {
        console.log("Starting connection to ws server")
        // this.connection = new WebSocket("ws://soyouthinkyouknowveeam.azurewebsites.net/");
        this.connection = new WebSocket("ws://"+location.hostname+"/api")

        this.connection.onopen = (event) => {
            console.log(event)
            console.log("Connected to server!")
        }
        this.connection.onmessage = (event) => {
            console.log(event)
            this.checkWin(event)
            this.resetGame(event)
        }
    }
}
</script>
<style scoped>
  .hidden-color {
    color: #e7e7e7
  }

</style>
