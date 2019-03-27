<template>
  <div>
    <h2>↓画像↓</h2>
    <div v-if="uploadImage">
        <img :src="uploadImage">
    </div>
    <input type="file" @change="onFileChange">
  </div>
</template>

<script>
export default {
  data () {
    return {
      uploadImage: ''
    }
  },
  methods: {
    onFileChange (e) {
      var file = e.target.files[0]
      if (file && file.type.match(/^image\/(png|jpeg)$/)) {
        this.uploadImage = URL.createObjectURL(file)
      }
    }
  }
}
</script>
