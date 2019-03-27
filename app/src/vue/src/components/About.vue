<template>
  <div>
    <p>Home page</p>
    <p> num: <input v-model="formData.val1" placeholder="number"></p>
    <p> number is: {{ returnVal }} </p>
    <button @click="getDoubleScore">Calc double score</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      formData: {
        val1: 0
      },
      returnVal: 0
    }
  },
  methods: {
    getDoubleScore () {
      this.val1 = this.getDoubleScoreFromBackend()
    },
    getDoubleScoreFromBackend () {
      const path = `/api/testpost`
      axios.post(path, this.formData)
        .then(response => {
          this.returnVal = response.data.result
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
