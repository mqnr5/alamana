import HomeView from "@/views/HomeView.vue";
import { createRouter, createWebHistory } from "vue-router";
import ChairManagementView from "@/views/ChairManagementView.vue";

export const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'Home',
            component: HomeView
        },
        {
            path: 'ChairManagement',
            name: 'ChairManagement',
            component: ChairManagementView
        }
    ]
})