<template>
  <div class="login-wrapper">
    <div class="login-box">
      <h2>🔐 تسجيل الدخول</h2>

      <form @submit.prevent="login">
        <label for="username">👤 اسم المستخدم</label>
        <input type="text" v-model="username" id="username" required />

        <label for="password">🔑 كلمة المرور</label>
        <input type="password" v-model="password" id="password" required />

        <button type="submit">دخول ➡️</button>
      </form>

      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      username: '',
      password: '',
      errorMessage: ''
    }
  },
  methods: {
   login() {
  if (this.username === 'admin' && this.password === '1234') {
    localStorage.setItem('loggedIn', 'true');
    this.$router.push('/');
  } else {
    this.errorMessage = '❌ اسم المستخدم أو كلمة المرور غير صحيحة';
  }


    }
  }
}
</script>

<style scoped>
.login-wrapper {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(145deg, #fafafa, #eaeaea);
  font-family: 'Tajawal', sans-serif;
  direction: rtl;
}

.login-box {
  background: white;
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 12px 20px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
  text-align: center;
  color: #2e2e2e;
}

h2 {
  color: #3b3b99;
  margin-bottom: 30px;
  font-size: 28px;
}

form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

label {
  text-align: right;
  font-weight: bold;
  color: #0b1957;
}

input {
  padding: 10px;
  border: 2px solid #dedede;
  border-radius: 10px;
  font-size: 16px;
}

button {
  background-color: #a40033;
  color: white;
  padding: 12px;
  font-weight: bold;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  font-size: 18px;
  transition: background-color 0.3s ease;
}
button:hover {
  background-color: #6c0024;
}

.error {
  color: #a40033;
  margin-top: 15px;
  font-weight: bold;
}
</style>
