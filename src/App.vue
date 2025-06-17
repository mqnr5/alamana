<template>
  <div class="app-container">
    <h1>نظام الأمانة العامة - العتبة العلوية</h1>

    <!-- القائمة الرئيسية -->
    <div v-if="!currentView" class="nav-buttons">
      <button @click="goToSection('admin')">رئيس الإدارة</button>
      <button @click="goToSection('section')">رئيس القسم</button>
      <button @click="goToSection('employee')">الموظف</button>
    </div>

    <!-- رئيس الإدارة -->
    <div v-if="currentView === 'admin'" class="section-box">
      <h2>رئيس الإدارة</h2>
      <p>الدور الأساسي لرئيس الإدارة هو الإشراف الكامل والتنسيق بين الأقسام المختلفة داخل الأمانة العامة.</p>
      
      <ul>
        <li>الإشراف الكامل على جميع الأقسام بما يشمل متابعة العمل وتقارير الإنجاز.</li>
        <li>استلام تقارير الإنجاز اليومية والأسبوعية من رؤساء الأقسام.</li>
        <li>إصدار التعليمات والتوجيهات لرؤساء الأقسام حسب الحاجة.</li>
        <li>متابعة حالة كل قسم (نشط، متأخر، بحاجة لدعم).</li>
      </ul>

      <h3>تقارير رئيس الإدارة</h3>
      <ul class="report-list">
        <li>تقرير نشاط الأقسام - الأسبوع الأول من الشهر</li>
        <li>تقرير إنجاز مهام الطوارئ</li>
        <li>تحليل نقاط القوة والضعف للأقسام</li>
      </ul>

      <div class="nav-sub-buttons">
        <button :disabled="adminPage === 1" @click="adminPage--">رجوع</button>
        <button :disabled="adminPage === 2" @click="adminPage++">التالي</button>
      </div>

      <!-- صفحات فرعية لرئيس الإدارة -->
      <div v-if="adminPage === 1" class="admin-subpage">
        <h4>الصفحة 1: المهام الأساسية</h4>
        <p>رئيس الإدارة يقوم بمتابعة تنفيذ الخطط الاستراتيجية والتأكد من التنسيق بين الأقسام المختلفة.</p>
      </div>
      <div v-if="adminPage === 2" class="admin-subpage">
        <h4>الصفحة 2: التعليمات والتوجيهات</h4>
        <p>يمكن لرئيس الإدارة إصدار تعليمات محددة لرؤساء الأقسام لتسريع تنفيذ بعض المهام أو تعديل الخطط حسب المستجدات.</p>
      </div>

      <button @click="currentView = null" class="back-main">العودة إلى القائمة الرئيسية</button>
    </div>

    <!-- رئيس القسم -->
    <div v-if="currentView === 'section'" class="section-box">
      <h2>رئيس القسم</h2>
      <p>رئيس القسم مسؤول عن تنظيم فريق العمل داخل القسم ومتابعة تنفيذ المهام المحددة.</p>

      <ul>
        <li>عرض قائمة الموظفين في القسم وتوزيع المهام عليهم.</li>
        <li>متابعة حالة المهام الموكلة لكل موظف.</li>
        <li>رفع تقارير دورية إلى رئيس الإدارة.</li>
        <li>تقديم الدعم والمساندة للموظفين في حال وجود مشاكل أو صعوبات في تنفيذ المهام.</li>
      </ul>

      <h3>قائمة الموظفين في القسم</h3>
      <ul class="employee-list">
        <li>أحمد - مسؤول الوثائق</li>
        <li>سارة - متابعة المشاريع</li>
        <li>خالد - الدعم الفني</li>
      </ul>

      <h3>مثال على مهام الموظفين</h3>
      <ul class="task-list">
        <li>أحمد: أرشفة المستندات الجديدة - الحالة: قيد التنفيذ</li>
        <li>سارة: إعداد تقرير نهاية الشهر - الحالة: لم تبدأ</li>
        <li>خالد: تحديث النظام الأمني - الحالة: مكتملة</li>
      </ul>

      <div class="nav-sub-buttons">
        <button :disabled="sectionPage === 1" @click="sectionPage--">رجوع</button>
        <button :disabled="sectionPage === 2" @click="sectionPage++">التالي</button>
      </div>

      <div v-if="sectionPage === 1" class="section-subpage">
        <h4>الصفحة 1: تنظيم فريق العمل</h4>
        <p>رئيس القسم يقوم بتحديد المهام بناءً على مهارات وقدرات كل موظف لضمان أفضل أداء.</p>
      </div>

      <div v-if="sectionPage === 2" class="section-subpage">
        <h4>الصفحة 2: متابعة وتقييم الأداء</h4>
        <p>يتم تحديث حالة المهام بشكل دوري ليتم تقييم الإنجاز ومعالجة العقبات بسرعة.</p>
      </div>

      <button @click="currentView = null" class="back-main">العودة إلى القائمة الرئيسية</button>
    </div>

    <!-- الموظف -->
    <div v-if="currentView === 'employee'" class="section-box">
      <h2>الموظف</h2>
      <p>الموظف يقوم بتنفيذ المهام المسندة إليه ويقوم بتحديث حالتها باستمرار.</p>

      <ul>
        <li>عرض قائمة المهام المسندة له من رئيس القسم.</li>
        <li>تحديث حالة المهمة (قيد التنفيذ، مكتملة، مؤجلة).</li>
        <li>تلقي الملاحظات والتعليمات الخاصة.</li>
        <li>إرسال إشعار عند إتمام المهمة بنجاح.</li>
      </ul>

      <h3>المهام الحالية</h3>
      <ul class="employee-tasks">
        <li><strong>أرشفة المستندات:</strong> الحالة: <span class="status ongoing">قيد التنفيذ</span></li>
        <li><strong>إعداد تقرير حالة المشروع:</strong> الحالة: <span class="status completed">مكتملة</span></li>
        <li><strong>صيانة الأجهزة المكتبية:</strong> الحالة: <span class="status delayed">مؤجلة</span></li>
      </ul>

      <div class="nav-sub-buttons">
        <button :disabled="employeePage === 1" @click="employeePage--">رجوع</button>
        <button :disabled="employeePage === 2" @click="employeePage++">التالي</button>
      </div>

      <div v-if="employeePage === 1" class="employee-subpage">
        <h4>الصفحة 1: مهام الموظف</h4>
        <p>تحديث حالة المهمة ضروري لتتبع التقدم وإبلاغ رئيس القسم.</p>
      </div>

      <div v-if="employeePage === 2" class="employee-subpage">
        <h4>الصفحة 2: التواصل والملاحظات</h4>
        <p>الموظف يمكنه إرسال ملاحظات أو طلب مساعدة عبر النظام في حال وجود أي صعوبات.</p>
      </div>

      <button @click="currentView = null" class="back-main">العودة إلى القائمة الرئيسية</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentView: null,
      adminPage: 1,
      sectionPage: 1,
      employeePage: 1,
    };
  },
  methods: {
    goToSection(section) {
      this.currentView = section;
      // Reset subpages when entering section
      if (section === 'admin') this.adminPage = 1;
      if (section === 'section') this.sectionPage = 1;
      if (section === 'employee') this.employeePage = 1;
    },
  },
};
</script>

