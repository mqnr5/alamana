<template>
  <div class="app-container">
    <HomePage v-if="!currentView" @navigate="goToSection" />

    <!-- رئيس القسم -->
    <div v-if="currentView === 'section'" class="section-box">
      <h2>رئيس القسم</h2>
      <p>رئيس القسم مسؤول عن تنظيم فريق العمل داخل القسم ومتابعة تنفيذ المهام المحددة.</p>

      <ul>
        <li>عرض قائمة الموظفين في القسم وتوزيع المهام عليهم.</li>
        <li>متابعة حالة المهام الموكلة لكل موظف.</li>
        <li>رفع تقارير دورية إلى رئيس الإدارة.</li>
        <li>تقديم الدعم والمساندة للموظفين.</li>
      </ul>

      <h3>قائمة الموظفين في القسم</h3>
      <ul class="employee-list">
        <li>أحمد - مسؤول الوثائق</li>
        <li>سارة - متابعة المشاريع</li>
        <li>خالد - الدعم الفني</li>
      </ul>

      <h3>مثال على مهام الموظفين</h3>
      <ul class="task-list">
        <li>أحمد: أرشفة المستندات - <span class="status ongoing">قيد التنفيذ</span></li>
        <li>سارة: إعداد تقرير - <span class="status delayed">لم تبدأ</span></li>
        <li>خالد: تحديث النظام - <span class="status completed">مكتملة</span></li>
      </ul>

      <div class="nav-sub-buttons">
        <button :disabled="sectionPage === 1" @click="sectionPage--">رجوع</button>
        <button :disabled="sectionPage === 2" @click="sectionPage++">التالي</button>
      </div>

      <div v-if="sectionPage === 1" class="section-subpage">
        <h4>تنظيم فريق العمل</h4>
        <p>يتم توزيع المهام حسب القدرات لضمان الجودة.</p>
      </div>
      <div v-if="sectionPage === 2" class="section-subpage">
        <h4>متابعة وتقييم الأداء</h4>
        <p>يتم تحديث المهام لمراقبة الإنجاز.</p>
      </div>

      <button class="back-main" @click="currentView = null">العودة</button>
    </div>

    <!-- الموظف -->
    <div v-if="currentView === 'employee'" class="section-box">
      <h2>الموظف</h2>
      <p>ينفذ المهام ويحدث حالتها باستمرار.</p>

      <ul>
        <li>عرض المهام المكلف بها.</li>
        <li>تحديث حالة المهمة.</li>
        <li>استلام التعليمات والملاحظات.</li>
        <li>إعلام رئيس القسم عند الإكمال.</li>
      </ul>

      <h3>المهام الحالية</h3>
      <ul class="employee-tasks">
        <li>أرشفة المستندات: <span class="status ongoing">قيد التنفيذ</span></li>
        <li>تقرير حالة المشروع: <span class="status completed">مكتملة</span></li>
        <li>صيانة الأجهزة: <span class="status delayed">مؤجلة</span></li>
      </ul>

      <div class="nav-sub-buttons">
        <button :disabled="employeePage === 1" @click="employeePage--">رجوع</button>
        <button :disabled="employeePage === 2" @click="employeePage++">التالي</button>
      </div>

      <div v-if="employeePage === 1" class="employee-subpage">
        <h4>مهام الموظف</h4>
        <p>التحديث المستمر لحالة المهام يساعد بالتقييم.</p>
      </div>
      <div v-if="employeePage === 2" class="employee-subpage">
        <h4>التواصل</h4>
        <p>يمكن إرسال ملاحظات لرئيس القسم عند الحاجة.</p>
      </div>

      <button class="back-main" @click="currentView = null">العودة</button>
    </div>
  </div>
</template>

<script>
import HomePage from './components/HomePage.vue';
export default {
  components: { HomePage },
  data() {
    return {
      currentView: null,
      sectionPage: 1,
      employeePage: 1,
    };
  },
  methods: {
    goToSection(section) {
      this.currentView = section;
      if (section === 'section') this.sectionPage = 1;
      if (section === 'employee') this.employeePage = 1;
    },
  },
};
</script>

<style scoped>
.app-container {
  font-family: 'Segoe UI', sans-serif;
  background-color: #ffffff;
  padding: 40px 20px;
  min-height: 100vh;
  color: #6D7CD9;
}

.section-box {
  background-color: #dec7e0;
  color: #6D7CD9;
  padding: 25px 30px;
  border-radius: 15px;
  box-shadow: 0 0 12px rgba(0, 0, 0, 0.1);
  max-width: 900px;
  margin: auto;
  margin-bottom: 40px;
}

h2 {
  color: #b1dfe4;
  font-size: 24px;
  margin-bottom: 10px;
}

h3 {
  color: #FFC046;
  margin-top: 20px;
}

h4 {
  color: #FAC5D4;
  margin: 10px 0;
}

ul {
  list-style: none;
  padding: 0;
  font-size: 16px;
}

li {
  margin-bottom: 8px;
}

.status {
  padding: 4px 10px;
  border-radius: 10px;
  font-weight: bold;
}

.status.ongoing {
  background-color: #F99866;
  color: white;
}

.status.completed {
  background-color: #C1E0BA;
  color: #6D7CD9;
}

.status.delayed {
  background-color: #FFC046;
  color: white;
}

.nav-sub-buttons {
  display: flex;
  justify-content: space-between;
  margin: 20px 0;
}

button {
  background-color: #C1E0BA;
  color: #6D7CD9;
  border: 2px solid #F99866;
  padding: 10px 20px;
  border-radius: 10px;
  font-weight: bold;
  cursor: pointer;
  transition: 0.3s ease;
}

button:hover:not(:disabled) {
  background-color: #FAC5D4;
  color: white;
}

button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.section-subpage,
.employee-subpage {
  background-color: #ffffff;
  padding: 15px;
  border-radius: 10px;
  border: 1px solid #F99866;
  color: #6D7CD9;
}

.back-main {
  margin: 20px auto 0;
  display: block;
}
</style>
