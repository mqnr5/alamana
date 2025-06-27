<script>
export default {
    name: 'HomePage',
    data() {
        return {
            title: 'نظام الأمانة العامة - العتبة العلوية المقدسة',
        }
    },
    methods: {
        goToSection(section) {
            this.$router.push(section)
        }
    },
}
</script>
<template>
    <div class="body">
        <div class="title">
            <h1>{{ title }}</h1>
        </div>
        <div class="all-sections">
            <button @click="goToSection('ChairManagement')" class="section-button">رئيس الإدارة</button>
            <button @click="goToSection('DepartmentHead')" class="section-button">رئيس القسم</button>
            <button @click="goToSection('Employee')" class="section-button">الموظف</button>
        </div>
    </div>
</template>
<style scoped>
.title {
    margin: 20px;
    font-weight: bold;
}
.body {
    background-color: #EFDFC5;
    justify-items: center;
}
</style>