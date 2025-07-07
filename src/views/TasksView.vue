<template>
  <div class="tasks-container">
    <h2>مهامي اليومية</h2>
    <div class="filters">
      <label>حالة المهمة:</label>
      <select v-model="filterStatus">
        <option value="all">الكل</option>
        <option value="pending">معلقة</option>
        <option value="in-progress">قيد التنفيذ</option>
        <option value="completed">مكتملة</option>
      </select>
    </div>

    <transition-group name="task-list" tag="div" class="tasks-list">
      <div
        v-for="task in filteredTasks"
        :key="task.id"
        class="task-card"
        :class="task.status"
      >
        <h3>{{ task.title }}</h3>
        <p>{{ task.text }}</p>
        <div class="task-meta">
          <span>تاريخ الاستحقاق: {{ task.deadline_date }}</span>
          <span :class="'status ' + task.status">{{ statusText(task.status) }}</span>
        </div>
        <div class="progress-bar">
          <div
            class="progress-fill"
            :style="{ width: progressWidth(task.status) }"
          ></div>
        </div>
        <div class="actions">
          <button
            v-if="task.status !== 'completed'"
            @click="updateStatus(task.id, nextStatus(task.status))"
            class="update-btn"
          >
            {{ nextStatusText(task.status) }}
          </button>
        </div>
      </div>
    </transition-group>

    <div v-if="filteredTasks.length === 0" class="no-tasks">لا توجد مهام جديدة.</div>
  </div>
</template>

<script>
import { get_missions, update_task } from '@/api/public_operations';

export default {
  name: "TasksView",
  data() {
    return {
      filterStatus: "all",
      tasks: [],
    };
  },
  async mounted() {
    const uid = localStorage.getItem('loggedIn')
    this.tasks = await get_missions(uid)
  },
  computed: {
    filteredTasks() {
      if (this.filterStatus === "all") return this.tasks;
      return this.tasks.filter((t) => t.status === this.filterStatus);
    },
  },
  methods: {
    async updateStatus(id, newStatus) {
      const task = this.tasks.find((t) => t.id === id);
      if (task) task.status = newStatus;
      await update_task(task.id, task)
    },
    nextStatus(status) {
      switch (status) {
        case "pending":
          return "in-progress";
        case "in-progress":
          return "completed";
        default:
          return "completed";
      }
    },
    statusText(status) {
      switch (status) {
        case "pending":
          return "معلقة";
        case "in-progress":
          return "قيد التنفيذ";
        case "completed":
          return "مكتملة";
        default:
          return "";
      }
    },
    nextStatusText(status) {
      switch (status) {
        case "pending":
          return "ابدأ التنفيذ";
        case "in-progress":
          return "إنهاء المهمة";
        default:
          return "";
      }
    },
    progressWidth(status) {
      switch (status) {
        case "pending":
          return "20%";
        case "in-progress":
          return "60%";
        case "completed":
          return "100%";
        default:
          return "0%";
      }
    },
  },
};
</script>

<style scoped>
.tasks-container {
  max-width: 900px;
  margin: auto;
  background-color: #ffffff;
  padding: 30px;
  border-radius: 15px;
  color: #0b1957;
  direction: rtl;
  text-align: right;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

h2 {
  font-size: 30px;
  font-weight: 700;
  margin-bottom: 20px;
  color: #0b1957;
}

.filters {
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 15px;
}

select {
  padding: 8px 15px;
  border-radius: 8px;
  border: 2px solid #A40033;
  background-color: #f7f4ed;
  color: #0b1957;
  font-weight: 600;
  cursor: pointer;
  transition: border-color 0.3s ease;
}

select:hover,
select:focus {
  border-color: #4E5174;
  outline: none;
}

.tasks-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.task-card {
  background-color: #d2b3db;
  padding: 20px 25px;
  border-radius: 15px;
  box-shadow: 0 5px 15px rgba(210, 179, 219, 0.4);
  position: relative;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: default;
}

.task-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 10px 20px rgba(164, 0, 51, 0.5);
}

.task-card.pending {
  border-left: 6px solid #A40033;
}

.task-card.in-progress {
  border-left: 6px solid #4E5174;
}

.task-card.completed {
  border-left: 6px solid #0b1957;
  opacity: 0.8;
}

.task-card h3 {
  margin: 0 0 10px 0;
  font-weight: 700;
  font-size: 22px;
  color: #0b1957;
}

.task-card p {
  font-size: 16px;
  margin-bottom: 15px;
  color: #4E5174;
}

.task-meta {
  display: flex;
  justify-content: space-between;
  font-weight: 600;
  margin-bottom: 15px;
  color: #0b1957;
}

.status {
  padding: 6px 14px;
  border-radius: 12px;
  font-weight: 700;
  color: white;
  user-select: none;
}

.status.pending {
  background-color: #A40033;
}

.status.in-progress {
  background-color: #4E5174;
}

.status.completed {
  background-color: #0b1957;
}

.progress-bar {
  background-color: #f7f4ed;
  border-radius: 15px;
  height: 18px;
  overflow: hidden;
  margin-bottom: 15px;
  box-shadow: inset 0 1px 4px rgba(0,0,0,0.1);
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #0b1957, #4E5174);
  transition: width 0.5s ease;
}

.actions {
  display: flex;
  justify-content: flex-end;
}

.update-btn {
  background-color: #A40033;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 12px;
  font-weight: 700;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.update-btn:hover {
  background-color: #4E5174;
}

/* Transitions for task-list */
.task-list-enter-from,
.task-list-leave-to {
  opacity: 0;
  transform: translateY(20px);
}

.task-list-enter-active,
.task-list-leave-active {
  transition: all 0.4s ease;
}


.no-tasks {
  margin-top: 40px;
  font-weight: 700;
  font-size: 18px;
  color: #A40033;
  text-align: center;
}
</style>