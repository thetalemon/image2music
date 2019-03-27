<template>
  <div>
    <h2>↓画像↓</h2>
    <div v-if="uploadImage">
        <img :src="uploadImage">
    </div>
      <h2>↓結果↓</h2>
    <div v-if="processedImage">
        <img :src="processedImage">
    </div>
    <input type="file" @change="onFileChange">
    <p> red   : {{ ave_red }}</p>
    <p> green : {{ ave_green }}</p>
    <p> blue  : {{ ave_blue }}</p>
    <div v-if="music">
      <audio controls :src="music"></audio>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      uploadImage: '',
      processedImage: '',
      music: ''
    }
  },
  methods: {
    onFileChange (e) {
      e.preventDefault()

      var file = e.target.files[0]
      if (file && file.type.match(/^image\/(png|jpeg)$/)) {
        this.uploadImage = URL.createObjectURL(file)
      }
      const reader = new FileReader()
      reader.onload = (e) => {
        this.postFile(e.target.result)
        console.log(e.target.result)
      }
      reader.readAsDataURL(file)
    },
    postFile (fileData) {
      const pathCanny = `/api/cannyFile`
      let formData = new FormData()
      formData.append('image', fileData)
      axios.post(pathCanny, formData)
        .then(response => {
          this.processedImage = response.data.image
          this.ave_red = response.data.red
          this.ave_green = response.data.green
          this.ave_blue = response.data.blue
        })
        .catch(error => {
          console.log(error)
        })
      const pathMusic = `/api/makeMusic`
      axios.get(pathMusic)
        .then(response => {
          this.music = response.data.music
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
