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
      task.done = !task.done;
    }
  }
}
</script>

<template>
  <div class="tasks-container">
    <div class="tasks-list">
      <ul class="list">
        <li v-for="task in todos" :key="task.id">
          <input type="checkbox" :checked="task.done" @change="checkTask(task)">
          {{ task.title }}
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.tasks-container {
  width: 60%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.tasks-list {
  margin: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
</style>
