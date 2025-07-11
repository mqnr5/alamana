<template>
  <div class="dashboard-container">
    <h2 class="title">لوحة تحكم السوبر أدمـن</h2>

    <div class="cards-grid">
      <div v-for="card in cards" :key="card.title" class="card">
        <h3>{{ card.title }}</h3>
        <p>{{ card.value }}</p>
      </div>
    </div>
    <button class="back-btn" @click="$router.go(-1)">↩️ رجوع</button>

  </div>
</template>

<script>
import {
  get_users,
  get_departments,
  get_hurryup_alerts,
  get_missions,
  get_review_requests,
  get_reports
} from '@/api/public_operations'

export default {
  name: 'SuperDashboard',
  data() {
    return {
      cards: []
    };
  },
  async mounted() {
    try {
      const users = await get_users();
      const departments = await get_departments();
      const alerts = await get_hurryup_alerts();
      const reviewRequests = await get_review_requests();
      const performance_reports = await get_reports();
      const missions = await get_missions(3); // user_id مؤقت

      this.cards = [
        { title: 'عدد الإدارات', value: departments.length },
        { title: 'عدد الموظفين', value: users.length },
        { title: 'عدد التنبيهات العاجلة', value: alerts.length },
        { title: 'عدد الطلبات الكبرى', value: reviewRequests.length },
        { title: 'عدد المهمات', value: missions.length },
        { title: 'عدد تقارير الأداء', value: performance_reports.length },
      ];
    } catch (err) {
      console.error('فشل تحميل البيانات:', err);
    }
  }
};
</script>

<style scoped>
.dashboard-container {
  max-width: 1000px;
  margin: auto;
  padding: 40px;
  text-align: center;
  background-color: #f5f6fc;
  border-radius: 18px;
  box-shadow: 0 0 12px rgba(130, 120, 180, 0.2);
  direction: rtl;
}

.title {
  color: #1c1c3c;
  font-weight: 800;
  font-size: 28px;
  margin-bottom: 30px;
}

.cards-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
}

.card {
  background-color: #fff;
  border: 2px solid #d2b3db;
  border-radius: 12px;
  padding: 25px;
  width: 220px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
  transition: 0.3s ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 20px rgba(210, 179, 219, 0.4);
}

.card h3 {
  font-size: 20px;
  color: #4e5174;
  margin-bottom: 10px;
}

.card p {
  font-size: 24px;
  font-weight: bold;
  color: #0b1957;
}

button {
  background-color: #3b3b99;
  color: white;
  padding: 8px 18px;
  border: none;
  margin: 30px;
  border-radius: 10px;
  font-size: 20px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}
button:hover {
  background-color: #25257c;
}

.back-btn {
  background-color: #a40033;
}
.back-btn:hover {
  background-color: #7b0028;
}
</style>
