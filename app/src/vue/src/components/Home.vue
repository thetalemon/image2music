<template>
  <div>
    <p>Home page</p>
    <p>Random number from backend: {{ randomNumber }}</p>
    <p> num: <input v-model="val1" placeholder="number"></p>
    <p> number is: {{ val1*2 }} </p>
    <button @click="getRandom">New random number</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      randomNumber: 0,
      val1: 0
    }
  },
  methods: {
    getRandom () {
      this.randomNumber = this.getRandomFromBackend()
    },
    getRandomFromBackend () {
      const path = `/api/random`
      axios.get(path)
        .then(response => {
          this.randomNumber = response.data.randomNumber
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created () {
    this.getRandom()
  }
}
</script>
