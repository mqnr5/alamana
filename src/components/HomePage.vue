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
  height: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 40px 20px;
}

.title h1 {
  color: #b1dfe4;
  font-size: 28px;
  font-weight: bold;
  margin-bottom: 40px;
  text-align: center;
}

.section-buttons {
  display: flex;
  flex-direction: column;
  gap: 20px;
  width: 100%;
  max-width: 400px;
}

.section-button {
  background-color: #c1e0ba;
  border: 2px solid #f99866;
  color: #6d7cd9;
  font-size: 18px;
  padding: 15px;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 500;
}

.section-button:hover {
  background-color: #fac5d4;
  color: white;
}
</style>
