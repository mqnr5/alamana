<template>
  <div class="users-container">
    <h2>إدارة المستخدمين</h2>

    <button @click="addUserVisible = !addUserVisible" class="add-user-button">
      <span v-if="!addUserVisible">➕ إضافة مستخدم</span>
      <span v-else>➖ إخفاء نموذج المستخدم</span>
    </button>
    <div class="add-user-form" :hidden="!addUserVisible">
      <AddEmployee />
    </div>
    <table class="users-table">
      <thead>
        <tr>
          <th>الاسم</th>
          <th>البريد الإلكتروني</th>
          <th>الدور</th>
          <th>الإجراءات</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in users" :key="user.id">
          <td>{{ user.name }}</td>
          <td>{{ user.email }}</td>
          <td>{{ user.role }}</td>
          <td class="actions">
            <button @click="editEmpInfo(user)" class="edit-btn">تعديل</button>
            <button @click="deleteUser(user)" class="delete-btn">حذف</button>
          </td>
        </tr>
      </tbody>
    </table>
    <ExportData :exportData="users" />
  </div>
</template>

<script>
import AddEmployee from '@/components/AddEmployee.vue';
import { employeeBus } from '@/bus';
import ExportData from '@/components/ExportData.vue';
import { delete_user, get_users } from '@/api/public_operations';

export default {
  name: "ManageUsers",
  components: {
    AddEmployee,
    ExportData
  },
  data() {
    return {
      addUserVisible: false,
      users: [],
    };
  },
  methods: {
    async deleteUser(user) {
      await delete_user(user.id)
    },
    editEmpInfo(user) {
       this.$router.push({ name: 'EditEmpInfoView', params: { uid: user.id } })
    }
  },
  async mounted() {
    this.users = await get_users()
    employeeBus.on('add-employee', () => this.addUserVisible = false)
  },
  beforeMount() {
    employeeBus.off('old-employee-info')
    employeeBus.off('add-employee')
  }
};
</script>
<style scoped>
.users-container {
  background-color: #ffffff;
  padding: 30px;
  border-radius: 15px;
  max-width: 1000px;
  direction: rtl;
  margin: 20px auto;
  box-shadow: 0 0 15px rgba(210, 179, 219, 0.4);
  color: #0b1957;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

h2 {
  color: #0b1957;
  text-align: center;
  margin-bottom: 20px;
  font-weight: 700;
  font-size: 26px;
}

.add-user-button {
  background-color: #d2b3db;
  border: none;
  padding: 10px 20px;
  color: #0b1957;
  font-weight: 700;
  border-radius: 10px;
  margin-bottom: 25px;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(210, 179, 219, 0.6);
  transition: background-color 0.3s ease, color 0.3s ease;
}
.add-user-button:hover {
  background-color: #A40033;
  color: #f7f4ed;
}

.users-table {
  width: 100%;
  border-collapse: collapse;
  background-color: #f7f4ed;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(210, 179, 219, 0.3);
  overflow: hidden;
}
.users-table th,
.users-table td {
  padding: 14px 18px;
  text-align: center;
  border: 1px solid #e9f3ff;
  color: #0b1957;
  font-weight: 600;
  font-size: 15px;
}
.users-table th {
  background-color: #d2b3db;
  color: #ffffff;
}
.users-table tbody tr:nth-child(even) {
  background-color: #e9f3ff;
}
.users-table tbody tr:hover {
  background-color: #d2b3db;
  color: #f7f4ed;
  transition: background-color 0.3s ease;
}
.actions {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}
.edit-btn {
  background-color: #ffc046;
  color: #0b1957;
  border: none;
  padding: 6px 14px;
  border-radius: 8px;
  margin-right: 6px;
  cursor: pointer;
  font-weight: 700;
  box-shadow: 0 2px 10px rgba(255, 192, 70, 0.6);
  transition: background-color 0.3s ease;
}
.edit-btn:hover {
  background-color: #A40033;
  color: #f7f4ed;
}

.delete-btn {
  background-color: #f99866;
  color: #f7f4ed;
  border: none;
  padding: 6px 14px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 700;
  box-shadow: 0 2px 10px rgba(249, 152, 102, 0.6);
  transition: background-color 0.3s ease;
}
.delete-btn:hover {
  background-color: #A40033;
  color: #f7f4ed;
}
</style>
