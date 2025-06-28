<script>
import TodoList from './TodoList.vue';

export default {
  name: "ChairManagement",
  components: {
    TodoList
  },
  props: {
    tasks: {
      type: Array,
      required: true
    }
},
}
</script>

<template>
  <h1>إدارة الأمانة</h1>
  <TodoList :tasks="tasks" />
</template>

<style scoped>

</style>
