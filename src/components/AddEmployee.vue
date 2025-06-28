<script>
import { employeeBus } from '@/bus.js';
export default {
  name: 'AddEmployee',
  data() {
    return {
      empName: '',
      empEmail: '',
      empRole: '',
      errorMsg: '',
      successMsg: '',
    };
  },
  methods: {
    addEmployee() {
      this.errorMsg = '';
      this.successMsg = '';
      if (!this.empName || !this.empEmail || !this.empRole) {
        this.errorMsg = 'يرجى تعبئة جميع الحقول';
        return;
      }
      employeeBus.emit('add-employee', {
        name: this.empName,
        email: this.empEmail,
        role: this.empRole,
      });
      this.successMsg = 'تمت إضافة الموظف بنجاح!';
      this.empName = '';
      this.empEmail = '';
      this.empRole = '';
    },
  },
};
</script>

<template>
  <div class="add-employee-container">
    <h2>إضافة موظف جديد</h2>
    <form @submit.prevent="addEmployee" class="form">
      <label for="name">الاسم:</label>
      <input
        type="text"
        id="name"
        v-model="empName"
        placeholder="أدخل اسم الموظف"
        required
      />

      <label for="email">البريد الإلكتروني:</label>
      <input
        type="email"
        id="email"
        v-model="empEmail"
        placeholder="example@mail.com"
        required
      />

      <label for="role">الدور:</label>
      <select id="role" v-model="empRole" required>
        <option disabled value="">اختر الدور</option>
        <option value="مدير">مدير</option>
        <option value="موظف">موظف</option>
        <option value="محاسب">محاسب</option>
      </select>

      <button type="submit">إضافة موظف</button>

      <p v-if="errorMsg" class="error-msg">{{ errorMsg }}</p>
      <p v-if="successMsg" class="success-msg">{{ successMsg }}</p>
    </form>
  </div>
</template>

<style scoped>
.add-employee-container {
  max-width: 450px;
  background: #f9f5ff;
  padding: 25px 30px;
  border-radius: 18px;
  box-shadow: 0 4px 10px rgba(120, 80, 180, 0.15);
  margin: 30px auto;
  direction: rtl;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
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

.form input,
.form select {
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

.form input:focus,
.form select:focus {
  border-color: #8f0b13;
  outline: none;
  background-color: #fff;
}

button[type='submit'] {
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
  margin-top: -10px;
  margin-bottom: 10px;
  text-align: center;
}

.success-msg {
  color: #2a9d8f;
  font-weight: 600;
  margin-top: -10px;
  margin-bottom: 10px;
  text-align: center;
}
</style>
