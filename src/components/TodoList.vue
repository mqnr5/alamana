<script>
export default {
  name: 'TodoList',
  props: {
    tasks: {
      type: Array,
      required: false
    }
  },
  data() {
    return {
      todos: []
    }
  },
  mounted() {
    this.todos = this.tasks || []
  },
  methods: {
    checkTask(task) {
      task.checked = !task.checked;
    }
  }
}
</script>

<template>
  <div class="tasks-container">
    <div class="tasks-list">
      <ul class="list">
        <li v-for="task in todos" :key="task.id">
          <input type="checkbox" :checked="task.checked" @change="checkTask(task)">
          {{ task.text }}
        </li>
      </ul>
    </div>
  </div>
</template>
<style scoped>
.tasks-container {
  width: 70%;
  min-height: 100vh;
  background-color: #ffffff;
  padding: 30px;
  border-radius: 15px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.05);
  margin: auto;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  direction: rtl;
  text-align: right;
  color: #0b1957;
}

.tasks-list {
  margin-top: 20px;
  width: 100%;
  background-color: #f7f4ed;
  border: 2px dashed #d2b3db;
  padding: 20px;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  gap: 15px;
}
</style>
