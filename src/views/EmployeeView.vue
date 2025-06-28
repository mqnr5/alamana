<template>
  <div class="employee-dashboard">
    <div class="header">
      <img :src="user.photo" alt="User Photo" class="avatar" />
      <div class="info">
        <h2>{{ user.name }}</h2>
        <p>{{ user.department }} | {{ user.role }}</p>
        <small>آخر تسجيل دخول: {{ user.lastLogin }}</small>
      </div>
    </div>

    <section class="stats">
      <div class="stat" v-for="stat in statistics" :key="stat.label">
        <div class="number">{{ stat.value }}</div>
        <div class="label">{{ stat.label }}</div>
      </div>
    </section>

    <section class="tasks">
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

    <section class="notifications">
      <h3>الإشعارات</h3>
      <ul>
        <li v-for="note in notifications" :key="note.id">🔔 {{ note.message }}</li>
      </ul>
    </section>

    <section class="attendance">
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

    <button class="export">📤 تصدير السجل</button>
  </div>
</template>

<script>
export default {
  name: 'EmployeeDashboard',
  data() {
    return {
      user: {
        name: 'محمد علي',
        department: 'الدعم الفني',
        role: 'موظف',
        photo: 'https://i.imgur.com/6VBx3io.png',
        lastLogin: '2025-06-27 08:00AM'
      },
      statistics: [
        { label: 'عدد المهام', value: 12 },
        { label: 'مهام مكتملة', value: 8 },
        { label: 'نسبة الإنجاز', value: '66%' },
        { label: 'طلبات مرسلة', value: 3 }
      ],
      tasks: [
        { id: 1, title: 'تحديث قاعدة البيانات', status: 'قيد التنفيذ' },
        { id: 2, title: 'الرد على التذاكر', status: 'مكتملة' }
      ],
      notifications: [
        { id: 1, message: 'تم تعيين مهمة جديدة لك.' },
        { id: 2, message: 'موعد تسليم المهمة خلال 3 ساعات.' }
      ],
      attendance: [
        { date: '2025-06-25', status: '✔️ حضور' },
        { date: '2025-06-26', status: '❌ غياب' }
      ]
    };
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

.info h2 {
  margin: 0;
  font-size: 24px;
}

.stats {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  margin: 30px 0;
}

.stat {
  flex: 1 1 22%;
  background-color: #e9f3ff;
  padding: 20px;
  text-align: center;
  border-radius: 12px;
  box-shadow: 0 0 10px rgba(0,0,0,0.05);
}

.number {
  font-size: 26px;
  font-weight: bold;
}

.tasks ul,
.notifications ul {
  list-style: none;
  padding: 0;
}

.tasks li,
.notifications li {
  background-color: #f7f4ed;
  margin-bottom: 10px;
  padding: 12px;
  border-radius: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
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
</style>
