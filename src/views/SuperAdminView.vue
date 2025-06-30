<template>
  <div class="section-box">
    <h2>رئيس الأمانة العامة</h2>
    <p>يتمتع رئيس الأمانة العامة بأعلى الصلاحيات داخل النظام، ويشرف على جميع الأقسام والإدارات والموظفين.</p>

    <h3>لوحة التحكم العامة</h3>
    <div class="stats-boxes">
      <div class="stat-card" v-for="stat in stats" :key="stat.title">
        <span class="stat-title">{{ stat.title }} : </span>
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
      <button @click="goTo('ReportViewer')">مراجعة التقارير السابقة</button>
    </div>

    <button @click="goTo('Home')" class="back-main">العودة إلى القائمة الرئيسية</button>
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
  background-color: #d2b3db;
  color: #0b1957;
  padding: 30px;
  border-radius: 15px;
  max-width: 900px;
  margin: auto;
  box-shadow: 0 0 18px rgba(210, 179, 219, 0.5);
  direction: rtl;
  animation: fadeIn 0.8s ease;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

h2 {
  color: #0b1957;
  font-weight: 700;
  font-size: 30px;
  text-align: center;
  margin-bottom: 20px;
}

h3 {
  margin-top: 25px;
  color: #4E5174;
  font-weight: 600;
  font-size: 22px;
  text-align: right;
}

.stats-boxes {
  display: flex;
  flex-wrap: wrap;
  gap: 18px;
  margin-top: 15px;
  justify-content: center;
}

.stat-card {
  background-color: #e9f3ff;
  color: #0b1957;
  border-radius: 12px;
  padding: 22px;
  flex: 1 1 42%;
  text-align: center;
  box-shadow: 0 4px 12px rgba(0, 25, 87, 0.15);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.stat-card:hover {
  transform: scale(1.03);
  box-shadow: 0 6px 20px rgba(0, 25, 87, 0.25);
}

.stat-title {
  font-size: 17px;
  font-weight: 600;
}

.stat-value {
  font-size: 26px;
  font-weight: 900;
  margin-top: 6px;
}

.sub-actions {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-top: 30px;
  max-width: 350px;
  margin-left: auto;
  margin-right: auto;
}

.sub-actions button {
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

.sub-actions button:hover {
  background-color: #A40033;
  color: white;
  box-shadow: 0 5px 16px rgba(164, 0, 51, 0.6);
  transform: translateY(-3px);
}

.back-main {
  margin-top: 35px;
  background-color: #A40033;
  color: white;
  padding: 12px 30px;
  border-radius: 12px;
  display: block;
  margin-left: auto;
  margin-right: auto;
  font-weight: 700;
  font-size: 17px;
  box-shadow: 0 5px 18px rgba(164, 0, 51, 0.5);
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.back-main:hover {
  background-color: #4E5174;
  box-shadow: 0 6px 22px rgba(78, 81, 116, 0.6);
  transform: translateY(-2px);
}
</style>
