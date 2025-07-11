<template>
  <div class="employee-dashboard">
    <div class="header">
      <div class="info">
        <h2>{{ user.name }}</h2>
        <p>{{ user.department }} | {{ user.role }}</p>
        <small>آخر تسجيل دخول: {{ user.lastLogin }}</small>
      </div>
    </div>

    <!-- ✅ التبويبات -->
    <div class="tabs">
      <button v-for="tab in tabs" :key="tab.name" :class="{ active: currentTab === tab.name }" @click="currentTab = tab.name">
        {{ tab.label }}
      </button>
    </div>

    <transition name="fade" mode="out-in">
      <div :key="currentTab">
        <!-- ✅ المهام اليومية -->
        <section v-if="currentTab === 'tasks'" class="section-content">
          <h3>المهام اليومية</h3>
          <ul>
            <li v-for="task in tasks" :key="task.id">
              <span>{{ task.title }}</span>
              <select v-model="task.status">
                <option>قيد التنفيذ</option>
                <option>مكتملة</option>
                <option>متأخرة</option>
              </select>
            </li>
          </ul>
          <router-link to="/Tasks" class="task-link">📋 عرض كل المهام</router-link>
        </section>

        <!-- ✅ الإشعارات -->
        <section v-else-if="currentTab === 'notifications'" class="section-content">
          <h3>الإشعارات</h3>
          <ul>
            <li v-for="note in notifications" :key="note.id">🔔 {{ note.message }}</li>
          </ul>
        </section>

        <!-- ✅ الحضور -->
        <section v-else-if="currentTab === 'attendance'" class="section-content">
          <h3>سجل الحضور</h3>
          <table>
            <thead>
              <tr>
                <th>التاريخ</th>
                <th>الحالة</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="record in attendance" :key="record.date">
                <td>{{ record.date }}</td>
                <td>{{ record.status }}</td>
              </tr>
            </tbody>
          </table>
        </section>

        <!-- ✅ الإجازات -->
        <section v-else-if="currentTab === 'leaves'" class="section-content">
          <h3>الإجازات</h3>
          <router-link to="/EmployeeLeaves" class="task-link">📅 عرض الإجازات</router-link>
        </section>
      </div>
    </transition>

    <button class="export">📤 تصدير السجل</button>
  </div>
</template>

<script>
import { get_notifications } from '@/api/public_operations';

export default {
  name: 'EmployeeDashboard',
  data() {
    return {
      currentTab: 'tasks',
      tabs: [
        { name: 'tasks', label: 'المهام' },
        { name: 'notifications', label: 'الإشعارات' },
        { name: 'attendance', label: 'الحضور' },
        { name: 'leaves', label: 'الإجازات' }
      ],
      user: {
        name: 'محمد علي',
        department: 'الدعم الفني',
        role: 'موظف',
        lastLogin: '2025-06-27 08:00AM'
      },
      notifications: [],
      attendance: []
    };
  },
  async mounted() {
    const uid = localStorage.getItem('loggedIn')
    this.notifications = await get_notifications(uid)
    
  }
};
</script>

<style scoped>
.employee-dashboard {
  background-color: #ffffff;
  color: #0b1957;
  padding: 30px;
  border-radius: 15px;
  max-width: 1000px;
  margin: auto;
  font-family: 'Tajawal', sans-serif;
  direction: rtl;
  text-align: right;
}

.header {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 30px;
}

.avatar {
  width: 90px;
  height: 90px;
  border-radius: 50%;
  border: 4px solid #d2b3db;
}

.info h2 { margin: 0; font-size: 24px; }

.tabs {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-bottom: 25px;
}

.tabs button {
  background-color: #e9f3ff;
  color: #0b1957;
  border: none;
  padding: 10px 20px;
  border-radius: 12px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s;
}

.tabs button.active,
.tabs button:hover {
  background-color: #ffc046;
  color: white;
}

.section-content {
  animation: fadeIn 0.4s ease-in-out;
}

.task-link {
  display: inline-block;
  margin-top: 10px;
  color: #A40033;
  font-weight: bold;
  text-decoration: underline;
  cursor: pointer;
  transition: 0.3s;
}
.task-link:hover {
  color: #4E5174;
}

.attendance table {
  width: 100%;
  background-color: #f7f4ed;
  border-radius: 10px;
  overflow: hidden;
  border-collapse: collapse;
  margin-top: 10px;
}

.attendance th,
.attendance td {
  padding: 12px;
  border: 1px solid #e9f3ff;
  text-align: center;
}

.export {
  background-color: #A40033;
  color: white;
  padding: 12px 25px;
  border: none;
  border-radius: 10px;
  font-weight: bold;
  display: block;
  margin: 30px auto 0 auto;
  transition: background-color 0.3s ease;
}
.export:hover {
  background-color: #4E5174;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.4s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>