<style>
body {
  margin: 0;
  font-family: 'Segoe UI', sans-serif;
  background-color: #EFDFC5;
  color: #380F17;
}

.app-container {
  text-align: center;
  padding: 30px;
  min-height: 100vh;
}

h1 {
  margin-bottom: 40px;
}

.nav-buttons {
  margin-bottom: 40px;
}

button {
  margin: 10px;
  padding: 12px 28px;
  background-color: #380F17;
  color: #EFDFC5;
  border: none;
  border-radius: 10px;
  font-size: 18px;
  cursor: pointer;
  transition: all 0.3s ease;
}

button:hover:not(:disabled) {
  background-color: #8F0B13;
  color: #252B2B;
}

button:disabled {
  background-color: #4C4F54;
  cursor: default;
  color: #8F0B13;
}

.section-box {
  background-color: #380F17;
  color: #EFDFC5;
  width: 90%;
  max-width: 900px;
  margin: auto;
  padding: 25px 30px;
  border-radius: 15px;
  text-align: start;
  box-shadow: 0 0 12px rgba(56, 15, 23, 0.6);
}

.section-box ul {
  list-style: none;
  padding: 0;
}

.section-box ul li {
  padding: 10px 0;
  border-bottom: 1px solid #EFDFC5;
  font-size: 17px;
}

.report-list,
.employee-list,
.task-list,
.employee-tasks {
  margin-top: 15px;
  font-size: 16px;
}

.nav-sub-buttons {
  margin: 20px 0;
  display: flex;
  justify-content: space-between;
}

.admin-subpage,
.section-subpage,
.employee-subpage {
  background-color: #252B2B;
  padding: 15px 20px;
  border-radius: 10px;
  margin-top: 15px;
  font-size: 16px;
  color: #EFDFC5;
}

.status {
  font-weight: bold;
  padding: 2px 8px;
  border-radius: 7px;
}

.status.ongoing {
  background-color: #8F0B13;
  color: #EFDFC5;
}

.status.completed {
  background-color: #4C4F54;
  color: #EFDFC5;
}

.status.delayed {
  background-color: #252B2B;
  color: #8F0B13;
}

.back-main {
  display: block;
  margin: 25px auto 0;
  background-color: #8F0B13;
  color: #EFDFC5;
  padding: 10px 25px;
  font-size: 16px;
}

.back-main:hover {
  background-color: #380F17;
  color: #EFDFC5;
}
</style>
