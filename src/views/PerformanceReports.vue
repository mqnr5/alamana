<template>
  <div class="performance-container">
    <h2>تقارير الأداء</h2>
    <p>فيما يلي تقارير الأداء الخاصة بكل قسم وموظف ضمن النظام.</p>

    <div class="filters">
      <label>اختر القسم:</label>
      <select v-model="selectedDepartment">
        <option disabled value="">-- اختر قسم --</option>
        <option v-for="dep in departments" :key="dep">{{ dep }}</option>
      </select>
    </div>

    <div class="report-table" v-if="filteredReports.length > 0">
      <table>
        <thead>
          <tr>
            <th>اسم الموظف</th>
            <th>عدد المهام</th>
            <th>المهام المكتملة</th>
            <th>نسبة الإنجاز</th>
            <th>التقييم</th>
            <th>الحالة</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="report in filteredReports" :key="report.name">
            <td>{{ report.name }}</td>
            <td>{{ report.total }}</td>
            <td>{{ report.completed }}</td>
            <td>{{ calcProgress(report) }}%</td>
            <td>{{ getRating(report) }}/5</td>
            <td>
              <span :class="['status', getStatus(report)]">
                {{ getStatusLabel(report) }}
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div v-else class="no-data">لا توجد تقارير متاحة لهذا القسم.</div>

    <button class="back-main" @click="$router.push({ name: 'SuperAdmin' })">
      العودة إلى لوحة السوبر أدمن
    </button>
  </div>
</template>

<script>
export default {
  name: "PerformanceReports",
  data() {
    return {
      selectedDepartment: "",
      departments: ["قسم الموارد البشرية", "قسم المشاريع", "قسم الدعم الفني"],
      reports: [
        { department: "قسم الموارد البشرية", name: "أحمد", total: 10, completed: 8 },
        { department: "قسم المشاريع", name: "سارة", total: 12, completed: 10 },
        { department: "قسم الدعم الفني", name: "خالد", total: 9, completed: 6 },
      ],
    };
  },
  computed: {
    filteredReports() {
      return this.reports.filter(r => r.department === this.selectedDepartment);
    },
  },
  methods: {
    calcProgress(report) {
      return ((report.completed / report.total) * 100).toFixed(1);
    },
    getRating(report) {
      const progress = this.calcProgress(report);
      if (progress >= 90) return 5;
      if (progress >= 75) return 4;
      if (progress >= 60) return 3;
      if (progress >= 40) return 2;
      return 1;
    },
    getStatus(report) {
      const progress = this.calcProgress(report);
      if (progress >= 85) return 'excellent';
      if (progress >= 60) return 'good';
      return 'weak';
    },
    getStatusLabel(report) {
      const status = this.getStatus(report);
      return status === 'excellent' ? 'ممتاز' : status === 'good' ? 'جيد' : 'ضعيف';
    }
  },
};
</script>

<style scoped>
.performance-container {
  background-color: #ffffff;
  color: #6d7cd9;
  padding: 30px;
  max-width: 950px;
  margin: auto;
  border-radius: 15px;
  direction: rtl;
  text-align: right;
}
h2 {
  color: #b1dfe4;
}
.filters {
  margin: 20px 0;
}
select {
  padding: 10px;
  border-radius: 8px;
  border: 2px solid #f99866;
  background-color: #fff8f5;
  color: #6d7cd9;
}
.report-table table {
  width: 100%;
  margin-top: 20px;
  border-collapse: collapse;
  background-color: #dec7e0;
}
.report-table th,
.report-table td {
  padding: 12px;
  border: 1px solid #fff;
  text-align: center;
}
.no-data {
  margin-top: 20px;
  color: #f99866;
  font-weight: bold;
}
.status {
  font-weight: bold;
  padding: 6px 12px;
  border-radius: 8px;
  color: white;
}
.status.excellent {
  background-color: #6d7cd9;
}
.status.good {
  background-color: #ffc046;
}
.status.weak {
  background-color: #f99866;
}
.back-main {
  margin-top: 30px;
  background-color: #ffc046;
  color: white;
  padding: 10px 25px;
  border-radius: 10px;
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>
