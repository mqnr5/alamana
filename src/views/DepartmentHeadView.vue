<script>
import TodoList from '@/components/TodoList.vue';

export default {
    name: 'DepartmentHeadView',
    components: {
        TodoList
    },
    data() {
        return {
            tasks: [
                { id: 1, text: 'مراجعة التقارير اليومية', checked: false },
                { id: 2, text: 'اجتماع مع فريق العمل', checked: true },
                { id: 3, text: 'إعداد خطة الأسبوع القادم', checked: false }
            ]
        };
    },
    methods: {
        // Define your methods here
    },
    mounted() {
        // Code to run when the component is mounted
    }
};
</script>
<template>
    <div class="view">
        <span>رئيس القسم</span>
        <TodoList :tasks="tasks" />
        <button @click="$router.go(-1)">رجوع</button>
    </div>
</template>
<style scoped>
.view {
  background-color: #ffffff;
  color: #0b1957;
  font-size: 26px;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 40px 20px;
  border-radius: 15px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.05);
  max-width: 900px;
  margin: auto;
}
</style>
