<script>
export default {
  name: 'HomePage',
  data() {
    return {
      title: 'نظام الأمانة العامة - العتبة العلوية المقدسة',
    };
  },
  methods: {
    goToSection(section, props) {
      if (props) {
        this.$router.push({ name: section, params: props });
      } else {
        this.$router.push({ name: section });
      }
    },
  },
};
</script>


<template>
  <div class="home-container">
    <div class="title">
      <h1>{{ title }}</h1>
    </div>

    <div class="section-buttons">
      <button @click="goToSection('SuperAdmin', false)" class="section-button">رئيس الأمانة</button>
      <button @click="goToSection('ChairManagement', false)" class="section-button">رئيس الإدارة</button>
      <button @click="goToSection('DepartmentHead', false)" class="section-button">رئيس القسم</button>
      <button @click="goToSection('Employee', false)" class="section-button">الموظف</button>
    </div>
  </div>
</template>
<style scoped>
.home-container {
  background-color: white;
  min-height: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 40px 20px;
  direction: rtl;
  text-align: center;
}

.title h1 {
  color: #0b1957;
  font-size: 30px;
  font-weight: bold;
  margin-bottom: 40px;
}

.section-buttons {
  display: flex;
  flex-direction: column;
  gap: 20px;
  width: 100%;
  max-width: 420px;
}

.section-button {
  background-color: #f7f4ed;
  border: 2px solid #A40033;
  color: #0b1957;
  font-size: 18px;
  padding: 15px;
  border-radius: 12px;
  cursor: pointer;
  font-weight: bold;
  transition: 0.3s;
}

.section-button:hover {
  background-color: #A40033;
  color: white;
}
</style>
