<template>
  <div class="section">
    <h2>⚠️ تنبيهات عاجلة</h2>
    <p>المهام التي تحتاج تدخل فوري.</p>

    <ul class="alerts" v-if="urgentAlerts.length">
      <li v-for="alert in urgentAlerts" :key="alert.id" class="alert-item">
        <strong>{{ alert.title }}</strong>
        <p>{{ alert.description }}</p>
        <button @click="resolve(alert)">تم الحل</button>
      </li>
    </ul>
    <p v-else class="no-alerts">لا توجد تنبيهات عاجلة حالياً.</p>

    <button class="back-btn" @click="goBack">رجوع</button>
  </div>
</template>

<script>
export default {
  name: 'UrgentTasksView',
  data() {
    return {
      urgentAlerts: [
        { id: 1, title: 'انقطاع في الخادم', description: 'الخادم الرئيسي لا يستجيب' },
        { id: 2, title: 'تأخير في تسليم التقارير', description: 'تقرير قسم المحاسبة لم يتم تسليمه' }
      ]
    }
  },
  methods: {
    resolve(alert) {
      alert(`تم حل: ${alert.title}`);
      this.urgentAlerts = this.urgentAlerts.filter(a => a.id !== alert.id);
    },
    goBack() {
      if (window.history.length > 1) {
        this.$router.go(-1);
      } else {
        this.$router.push('/');
      }
    }
  }
}
</script>

<style scoped>
.section {
  max-width: 1200px;
  margin: 50px auto;
  padding: 50px 60px;
  background-color: #fff0f0;
  border-radius: 25px;
  box-shadow: 0 12px 25px rgba(164, 0, 51, 0.3);
  font-family: 'Tajawal', sans-serif;
  color: #44000a;
  text-align: right;
  direction: rtl;
  border: 3px solid #a40033;
  transition: transform 0.3s ease;
}

.section:hover {
  transform: scale(1.03);
}

h2 {
  font-size: 48px;
  font-weight: 900;
  margin-bottom: 25px;
  color: #a40033;
  text-shadow: 2px 2px 6px #6c0024;
}

p {
  font-size: 24px;
  margin-bottom: 35px;
  font-weight: 600;
}

.alerts {
  list-style: none;
  padding: 0;
}

.alert-item {
  background: #ffe6e6;
  border: 3px solid #ff4d4d;
  padding: 30px 40px;
  border-radius: 25px;
  margin-bottom: 30px;
  box-shadow: inset 0 0 15px rgba(255, 77, 77, 0.3);
  transition: background-color 0.3s ease;
  cursor: pointer;
}

.alert-item:hover {
  background-color: #ffd6d6;
}

.alert-item strong {
  display: block;
  font-size: 32px;
  font-weight: 900;
  margin-bottom: 15px;
  color: #a40033;
  text-shadow: 1px 1px 3px #6c0024;
}

.alert-item p {
  font-size: 22px;
  margin: 0 0 25px 0;
  color: #8b0000;
  font-weight: 700;
  line-height: 1.4;
}

button {
  background: #a40033;
  color: white;
  padding: 18px 40px;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  font-weight: 900;
  font-size: 24px;
  transition: background-color 0.4s ease, box-shadow 0.3s ease;
  box-shadow: 0 6px 15px rgba(164, 0, 51, 0.6);
  user-select: none;
}

button:hover {
  background: #6c0024;
  box-shadow: 0 8px 20px rgba(108, 0, 36, 0.8);
}

.back-btn {
  margin-top: 50px;
  width: 100%;
  font-size: 28px;
  font-weight: 900;
  letter-spacing: 1.5px;
  background-color: #44000a;
  box-shadow: 0 8px 20px rgba(68, 0, 10, 0.8);
  border: 3px solid #a40033;
  transition: all 0.3s ease;
}

.back-btn:hover {
  background-color: #a40033;
  color: white;
  border-color: #6c0024;
  box-shadow: 0 10px 30px rgba(164, 0, 51, 1);
}

.no-alerts {
  font-size: 28px;
  font-weight: 700;
  color: #66001a;
  margin: 40px 0;
  text-shadow: 1px 1px 5px #a40033;
}
</style>
