<script>
export default {
  name: "ExportData",
  props: {
    exportData: {
        type: Array,
        required: true
    }
  },
  data() {
    return {
        format: ''
    }
  },
  methods: {
    exportToCSV() {
      const csvContent = this.exportData.map(row => row.join(",")).join("\n");
      const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.setAttribute("href", url);
      link.setAttribute("download", "exported_data.csv");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    },
    exportToJSON() {
      const jsonContent = JSON.stringify(this.exportData, null, 2);
      const blob = new Blob([jsonContent], { type: 'application/json;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.setAttribute("href", url);
      link.setAttribute("download", "exported_data.json");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    },
    exportDataHandler() {
      if (this.format === 'csv') {
        this.exportToCSV();
      } else if (this.format === 'json') {
        this.exportToJSON();
      }
    }
  }
};
</script>
<template>
    <div class="export-field">
        <span>تصدير بصيغة : </span>
        <select v-model="format">
          <option value="csv">CSV</option>
          <option value="json">JSON</option>
        </select>
        <button @click="exportDataHandler">تصدير البيانات</button>
    </div>
</template>
<style scoped>
.export-field {
  background-color: #f7f4ed;
  color: #0b1957;
  border: 2px solid #A40033;
  padding: 14px 22px;
  border-radius: 12px;
  font-weight: 700;
  margin: 20px auto;
}
span {
    font-size: 28px;
}
select {
  padding: 10px;
  border-radius: 8px;
  border: 2px solid #A40033;
  background-color: #e9f3ff;
  color: #0b1957;
  font-weight: bold;
}
button {
    margin: 20px;
    cursor: pointer;
    height: 30px;
    font-size: 24px;
    border-radius: 10px;
    margin: 20px auto;
}
</style>