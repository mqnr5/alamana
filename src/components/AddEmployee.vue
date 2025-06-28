<script>
import { employeeBus } from '@/bus.js';
export default {
    name: 'AddEmployee',
    data() {
        return {
            empName: '',
            empEmail: '',
            empRole: '',
        }
    },
    methods: {
        addEmp() {
            employeeBus.emit('add-employee', {
                name: this.empName,
                email: this.empEmail,
                role: this.empRole
            });
        }
    }
}
</script>
<template>
    <div class="view">
        <h2>إضافة موظف جديد</h2>
        <form @submit.prevent="addEmployee" ckass="form">
            <label for="name">الاسم:</label>
            <input type="text" id="name" v-model="empName" required>
            <br>
            <label for="email">البريد الإلكتروني:</label>
            <input type="email" id="email" v-model="empEmail" required>
            <br>
            <label for="role">الدور:</label>
            <select id="role" v-model="empRole" required>
                <option value="">اختر الدور</option>
                <option value="مدير">مدير</option>
                <option value="موظف">موظف</option>
                <option value="محاسب">محاسب</option>
            </select>
            <br>
            <button @click="addEmp">إضافة موظف</button>
        </form>
    </div>
</template>
<style scoped>
.view {
    width: 60%;
    height: 150px;
    display: flex;
    direction: rtl;
    margin: 20px;
    flex-direction: column;
    justify-self: center;
    align-items: center;
    border: 2px solid pink;
    border-radius: 20px;
}
</style>