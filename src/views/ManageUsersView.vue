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
            <button class="edit-btn">تعديل</button>
            <button class="delete-btn">حذف</button>
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
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.08);
  color: #6d7cd9;
}

h2 {
  color: #b1dfe4;
  text-align: center;
  margin-bottom: 20px;
}

.add-user-button {
  background-color: #fac5d4;
  border: none;
  padding: 10px 18px;
  color: #6d7cd9;
  font-weight: bold;
  border-radius: 8px;
  margin-bottom: 20px;
  cursor: pointer;
}

.add-user-button:hover {
  background-color: #f99866;
  color: white;
}

.users-table {
  width: 100%;
  border-collapse: collapse;
  background-color: #dec7e0;
}

.users-table th,
.users-table td {
  padding: 12px;
  text-align: center;
  border: 1px solid #ffffff;
}

.users-table th {
  background-color: #b1dfe4;
  color: white;
}

.edit-btn {
  background-color: #ffc046;
  color: white;
  border: none;
  padding: 5px 12px;
  border-radius: 6px;
  margin-right: 5px;
  cursor: pointer;
}

.delete-btn {
  background-color: #f99866;
  color: white;
  border: none;
  padding: 5px 12px;
  border-radius: 6px;
  cursor: pointer;
}

.edit-btn:hover,
.delete-btn:hover {
  opacity: 0.9;
}
</style>
