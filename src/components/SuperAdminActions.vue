<script>
export default {
    name: 'SuperAdminActions',
    methods: {
        goTo(viewName) {
            this.$router.push({ name: viewName });
        }
    }
}
</script>
<template>
    <div class="actions">
      <button @click="goTo('ManageUsers')">إدارة المستخدمين</button>
      <button @click="goTo('SystemSettings')">إعدادات النظام</button>
      <button @click="goTo('PerformanceReports')">تقارير الأداء</button>
      <button @click="goTo('MajorRequests')">الطلبات الكبرى</button>
      <button @click="goTo('DepartmentOverview')">إشراف الأقسام</button>
      <button @click="goTo('ReportViewer')">مراجعة التقارير السابقة</button>
    </div>
</template>
<style scoped>
.actions {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-top: 30px;
  max-width: 350px;
  margin-left: auto;
  margin-right: auto;
}

.actions button {
  background-color: #f7f4ed;
  color: #0b1957;
  border: 2px solid #A40033;
  padding: 14px 22px;
  border-radius: 12px;
  cursor: pointer;
  font-weight: 700;
  font-size: 16px;
  transition: all 0.3s ease;
  box-shadow: 0 2px 6px rgba(164, 0, 51, 0.25);
}

.actions button:hover {
  background-color: #A40033;
  color: white;
  box-shadow: 0 5px 16px rgba(164, 0, 51, 0.6);
  transform: translateY(-3px);
}
</style>