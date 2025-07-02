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
      <ExportData :exportData="filteredReports" />
    </div>

    <div v-else class="no-data">لا توجد تقارير متاحة لهذا القسم.</div>

    <button class="back-main" @click="$router.go(-1)">
      العودة إلى الصفحة السابقة
    </button>
  </div>
</template>

<script>
import ExportData from '@/components/ExportData.vue';

export default {
  name: "PerformanceReports",
  components: {
    ExportData
  },
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
    },
  },
};
</script>
<style scoped>
.performance-container {
  background-color: #ffffff;
  color: #0b1957;
  padding: 30px;
  max-width: 950px;
  margin: auto;
  border-radius: 15px;
  direction: rtl;
  text-align: right;
  box-shadow: 0 0 15px rgba(210, 179, 219, 0.4);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
h2 {
  color: #0b1957;
  font-weight: 700;
  font-size: 28px;
  margin-bottom: 15px;
  text-align: center;
}
.filters {
  margin: 25px 0;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  gap: 10px;
  font-weight: 600;
  color: #0b1957;
  font-size: 16px;
}
select {
  padding: 10px 14px;
  border-radius: 8px;
  border: 2px solid #A40033;
  background-color: #e9f3ff;
  color: #0b1957;
  font-weight: 600;
  cursor: pointer;
  min-width: 180px;
  transition: border-color 0.3s ease;
}
select:hover, select:focus {
  border-color: #4E5174;
  outline: none;
}

.report-table table {
  width: 100%;
  margin-top: 20px;
  border-collapse: collapse;
  background-color: #f7f4ed;
  box-shadow: 0 4px 10px rgba(210, 179, 219, 0.3);
  border-radius: 12px;
  overflow: hidden;
}
.report-table th,
.report-table td {
  padding: 14px 18px;
  border: 1px solid #e9f3ff;
  text-align: center;
  color: #0b1957;
  font-weight: 600;
  font-size: 15px;
}
.report-table th {
  background-color: #d2b3db;
  color: #ffffff;
}
.report-table tbody tr:nth-child(even) {
  background-color: #e9f3ff;
}
.report-table tbody tr:hover {
  background-color: #d2b3db;
  color: white;
  transition: background-color 0.3s ease;
}
.no-data {
  margin-top: 20px;
  color: #A40033;
  font-weight: 700;
  font-size: 18px;
  text-align: center;
}

.status {
  font-weight: 700;
  padding: 8px 14px;
  border-radius: 12px;
  color: white;
  display: inline-block;
  min-width: 90px;
}
.status.excellent {
  background-color: #0b1957;
}
.status.good {
  background-color: #ffc046;
  color: #0b1957;
}
.status.weak {
  background-color: #A40033;
}
.back-main,
.export {
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
  box-shadow: 0 5px 18px rgba(164, 0, 51, 0.6);
  cursor: pointer;
  transition: background-color 0.3s ease;
}
.back-main:hover,
.export:hover {
  background-color: #4E5174;
  box-shadow: 0 6px 20px rgba(78, 81, 116, 0.8);
}
</style>
