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
            todos: [] // [{id: 1, text: '', checked: false}, {id: 2, text: '', checked: false}, ...]
        }
    },
    mounted() {
        this.todos = this.tasks
    },
    methods: {
        checkTask(task) {
            task.checked = !task.checked
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