<script>
export default {
  name: 'DepartmentHeadView',
  methods: {
    goTo(route) {
      this.$router.push(route);
    }
  }
}
</script>

<template>
  <div class="dashboard">
    <h1>📋 لوحة تحكم رئيس القسم</h1>
    <p class="subtitle">أهلاً بك، يمكنك إدارة القسم من خلال الواجهات التالية:</p>

    <div class="cards">
      <div class="card" @click="goTo('/review-reports')">
        📑 مراجعة التقارير
        <span>عرض تقارير الأقسام والرد عليها</span>
      </div>
      <div class="card" @click="goTo('/manage-staff')">
        👥 إدارة الموظفين
        <span>متابعة الحضور والتقييمات والملاحظات</span>
      </div>
      <div class="card" @click="goTo('/urgent-tasks')">
        ⚠️ تنبيهات عاجلة
        <span>مهام وتنبيهات يجب التعامل معها فوراً</span>
      </div>
    </div>

    <button class="back-btn" @click="$router.go(-1)">🔙 رجوع</button>
  </div>
</template>

<style scoped>
.dashboard {
  padding: 40px;
  background: #f9f9f9;
  border-radius: 25px;
  box-shadow: 0 12px 20px rgba(0,0,0,0.08);
  font-family: 'Tajawal', sans-serif;
  text-align: center;
  direction: rtl;
  max-width: 1000px;
  margin: auto;
}

h1 {
  color: #0b1957;
  font-size: 32px;
  margin-bottom: 10px;
}

.subtitle {
  font-size: 18px;
  color: #555;
  margin-bottom: 30px;
}

.cards {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
}

.card {
  background: white;
  color: #0b1957;
  padding: 20px;
  border-radius: 18px;
  width: 280px;
  box-shadow: 0 6px 12px rgba(0,0,0,0.05);
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 22px;
  font-weight: bold;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.card span {
  font-size: 15px;
  font-weight: normal;
  color: #666;
}

.card:hover {
  background: #edf0ff;
  transform: translateY(-5px);
}

.back-btn {
  margin-top: 30px;
  padding: 12px 24px;
  background: #a40033;
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 16px;
  cursor: pointer;
}
.back-btn:hover {
  background: #6c0024;
}
</style>
