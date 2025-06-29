<template>
  <div class="users-container">
    <h2>إدارة المستخدمين</h2>

    <button @click="addUserVisible = true" class="add-user-button">➕ إضافة مستخدم</button>
    <div class="add-user-form" :visible="addUserVisible">
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
          <td>
            <button @click="editEmpInfo(user)" class="edit-btn">تعديل</button>
            <button @click="deleteUser(user)" class="delete-btn">حذف</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import AddEmployee from '@/components/AddEmployee.vue';
import { employeeBus } from '@/bus';

export default {
  name: "ManageUsers",
  components: {
    AddEmployee
  },
  data() {
    return {
      addUserVisible: false,
      users: [
        { id: 1, name: "أحمد علي", email: "ahmed@example.com", role: "رئيس قسم" },
        { id: 2, name: "فاطمة حسن", email: "fatima@example.com", role: "موظف" },
        { id: 3, name: "كرار محمد", email: "karar@example.com", role: "رئيس إدارة" },
      ],
    };
  },
  methods: {
    deleteUser(user) {
      this.users = this.users.filter(u => u.id !== user.id);
    },
    editEmpInfo(user) {
      employeeBus.emit('old-employee-info', {
          EmpName: user.name,
          EmpEmail: user.email,
          EmpRole: user.role
       })
       this.$router.push({ name: 'EditEmpInfo' })
    }
  },
  mounted() {
    employeeBus.on('add-employee', (user) => {
      this.users.push({
        id: this.users.length + 1,
        name: user.name,
        email: user.email,
        role: user.role
      })
      this.addUserVisible = false
    })
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
  margin: auto;
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
