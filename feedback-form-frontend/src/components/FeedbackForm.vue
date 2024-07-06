<template>
  <div class="rating-box">
    <h1>Rate Our Service?</h1>
    <p>Give us a quick rating so we know if you like it.</p>
    <div class="stars">
      <div
        v-for="star in 5"
        :key="star"
        @click="setRating(star)"
        :class="{ 'active': star <= rating }"
        class="star-item"
      >
        <i class="bx bxs-star"></i>
        <span>{{ star }}</span> <!-- Menampilkan nomor rating -->
      </div>
    </div>
    <button @click="submitFeedback">Submit</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      rating: 0 // Default rating
    };
  },
  methods: {
    setRating(rating) {
      this.rating = rating;
    },
    async submitFeedback() {
      try {
        await axios.post('http://localhost:8080/feedback/', {
          rating: this.rating
        });
        alert('Feedback submitted successfully');
      } catch (error) {
        console.error('Error submitting feedback:', error);
        alert('Failed to submit feedback');
      }
    }
  }
};
</script>

<style scoped>
.rating-box {
  width: 470px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: relative;
  padding: 70px 50px;
  border-radius: 40px;
  background: linear-gradient(-60deg, #ffffff90, #ffffffff);
  border: solid 5px transparent;
  background-clip: padding-box;
  box-shadow: 0 10px 10px rgba(46, 54, 68, .1);
}

.rating-box h1 {
  font-size: 25px;
  line-height: 25px;
  font-weight: 700;
  margin-bottom: 10px;
  color: var(--black);
  text-transform: capitalize;
  text-align: center;
}

.rating-box p {
  font-size: 15px;
  color: var(--grey);
  margin-bottom: 40px;
  text-align: center;
}

.stars {
  display: flex;
  align-items: center;
  gap: 15px;
}

.star-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
}

.star-item span {
  font-size: 12px;
  color: var(--grey);
  margin-top: 5px;
}

.stars i {
  color: var(--grey);
  font-size: 40px;
  cursor: pointer;
  transition: color .2s ease;
}

.stars .active i {
  color: var(--yellow);
}
</style>
