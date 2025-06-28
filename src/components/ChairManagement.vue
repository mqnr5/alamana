<script>
export default {
  name: "ChairManagement",
  data() {
    return {
      page: 1,
      stats: [
        { title: "عدد الأقسام", value: 5 },
        { title: "عدد الموظفين الكلي", value: 42 },
        { title: "مهام قيد التنفيذ", value: 18 },
        { title: "طلبات قيد الانتظار", value: 4 },
      ],
      departmentHeads: [
        { name: "زينب عبد الزهره", department: "المالية", employees: 7, lastReport: "2025/06/25" },
        { name: "علي رحيم", department: "الدعم الفني", employees: 9, lastReport: "2025/06/26" },
        { name: "هدى حسين", department: "التنمية البشرية", employees: 6, lastReport: "2025/06/24" },
      ],
    };
  },
};
</script>
<template>
  
</template>
<style scoped>
.section-box {
  background-color: #dec7e0;
  color: #6d7cd9;
  padding: 30px;
  border-radius: 15px;
  max-width: 900px;
  margin: auto;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
h2 {
  color: #b1dfe4;
  font-size: 26px;
  margin-bottom: 10px;
}
h3 {
  margin-top: 25px;
  color: #ffc046;
}
ul.task-list {
  list-style: none;
  padding: 0;
}
ul.task-list li {
  margin-bottom: 10px;
}
.stats-boxes {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  margin-top: 15px;
}
.stat-card {
  flex: 1 1 40%;
  background-color: #ffc046;
  color: white;
  border-radius: 12px;
  padding: 20px;
  text-align: center;
}
.stat-title {
  display: block;
  font-size: 16px;
  margin-bottom: 8px;
}
.stat-value {
  font-size: 22px;
  font-weight: bold;
}
.admin-table {
  width: 100%;
  margin-top: 20px;
  border-collapse: collapse;
  background-color: #ffffff;
}
.admin-table th,
.admin-table td {
  border: 1px solid #f99866;
  padding: 12px;
  text-align: center;
  color: #6d7cd9;
}
.nav-sub-buttons {
  display: flex;
  justify-content: space-between;
  margin: 25px 0;
}
button {
  background-color: #c1e0ba;
  color: #6d7cd9;
  border: 2px solid #f99866;
  padding: 10px 20px;
  border-radius: 10px;
  font-weight: bold;
  cursor: pointer;
  transition: 0.3s ease;
}
button:hover:not(:disabled) {
  background-color: #fac5d4;
  color: white;
}
button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
.admin-subpage {
  background-color: #ffffff;
  border: 1px solid #f99866;
  border-radius: 12px;
  padding: 20px;
  margin-top: 20px;
  color: #6d7cd9;
}
.back-main {
  display: block;
  margin: 30px auto 0;
}
</style>
