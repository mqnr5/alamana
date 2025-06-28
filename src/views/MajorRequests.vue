<template>
  <div class="major-requests">
    <h2>الطلبات الكبرى</h2>
    <p>فيما يلي تفاصيل الطلبات المُقدمة من رؤساء الأقسام، والتي تتطلب موافقة الإدارة العليا.</p>

    <div class="filters">
      <label>ترتيب حسب:</label>
      <select v-model="sortBy">
        <option value="default">الافتراضي</option>
        <option value="pending">قيد المراجعة</option>
        <option value="accepted">المقبولة</option>
        <option value="rejected">المرفوضة</option>
      </select>
    </div>

    <div class="request-table" v-if="filteredRequests.length > 0">
      <table>
        <thead>
          <tr>
            <th>القسم</th>
            <th>نوع الطلب</th>
            <th>الوصف</th>
            <th>الحالة</th>
            <th>إجراء</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(req, index) in filteredRequests" :key="index">
            <td>{{ req.department }}</td>
            <td>{{ req.type }}</td>
            <td>{{ req.description }}</td>
            <td>
              <span :class="'status ' + req.status">{{ req.status }}</span>
            </td>
            <td>
              <button @click="updateStatus(index, 'مقبول')" :disabled="req.status !== 'قيد المراجعة'">✔ قبول</button>
              <button @click="updateStatus(index, 'مرفوض')" :disabled="req.status !== 'قيد المراجعة'">✖ رفض</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div v-else class="no-data">لا توجد طلبات متاحة حالياً حسب التصفية المختارة.</div>

    <button class="back-main" @click="$router.push({ name: 'SuperAdmin' })">
      العودة إلى لوحة السوبر أدمن
    </button>
  </div>
</template>

<script>
export default {
  name: "MajorRequests",
  data() {
    return {
      sortBy: "default",
      requests: [
        {
          department: "قسم المشاريع",
          type: "طلب ميزانية إضافية",
          description: "مشروع تطوير نظام داخلي يتطلب تمويلاً إضافياً.",
          status: "قيد المراجعة",
        },
        {
          department: "قسم الموارد البشرية",
          type: "طلب توظيف",
          description: "نحتاج إلى توظيف موظف جديد في قسم التدريب.",
          status: "قيد المراجعة",
        },
        {
          department: "قسم الدعم الفني",
          type: "شراء معدات",
          description: "شراء أجهزة حاسوب جديدة للقسم.",
          status: "مقبول",
        },
      ],
    };
  },
  computed: {
    filteredRequests() {
      if (this.sortBy === "default") return this.requests;
      if (this.sortBy === "pending") return this.requests.filter(r => r.status === "قيد المراجعة");
      if (this.sortBy === "accepted") return this.requests.filter(r => r.status === "مقبول");
      if (this.sortBy === "rejected") return this.requests.filter(r => r.status === "مرفوض");
      return this.requests;
    },
  },
  methods: {
    updateStatus(index, newStatus) {
      this.requests[index].status = newStatus;
    },
  },
};
</script>

<style scoped>
.major-requests {
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
  margin-bottom: 10px;
}
.filters {
  margin: 20px 0;
  display: flex;
  align-items: center;
  gap: 15px;
}
select {
  padding: 10px;
  border-radius: 8px;
  border: 2px solid #f99866;
  background-color: #fff8f5;
  color: #6d7cd9;
}
.request-table table {
  width: 100%;
  margin-top: 20px;
  border-collapse: collapse;
  background-color: #f9f4ff;
  border-radius: 10px;
  overflow: hidden;
}
.request-table th,
.request-table td {
  padding: 14px;
  border: 1px solid #eee;
  text-align: center;
}
.status {
  font-weight: bold;
  padding: 6px 12px;
  border-radius: 10px;
}
.status.قيد\:المراجعة {
  background-color: #ffc046;
  color: white;
}
.status.مقبول {
  background-color: #4caf50;
  color: white;
}
.status.مرفوض {
  background-color: #f44336;
  color: white;
}
button {
  margin: 5px;
  padding: 8px 16px;
  border: none;
  border-radius: 8px;
  font-weight: bold;
  cursor: pointer;
  transition: 0.3s;
}
button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
button:not(:disabled):hover {
  background-color: #fac5d4;
  color: white;
}
.no-data {
  margin-top: 25px;
  font-weight: bold;
  color: #f99866;
}
.back-main {
  margin-top: 40px;
  background-color: #ffc046;
  color: white;
  padding: 12px 30px;
  border-radius: 12px;
  display: block;
  margin-right: auto;
  margin-left: auto;
}
</style>
