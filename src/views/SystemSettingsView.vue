<template>
  <div class="settings-container">
    <h2>إعدادات النظام</h2>

    <div class="setting-section">
      <label for="language">اختيار اللغة : </label>
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
  background-color: #ffffff; /* خلفية بيضاء عامة */
  padding: 30px;
  border-radius: 15px;
  max-width: 700px;
  margin: auto;
  box-shadow: 0 0 12px rgba(0, 0, 0, 0.08);
  color: #0b1957; /* لون الخطوط الأساسي */
  direction: rtl;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

h2 {
  color: #0b1957; /* عناوين باللون الداكن */
  text-align: center;
  margin-bottom: 25px;
  font-weight: 700;
  font-size: 28px;
}

.setting-section {
  background-color: #e9f3ff; /* خلفية هادئة ومريحة للحقول */
  padding: 20px;
  margin-bottom: 20px;
  border-radius: 12px;
  color: #0b1957;
  font-size: 16px;
  border: 2px solid #d2b3db; /* إطار أنيق وناعم */
  box-shadow: 2px 2px 8px rgba(210,179,219,0.3);
}

select {
  padding: 10px 14px;
  border: 2px solid #d2b3db; /* إطار أفتح */
  border-radius: 12px;
  margin-top: 10px;
  font-size: 16px;
  color: #0b1957;
  background-color: #f7f4ed; /* خلفية مريحة */
  width: 100%;
  box-sizing: border-box;
  transition: border-color 0.3s ease;
}

select:hover, select:focus {
  border-color: #A40033; /* لون بارز عند التفاعل */
  outline: none;
}

input[type="checkbox"] {
  margin-left: 10px;
  width: 18px;
  height: 18px;
  cursor: pointer;
}

.backup-btn {
  background-color: #A40033; /* لون خلفية الأزرار */
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 12px;
  cursor: pointer;
  font-weight: 700;
  font-size: 16px;
  display: block;
  margin: 30px auto 0 auto;
  transition: background-color 0.3s ease;
  box-shadow: 0 4px 10px rgba(164,0,51,0.4);
}

.backup-btn:hover {
  background-color: #4E5174; /* لون بديل عند التمرير */
}
</style>
