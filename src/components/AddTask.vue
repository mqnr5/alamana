<script>
import { add_task, get_user_by_id } from '@/api/public_operations';

export default {
    name: 'AddTask',
    data() {
        return {
            user: null,
            username: '',
            title: '',
            text: '',
            deadline_date: '',
            errorMsg: '',
            successMsg: ''
        }
    },
    methods: {
      async addTask(title, text, deadline_date) {
        await add_task({
          user_id: this.user.id,
          title: title,
          text: text,
          deadline_date: deadline_date,
          status: 'pending'
        })
      }
    },
    async mounted() {
        this.user = await get_user_by_id(3);
        this.username = this.user.name;
    }
}
</script>
<template>
    <div class="add-task-container">
        <h2>إضافة مهمة جديدة الى {{ username }}</h2>
        <form @submit.prevent="addTask" class="form">
            <label for="mission-title">عنوان المهمة :</label>
            <input
                type="text"
                id="mission-title"
                v-model="title"
                required
            />
            <label for="mission-text">نص المهمة :</label>
            <input
                type="text"
                id="mission-text"
                v-model="text"
                required
            />

            <label for="mission-deadline">تاريخ الانتهاء :</label>
            <input
                type="date"
                id="mission-deadline"
                v-model="deadline_date"
                required
            />

            <button @click="addTask">إضافة مهمة</button>

            <p v-if="errorMsg" class="error-msg">{{ errorMsg }}</p>
            <p v-if="successMsg" class="success-msg">{{ successMsg }}</p>
        </form>
    </div>
</template>
<style scoped>
.add-task-container {
  max-width: 450px;
  background: #f9f5ff;
  padding: 25px 50px;
  justify-content: center;
  border-radius: 18px;
  box-shadow: 0 4px 10px 
  rgba(120, 80, 180, 0.15);
  margin: 30px auto;
  direction: rtl;
  font-family: 'Segoe UI', Tahoma, 
      Geneva, Verdana, sans-serif;
  color: #4a3f6e;
  text-align: right;
}

h2 {
  margin-bottom: 20px;
  color: #6d7cd9;
  font-weight: 700;
  text-align: center;
}

.form label {
  display: block;
  margin-bottom: 6px;
  font-weight: 600;
  font-size: 14px;
  color: #6d7cd9;
}

.form input {
  width: 100%;
  padding: 10px 14px;
  margin-bottom: 18px;
  border: 2px solid #c1a3f2;
  border-radius: 12px;
  font-size: 15px;
  color: #4a3f6e;
  background-color: #f9f5ff;
  transition: border-color 0.3s ease;
}

input[id="mission-text"] {
    height: 100px;
}

.form input:focus {
  border-color: #8f0b13;
  outline: none;
  background-color: #fff;
}

button {
  width: 100%;
  padding: 12px 0;
  background-color: #8f0b13;
  border: none;
  border-radius: 15px;
  color: #f9f5ff;
  font-weight: 700;
  font-size: 17px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button[type='submit']:hover {
  background-color: #b13641;
}

.error-msg {
  color: #d94f4f;
  font-weight: 600;
  margin-top: 10px;
  margin-bottom: 10px;
  text-align: center;
}

.success-msg {
  color: #2a9d8f;
  font-weight: 600;
  margin-top: 10px;
  margin-bottom: 10px;
  text-align: center;
}
</style>