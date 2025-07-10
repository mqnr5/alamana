<template>
  <div class="manage-staff">
    <h1>👥 إدارة الموظفين</h1>
    <p class="desc">يمكنك هنا متابعة حالة الموظفين وتحديث معلوماتهم.</p>

    <transition-group name="fade-slide" tag="table" class="staff-table">
      <thead>
        <tr>
          <th>الاسم</th>
          <th>الحالة</th>
          <th>الإجراء</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="staff in staffList" :key="staff.id">
          <td>{{ staff.name }}</td>
          <td>{{ staff.status }}</td>
          <td class="staff-actions">
            <button @click="edit(staff)">✏️ تعديل</button>
            <button @click="addTask(staff)">➕ إضافة مهمة</button>
          </td>
        </tr>
      </tbody>
    </transition-group>

    <button class="back-btn" @click="$router.go(-1)">↩️ رجوع</button>
  </div>
</template>

<script>
export default {
  name: 'ManageStaffView',
  data() {
    return {
      staffList: [
        { id: 1, name: 'علي حسن', status: 'نشط' },
        { id: 2, name: 'سارة محمد', status: 'إجازة' },
        { id: 3, name: 'مريم عبد الله', status: 'منقطع' }
      ]
    };
  },
  methods: {
    edit(staff) {
      this.$router.push({ name: 'EditEmpInfo', query: { id: staff.id } });
    },
    addTask(staff) {
      this.$router.push({ name: 'AddTask', query: { id: staff.id } });
    }
  }
};
</script>

<style scoped>
.manage-staff {
  padding: 40px 25px;
  max-width: 1000px;
  margin: auto;
  background-color: #fefefe;
  border-radius: 16px;
  box-shadow: 0 8px 18px rgba(0, 0, 0, 0.07);
  font-family: 'Tajawal', sans-serif;
  direction: rtl;
  text-align: center;
}

h1 {
  font-size: 30px;
  color: #2d2d6e;
  margin-bottom: 10px;
}
.desc {
  font-size: 16px;
  color: #666;
  margin-bottom: 25px;
}

.staff-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 30px;
}
.staff-table th,
.staff-table td {
  padding: 12px 16px;
  border-bottom: 1px solid #ddd;
  text-align: center;
}
.staff-table th {
  background-color: #f0f0f8;
  color: #444;
  font-weight: bold;
}
.staff-table td {
  color: #333;
}
.staff-actions {
  display: flex;
  flex-direction: row;
  justify-content: center;
  gap: 30px;
}

button {
  background-color: #3b3b99;
  color: white;
  padding: 8px 18px;
  border: none;
  border-radius: 10px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}
button:hover {
  background-color: #25257c;
}

.back-btn {
  background-color: #a40033;
}
.back-btn:hover {
  background-color: #7b0028;
}

.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.4s ease;
}
.fade-slide-enter-from,
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(15px);
}
</style>
