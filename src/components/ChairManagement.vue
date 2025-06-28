<script>
import TodoList from './TodoList.vue';

export default {
  name: "ChairManagement",
  components: {
    TodoList
  },
  data() {
    return {
      tasks: [
        { id: 1, title: "مراجعة البريد الرسمي", done: false },
        { id: 2, title: "تنظيم الاجتماعات", done: true },
        { id: 3, title: "متابعة تقارير الموظفين", done: false }
      ]
    }
  }
}
</script>

<template>
  <h1>إدارة الأمانة</h1>
  <TodoList :tasks="tasks" />
</template>

<style scoped>

</style>
