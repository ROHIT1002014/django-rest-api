<template>
  <div class="about">
    <ul>
      <li v-for="post in posts" :key="post.id">
          <h1>
            {{ post.id }}
          </h1>
          <h1>
            {{ post.title }}
          </h1>
          <p>
            {{ post.body }}
          </p>
      </li>
    </ul>
  </div>
</template>
<script>
import axios from 'axios';
export default {
  data() {
    return {
      posts: [],
      errors: []
    }
  },
 created() {
    axios.get(`http://127.0.0.1:8000/api/`)
    .then(response => {
      // JSON responses are automatically parsed.
      this.posts = response.data
      console.log(this.posts)
    })
    .catch(e => {
      this.errors.push(e)
    })
  },
}
</script>