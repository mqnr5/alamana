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
      const csvContent = this.exportData.map(row => Array.isArray(row) ? row.join(",") : row).join("\n");
      const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.setAttribute("href", url);
      link.setAttribute("download", "exported_data.csv");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      URL.revokeObjectURL(url);
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
      <div class="format">
        <span>تصدير بصيغة : </span>
        <select v-model="format" required>
          <option value="csv" disabled>CSV</option>
          <option value="json">JSON</option>
        </select>
      </div>
      <div class="epxport-action">
          <button @click="exportDataHandler">تصدير البيانات</button>
      </div>
    </div>
</template>
<style scoped>
.export-field {
  background-color: #f7f4ed;
  color: #0b1957;
  border: 2px solid #A40033;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 14px 22px;
  border-radius: 12px;
  font-weight: 700;
  margin: 20px auto;
}
.format {
  width: 30%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}
.format-action {
  display: flex;
  flex-direction: row;
  justify-content: center;
  margin: 50px auto;
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
  background-color: #d2b3db;
  border: none;
  padding: 10px 20px;
  color: #0b1957;
  font-weight: 700;
  font-size: 24px;
  border-radius: 10px;
  margin: auto;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(210, 179, 219, 0.6);
  transition: background-color 0.3s ease, color 0.3s ease;
}
button:hover {
  background-color: #A40033;
  color: #f7f4ed;
}
</style>