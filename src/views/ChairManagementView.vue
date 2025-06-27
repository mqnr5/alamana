<script>
export default {
    name: 'ChairManagementView',
}
</script>
<template>
    <div class="body">
        <h1>رئيس الإدارة</h1>
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
</template>
<style scoped>
.body {
    background-color: #EFDFC5;
    justify-items: center;
}
</style>