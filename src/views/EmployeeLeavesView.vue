<template>
  <div class="leave-container">
    <header class="leave-header">
      <h1>سجل الإجازات</h1>
      <p>استعرض وسجل كل إجازاتك بتفاصيل دقيقة</p>
    </header>

    <div class="actions-bar">
      <select v-model="selectedStatus">
        <option value="">جميع الحالات</option>
        <option>مقبولة</option>
        <option>مرفوضة</option>
        <option>قيد الانتظار</option>
      </select>
      <button @click="showForm = !showForm">➕ إضافة طلب إجازة</button>
    </div>

    <transition name="slide-fade">
      <form v-if="showForm" @submit.prevent="submitLeave" class="leave-form">
        <input v-model="newLeave.title" type="text" placeholder="عنوان الإجازة" required />
        <input v-model="newLeave.date" type="date" required />
        <textarea v-model="newLeave.notes" placeholder="تفاصيل إضافية"></textarea>
        <button type="submit">📤 إرسال</button>
      </form>
    </transition>

    <transition-group name="fade-up" tag="div" class="leave-grid">
      <div
        class="leave-card"
        v-for="leave in filteredLeaves"
        :key="leave.id"
        :class="leave.status"
      >
        <h4>{{ leave.title }}</h4>
        <p><strong>📅</strong> {{ leave.date }}</p>
        <p><strong>📝</strong> {{ leave.details }}</p>
        <span>{{ leave.status }}</span>
      </div>
    </transition-group>
  </div>
</template>

<script>
import { add_leave } from '@/api/public_operations';

export default {
  name: 'EmployeeLeavesView',
  data() {
    return {
      showForm: false,
      selectedStatus: '',
      leaves: [],
      newLeave: {
        title: '',
        date: '',
        notes: '',
        status: 'قيد الانتظار'
      }
    };
  },
  computed: {
    filteredLeaves() {
      return this.selectedStatus
        ? this.leaves.filter(l => l.status 
        === this.selectedStatus) : this.leaves;
    }
  },
  methods: {
    async submitLeave() {
      const uid = parseInt(localStorage.getItem('loggedIn'));
      this.newLeave = {
        user_id: uid,
        ...this.newLeave
      }
      await add_leave(this.newLeave);
      this.resetForm();
    },
    resetForm() {
      this.newLeave = {
        user_id: 0,
        title: '',
        leave_date: '',
        details: '',
        status: 'قيد الانتظار'
      };
      this.showForm = false;
    },
    getStatusClass(status) {
      return {
        'مقبولة': 'approved',
        'مرفوضة': 'rejected',
        'قيد الانتظار': 'pending'
      }[status];
    },
  },
  mounted() {
  }
};
</script>

<style scoped>
.leave-container {
  max-width: 1000px;
  margin: auto;
  padding: 35px;
  background: linear-gradient(135deg, #fffaf4, #fff0e6);
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(255, 192, 70, 0.3);
  direction: rtl;
  font-family: 'Tajawal', sans-serif;
  color: #3c3c3c;
  animation: fadeIn 1s ease;
}

.leave-header {
  text-align: center;
  margin-bottom: 30px;
}

.leave-header h1 {
  font-size: 32px;
  color: #ff7f0f;
  margin-bottom: 10px;
}

.leave-header p {
  color: #888;
}

.actions-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 25px;
  gap: 15px;
}

.actions-bar select,
.actions-bar button {
  padding: 10px 14px;
  border-radius: 12px;
  border: 1.5px solid #ffd599;
  font-size: 15px;
}

.actions-bar button {
  background-color: #ffb74d;
  color: white;
  font-weight: bold;
  transition: 0.3s ease;
}

.actions-bar button:hover {
  background-color: #fb8c00;
}

.leave-form {
  display: flex;
  flex-direction: column;
  gap: 12px;
  background: #fff9f0;
  padding: 20px;
  border-radius: 15px;
  box-shadow: 0 6px 18px rgba(255, 193, 7, 0.2);
  margin-bottom: 25px;
}

.leave-form input,
.leave-form textarea {
  padding: 12px;
  border-radius: 10px;
  border: 1.5px solid #ffc046;
  font-size: 16px;
}

.leave-form button {
  background-color: #ffa726;
  color: white;
  border: none;
  padding: 12px;
  border-radius: 10px;
  font-weight: bold;
  transition: 0.3s;
}

.leave-form button:hover {
  background-color: #fb8c00;
}

.leave-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
}

.leave-card {
  background-color: #fff7ed;
  border: 2px dashed #ffc046;
  border-radius: 16px;
  padding: 20px;
  transition: transform 0.3s;
}

.leave-card:hover {
  transform: translateY(-6px);
}

.leave-card h4 {
  margin-bottom: 10px;
  color: #ff7f0f;
}

.leave-card span {
  display: inline-block;
  margin-top: 10px;
  padding: 6px 14px;
  border-radius: 10px;
  font-weight: 600;
  font-size: 14px;
}

.approved {
  background: #c8e6c9;
  color: #2e7d32;
}

.rejected {
  background: #ffcccb;
  color: #c62828;
}

.pending {
  background: #fff3cd;
  color: #856404;
}

@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: translateY(20px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

.fade-up-enter-active,
.fade-up-leave-active {
  transition: all 0.5s ease;
}
.fade-up-enter-from,
.fade-up-leave-to {
  opacity: 0;
  transform: translateY(10px);
}

.slide-fade-enter-active {
  transition: all 0.5s ease;
}
.slide-fade-enter-from {
  opacity: 0;
  transform: translateY(-10px);
}
</style>
