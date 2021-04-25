<template>
  <div>
    <!-- Title -->
    <!-- <div>
      <div>
        <h1>The Game!</h1>
      </div>
    </div> -->

    <!-- Entry point -->
    <div>
      <div class="card">
        <div>
          <h3>
            The Current State is: {{ currentState ? "In Play" : "Winner" }}
          </h3>
          <h5 v-if="!currentState">Winner was {{ winnerName }}</h5>
        </div>

      </div>
    </div>
    <div>
       <button class="btn" v-bind:disabled="currentState" v-on:click="sendMessage">
          Reset
        </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "Admin",
  data() {
    return {
      connection: null,
      currentState: true,
      winnerName: "TBC",
    };
  },
  methods: {
    setName() {
      this.showInput = false;
      this.showPlay = true;
    },
    checkWin(event) {
      if (event.data !== "") {
        this.currentState = false;
        this.winnerName = event.data;
      }
    },
    checkReset(event) {
      if (event.data === "reset") {
        this.currentState = true;
        this.winnerName = "TBC";
      }
    },
    sendMessage() {
      this.connection.send("reset");
    },
  },
  created() {
    console.log("Starting connection to ws server");
    // this.connection = new WebSocket("ws://soyouthinkyouknowveeam.azurewebsites.net/");
    this.connection = new WebSocket("ws://"+location.hostname+"/api");

    this.connection.onopen = (event) => {
      console.log(event);
      console.log("Connected to server!");
    };

    this.connection.onmessage = (event) => {
      console.log(event);
      this.checkWin(event);
      this.checkReset(event);
    };
  },
};
</script>
<style>
.h1 {
  font-family: 'Courier New', Courier, monospace;
}

</style>
