<template>
  <div class="section-box">
    <h2>رئيس الأمانة العامة</h2>
    <p>يتمتع رئيس الأمانة العامة بأعلى الصلاحيات داخل النظام، ويشرف على جميع الأقسام والإدارات والموظفين.</p>

    <h3>لوحة التحكم العامة</h3>
    <div class="stats-boxes">
      <div class="stat-card" v-for="stat in stats" :key="stat.title">
        <span class="stat-title">{{ stat.title }}</span>
        <span class="stat-value">{{ stat.value }}</span>
      </div>
    </div>

    <h3>التحكم والإدارة</h3>
    <div class="sub-actions">
      <button @click="goTo('ManageUsers')">إدارة المستخدمين</button>
      <button @click="goTo('SystemSettings')">إعدادات النظام</button>
      <button @click="goTo('PerformanceReports')">تقارير الأداء</button>
      <button @click="goTo('MajorRequests')">الطلبات الكبرى</button>
      <button @click="goTo('DepartmentOverview')">إشراف الأقسام</button>
    </div>

    <button @click="$emit('back')" class="back-main">العودة إلى القائمة الرئيسية</button>
  </div>
</template>

<script>
export default {
  name: "SuperAdmin",
  data() {
    return {
      stats: [
        { title: "عدد الإدارات", value: 4 },
        { title: "عدد الأقسام", value: 12 },
        { title: "عدد الموظفين", value: 85 },
        { title: "عدد الطلبات الكُبرى", value: 6 },
      ],
    };
  },
  methods: {
    goTo(viewName) {
      this.$router.push({ name: viewName });
    },
  },
};
</script>

<style scoped>
.section-box {
  background-color: #dec7e0;
  color: #6d7cd9;
  padding: 30px;
  border-radius: 15px;
  max-width: 900px;
  margin: auto;
}
h2 {
  color: #b1dfe4;
}
h3 {
  margin-top: 20px;
  color: #ffc046;
}
.stats-boxes {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  margin-top: 10px;
}
.stat-card {
  background-color: #ffc046;
  color: white;
  border-radius: 10px;
  padding: 20px;
  flex: 1 1 40%;
  text-align: center;
}
.stat-title {
  font-size: 16px;
}
.stat-value {
  font-size: 22px;
  font-weight: bold;
}
.sub-actions {
  display: flex;
  flex-direction: column;
  gap: 15px;
  margin-top: 20px;
}
.sub-actions button {
  background-color: #c1e0ba;
  color: #6d7cd9;
  border: 2px solid #f99866;
  padding: 12px;
  border-radius: 10px;
  cursor: pointer;
  font-weight: bold;
}
.sub-actions button:hover {
  background-color: #fac5d4;
  color: white;
}
.back-main {
  margin-top: 30px;
  background-color: #f99866;
  color: white;
  padding: 10px 25px;
  border-radius: 10px;
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>
