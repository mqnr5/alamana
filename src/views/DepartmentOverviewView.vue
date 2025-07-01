<template>
  <div class="supervision-dashboard">
    <header class="dashboard-header">
      <h1>🧭 واجهة إشراف الأقسام</h1>
      <p>نظرة شاملة وتحكم مركزي بأداء الأقسام</p>
    </header>

    <section class="overview-cards">
      <div class="card" v-for="card in cards" :key="card.title">
        <div class="icon">{{ card.icon }}</div>
        <div class="details">
          <h3>{{ card.title }}</h3>
          <p>{{ card.value }}</p>
        </div>
      </div>
    </section>

    <section class="charts-section">
      <h2>📊 إحصائيات الأداء العام</h2>
      <Bar :data="barChartData" :options="barChartOptions" />
    </section>

    <section class="departments-table">
      <h2>📁 بيانات الأقسام</h2>
      <table>
        <thead>
          <tr>
            <th>اسم القسم</th>
            <th>عدد الموظفين</th>
            <th>نسبة الإنجاز</th>
            <th>ملاحظات</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="dept in departments" :key="dept.name">
            <td>{{ dept.name }}</td>
            <td>{{ dept.employees }}</td>
            <td>{{ dept.performance }}%</td>
            <td>{{ dept.notes }}</td>
          </tr>
        </tbody>
      </table>
    </section>
    <ExportData />
  </div>
</template>

<script>
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js'
import ExportData from '@/components/ExportData.vue'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'DepartmentOverviewView',
  components: {
    Bar,
    ExportData
  },
  data() {
    return {
      cards: [
        { title: 'عدد الأقسام', value: 8, icon: '🏢' },
        { title: 'عدد الموظفين', value: 124, icon: '👥' },
        { title: 'متوسط الإنجاز', value: '78%', icon: '📈' },
        { title: 'مهام حرجة', value: 12, icon: '⚠️' }
      ],
      departments: [
        { name: 'الصيانة', employees: 15, performance: 80, notes: 'بحاجة لموظف إضافي' },
        { name: 'الدعم الفني', employees: 20, performance: 90, notes: 'أداء متميز' },
        { name: 'الأمانة', employees: 18, performance: 75, notes: 'توصيات بزيادة التنسيق' }
      ],
      barChartData: {
        labels: ['الصيانة', 'الدعم الفني', 'الأمانة'],
        datasets: [
          {
            label: 'نسبة الإنجاز',
            backgroundColor: ['#A40033', '#4E5174', '#6db5ff'],
            data: [80, 90, 75]
          }
        ]
      },
      barChartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            labels: {
              font: {
                family: 'Tajawal'
              }
            }
          }
        }
      }
    }
  }
}
</script>

<style scoped>
.supervision-dashboard {
  font-family: 'Tajawal', sans-serif;
  padding: 30px;
  background: #fefefe;
  direction: rtl;
  color: #1a1a1a;
  max-width: 1200px;
  margin: auto;
}
.dashboard-header {
  text-align: center;
  margin-bottom: 30px;
}
.dashboard-header h1 {
  font-size: 30px;
  color: #A40033;
}
.overview-cards {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
  justify-content: space-around;
  margin-bottom: 40px;
}
.card {
  flex: 1 1 200px;
  background-color: #f3f6fb;
  padding: 20px;
  border-radius: 15px;
  box-shadow: 0 0 8px rgba(0,0,0,0.05);
  text-align: center;
}
.card .icon {
  font-size: 32px;
  margin-bottom: 10px;
}
.charts-section {
  margin-bottom: 40px;
  height: 300px;
}
.charts-section h2 {
  margin-bottom: 15px;
}
.departments-table table {
  width: 100%;
  border-collapse: collapse;
  background-color: #fff;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 0 10px rgba(0,0,0,0.07);
}
.departments-table th,
.departments-table td {
  padding: 12px;
  text-align: center;
  border-bottom: 1px solid #ddd;
}
.departments-table thead {
  background-color: #f0f0f0;
}
</style>
