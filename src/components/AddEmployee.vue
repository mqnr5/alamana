<script>
export default {
    name: 'AddEployee',
    data() {
        return {
            empName: '',
            empEmail: '',
            empRole: '',
        }
    },
}
</script>
<template>
    <div class="view">
        <h2>إضافة موظف جديد</h2>
        <form @submit.prevent="addEmployee">
            <label for="name">الاسم:</label>
            <input type="text" id="name" v-model="empName" required>

            <label for="email">البريد الإلكتروني:</label>
            <input type="email" id="email" v-model="empEmail" required>

            <label for="role">الدور:</label>
            <select id="role" v-model="empRole" required>
                <option value="">اختر الدور</option>
                <option value="مدير">مدير</option>
                <option value="موظف">موظف</option>
                <option value="محاسب">محاسب</option>
            </select>

            <button type="submit">إضافة موظف</button>
        </form>
    </div>
</template>
<style scoped>
.view {
    width: 60%;
    height: 100px;
    display: flex;
    flex-direction: column;
    border: 2px solid pink;
    border-radius: 20px;
}
</style>