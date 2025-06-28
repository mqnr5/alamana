<template>
  <div class="chair-container">
    <h2>رئيس الإدارة</h2>
    <p>تشرف على الأقسام وتتابع تقارير الأداء وتدير الطلبات المهمة.</p>

    <div class="filters">
      <label>تصفية حسب القسم:</label>
      <select v-model="selectedDepartment">
        <option value="">كل الأقسام</option>
        <option v-for="dep in departments" :key="dep">{{ dep }}</option>
      </select>
    </div>

    <div class="stats">
      <div class="stat-box" v-for="stat in filteredStats" :key="stat.title">
        <span class="stat-title">{{ stat.title }}</span>
        <span class="stat-value">{{ stat.value }}</span>
      </div>
    </div>

    <div class="requests">
      <h3>طلبات تنتظر مراجعتك</h3>
      <div v-if="pendingRequests.length > 0">
        <ul>
          <li v-for="req in pendingRequests" :key="req.id">
            <strong>{{ req.title }}</strong> من {{ req.sender }} - 
            <button @click="approve(req.id)">قبول</button>
            <button @click="reject(req.id)">رفض</button>
          </li>
        </ul>
      </div>
      <div v-else>
        <p>لا توجد طلبات معلقة حالياً.</p>
      </div>
    </div>

    <div class="actions">
      <button @click="goTo('PerformanceReports')">عرض تقارير الأداء</button>
      <button @click="goTo('DepartmentOverview')">إدارة الأقسام</button>
      <button @click="goTo('MajorRequests')">عرض الطلبات الكبرى</button>
      <button @click="goTo('Home')">رجوع للقائمة الرئيسية</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "ChairManagementView",
  data() {
    return {
      selectedDepartment: "",
      departments: ["الموارد البشرية", "المشاريع", "الدعم الفني"],
      stats: [
        { title: "عدد الموظفين", value: 20, department: "الموارد البشرية" },
        { title: "عدد المهام", value: 50, department: "المشاريع" },
        { title: "نسبة الإنجاز", value: "80%", department: "الدعم الفني" },
        { title: "تقارير واردة", value: 10, department: "الموارد البشرية" }
      ],
      pendingRequests: [
        { id: 1, title: "طلب إجازة", sender: "أحمد" },
        { id: 2, title: "مراجعة تقرير", sender: "سارة" }
      ]
    };
  },
  computed: {
    filteredStats() {
      if (!this.selectedDepartment) return this.stats;
      return this.stats.filter(stat => stat.department === this.selectedDepartment);
    }
  },
  methods: {
    goTo(view) {
      this.$router.push({ name: view });
    },
    approve(id) {
      this.pendingRequests = this.pendingRequests.filter(r => r.id !== id);
      alert("تمت الموافقة على الطلب رقم " + id);
    },
    reject(id) {
      this.pendingRequests = this.pendingRequests.filter(r => r.id !== id);
      alert("تم رفض الطلب رقم " + id);
    }
  }
};
</script><style scoped>
.chair-container {
  background-color: #ffffff;
  color: #0b1957;
  padding: 40px 25px;
  max-width: 1000px;
  margin: auto;
  border-radius: 15px;
  direction: rtl;
  text-align: right;
}

h2 {
  color: #0b1957;
  font-size: 28px;
  margin-bottom: 20px;
}

.filters {
  margin-bottom: 20px;
}

select {
  padding: 10px;
  border-radius: 8px;
  border: 2px solid #A40033;
  background-color: #e9f3ff;
  color: #0b1957;
  font-weight: bold;
}

.stats {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  margin-bottom: 30px;
}

.stat-box {
  background-color: #f7f4ed;
  border: 2px solid #d2b3db;
  padding: 20px;
  border-radius: 10px;
  flex: 1 1 40%;
  text-align: center;
}

.stat-title {
  font-size: 16px;
  font-weight: 600;
}

.stat-value {
  font-size: 22px;
  font-weight: bold;
  color: #A40033;
}

.requests {
  margin-bottom: 30px;
}

.requests ul {
  list-style: none;
  padding: 0;
}

.requests li {
  background: #e9f3ff;
  border: 1px solid #d2b3db;
  padding: 12px;
  border-radius: 10px;
  margin-bottom: 10px;
}

.requests button {
  margin-right: 10px;
  background-color: #d2b3db;
  border: none;
  padding: 6px 14px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: bold;
  color: #0b1957;
}

.requests button:hover {
  background-color: #A40033;
  color: white;
}

.actions {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.actions button {
  background-color: #A40033;
  color: white;
  padding: 12px 22px;
  border-radius: 10px;
  font-weight: bold;
  border: none;
  cursor: pointer;
  transition: 0.3s;
}

.actions button:hover {
  background-color: #d2b3db;
  color: #0b1957;
}
</style>
