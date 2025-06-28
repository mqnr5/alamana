<template>
  <div class="settings-container">
    <h2>إعدادات النظام</h2>

    <div class="setting-section">
      <label for="language">اختيار اللغة:</label>
      <select id="language" v-model="language">
        <option value="ar">العربية</option>
        <option value="en">الإنجليزية</option>
      </select>
    </div>

    <div class="setting-section">
      <label>
        <input type="checkbox" v-model="darkMode" />
        تفعيل الوضع الليلي
      </label>
    </div>

    <div class="setting-section">
      <h3>النسخ الاحتياطي</h3>
      <button class="backup-btn" @click="performBackup">🔄 تنفيذ النسخ الاحتياطي الآن</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "SystemSettings",
  data() {
    return {
      language: "ar",
      darkMode: false,
    };
  },
  methods: {
    performBackup() {
      alert("✅ تم تنفيذ النسخ الاحتياطي بنجاح!");
    },
  },
};
</script>

<style scoped>
.settings-container {
  background-color: #ffffff;
  padding: 30px;
  border-radius: 15px;
  max-width: 700px;
  margin: auto;
  box-shadow: 0 0 12px rgba(0, 0, 0, 0.08);
  color: #6d7cd9;
}

h2 {
  color: #b1dfe4;
  text-align: center;
  margin-bottom: 25px;
}

.setting-section {
  background-color: #dec7e0;
  padding: 20px;
  margin-bottom: 20px;
  border-radius: 10px;
  color: #6d7cd9;
  font-size: 16px;
}

select {
  padding: 8px 12px;
  border: 2px solid #f99866;
  border-radius: 8px;
  margin-top: 10px;
  font-size: 15px;
  color: #6d7cd9;
}

input[type="checkbox"] {
  margin-left: 10px;
}

.backup-btn {
  background-color: #ffc046;
  color: white;
  border: none;
  padding: 10px 18px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: bold;
}

.backup-btn:hover {
  background-color: #f99866;
}
</style>
