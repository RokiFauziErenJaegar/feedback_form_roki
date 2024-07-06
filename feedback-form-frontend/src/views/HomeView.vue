<template>
  <div class="home">
    <!--<img alt="Vue logo" src="../assets/logo.png"> --> <!-- Komentar atau hapus baris ini -->
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/FeedbackForm.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  }
}
</script>
