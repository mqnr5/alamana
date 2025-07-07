<template>
  <transition name="fade-slide">
    <div class="edit-employee-container">
      <h2>تعديل معلومات الموظف</h2>
      
      <form @submit.prevent="saveEmpInfo" class="form">
      <label for="name">الاسم:</label>
      <input
        type="text"
        id="name"
        v-model="EmpName"
        :placeholder="EmpName"
        required
      />

      <label for="email">البريد الإلكتروني:</label>
      <input
        type="email"
        id="email"
        v-model="EmpEmail"
        :placeholder="EmpEmail"
        required
      />

      <label for="password">كلمة السر:</label>
      <input
        type="password"
        id="password"
        v-model="EmpPassword"
        :placeholder="EmpPassword"
      />

      <label for="department">القسم:</label>
      <select id="department" v-model="EmpDepartment">
        <option disabled value="">اختر القسم</option>
        <option v-for="department in departments" 
        :key="department.id" 
        :value="department.id">
          {{ department.name }}
        </option>
      </select>

      <label for="role">الدور:</label>
      <select id="role" v-model="empRole" required>
        <option disabled value="">اختر الدور</option>
        <option value="مدير">مدير</option>
        <option value="موظف">موظف</option>
        <option value="محاسب">محاسب</option>
      </select>

        <button type="submit">💾 حفظ المعلومات</button>
      </form>

      <div v-if="toastMessage" :class="['toast', toastType]">
        {{ toastMessage }}
      </div>
    </div>
  </transition>
</template>

<script>
import { get_user_by_id } from '@/api/public_operations';
import { employeeBus } from '@/bus';

export default {
  name: 'EditEmpInfo',
  props: {
    userId: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      EmpName: '',
      EmpEmail: '',
      empPassword: '',
      empDepartment: 0,
      EmpRole: '',
      empStatus: '',
      toastMessage: '',
      toastType: '',
      listener: null
    };
  },
  methods: {
    saveEmpInfo() {
      if (!this.EmpName || !this.EmpEmail || !this.EmpRole) {
        this.showToast('يرجى ملء جميع الحقول', 'error');
        return;
      }
      this.showToast('✅ تم حفظ المعلومات بنجاح', 'success');
    },
    showToast(msg, type = 'success') {
      this.toastMessage = msg;
      this.toastType = type;
      setTimeout(() => {
        this.toastMessage = '';
      }, 3000);
    },
  },
  async mounted() {
    const user = await get_user_by_id(this.userId);
    this.EmpName = user?.name || '';
    this.EmpEmail = user?.email || '';
    this.EmpPassword = user?.password || '';
    this.EmpDepartment = user?.department || 0;
    this.EmpRole = user?.role || '';
    this.EmpStatus = user?.status || '';
  },
  beforeUnmount() {
    employeeBus.off('old-employee-info', this.listener);
  }
};
</script>

<style scoped>
.edit-employee-container {
  max-width: 480px;
  background: #f9f5ff;
  padding: 30px;
  border-radius: 20px;
  box-shadow: 0 5px 15px rgba(120, 80, 180, 0.2);
  margin: 40px auto;
  direction: rtl;
  font-family: 'Tajawal', sans-serif;
  color: #4a3f6e;
  animation: fadeIn 0.8s ease;
}

h2 {
  margin-bottom: 25px;
  color: #6d7cd9;
  font-weight: 800;
  text-align: center;
}

.form label {
  font-weight: 600;
  margin-bottom: 6px;
  display: block;
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
  background-color: #fefeff;
  transition: border-color 0.3s ease;
}

.form input:focus,
.form select:focus {
  border-color: #ff9933;
  background-color: #fff;
  outline: none;
}

button[type='submit'] {
  width: 100%;
  padding: 12px 0;
  background-color: #ff9933;
  border: none;
  border-radius: 15px;
  color: white;
  font-weight: 700;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button[type='submit']:hover {
  background-color: #e67e22;
}

.toast {
  margin-top: 15px;
  padding: 12px;
  border-radius: 10px;
  text-align: center;
  font-weight: 600;
  animation: fadeIn 0.5s;
}

.toast.success {
  background-color: #d1f7c4;
  color: #275d2c;
}

.toast.error {
  background-color: #fcdede;
  color: #941515;
}

.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.5s ease;
}
.fade-slide-enter-from {
  opacity: 0;
  transform: translateY(20px);
}
.fade-slide-enter-to {
  opacity: 1;
  transform: translateY(0);
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
