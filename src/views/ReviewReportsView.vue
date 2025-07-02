<template>
  <div class="review-view">
    <h1>📑 مراجعة التقارير</h1>
    <p class="desc">يمكنك هنا مراجعة تقارير الأقسام والتحقق من محتواها بدقة.</p>

    <transition-group name="fade-slide" tag="ul" class="report-list">
      <li v-for="report in reports" :key="report.id" class="report-item">
        <div class="report-info">
          <strong>{{ report.title }}</strong>
          <span>{{ report.date }}</span>
        </div>
        <button @click="review(report)">👁️ عرض</button>
      </li>
    </transition-group>

    <button class="back-btn" @click="$router.go(-1)">↩️ رجوع</button>
  </div>
</template>

<script>
export default {
  name: 'ReviewReportsView',
  data() {
    return {
      reports: [
        { id: 1, title: 'تقرير قسم البرمجة', date: '2025-07-01' },
        { id: 2, title: 'تقرير قسم التصميم', date: '2025-06-30' },
        { id: 3, title: 'تقرير قسم الدعم الفني', date: '2025-06-29' }
      ]
    };
  },
  methods: {
    review(report) {
      this.$router.push({ name: 'ReportViewer', query: { reportId: report.id } });
    }
  }
};
</script>

<style scoped>
.review-view {
  padding: 40px 25px;
  max-width: 1000px;
  margin: auto;
  background-color: #fdfdfd;
  border-radius: 16px;
  box-shadow: 0 8px 18px rgba(0, 0, 0, 0.07);
  font-family: 'Tajawal', sans-serif;
  text-align: center;
  direction: rtl;
}

h1 {
  font-size: 30px;
  color: #2d2d6e;
  margin-bottom: 10px;
}

.desc {
  font-size: 16px;
  color: #666;
  margin-bottom: 25px;
}

.report-list {
  list-style: none;
  padding: 0;
}

.report-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #f5f6fa;
  padding: 15px 20px;
  border-radius: 12px;
  margin-bottom: 12px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.03);
}

.report-info {
  text-align: right;
}
.report-info strong {
  display: block;
  font-size: 18px;
  color: #333;
}
.report-info span {
  font-size: 14px;
  color: #777;
}

button {
  background-color: #3b3b99;
  color: white;
  border: none;
  padding: 8px 18px;
  border-radius: 10px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}
button:hover {
  background-color: #25257c;
}

.back-btn {
  margin-top: 30px;
  background-color: #a40033;
}
.back-btn:hover {
  background-color: #7b0028;
}

.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.4s ease;
}
.fade-slide-enter-from,
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(15px);
}
</style>
