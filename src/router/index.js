import HomeView from "@/views/HomeView.vue";
import { createRouter, createWebHistory } from "vue-router";
import ChairManagementView from "@/views/ChairManagementView.vue";
import ManageUsers from "@/components/ManageUsers.vue";
import SystemSettings from "@/components/SystemSettings.vue";

export const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'Home',
            component: HomeView
        },
        {
            path: '/ChairManagement',
            name: 'ChairManagement',
            component: ChairManagementView,
            props: true
        },
        {
            path: '/ManageUsers',
            name: 'ManageUsers',
            component: ManageUsers
        },
        {
            path: '/SystemSettings',
            name: 'SystemSettings',
            component: SystemSettings
        }
    ]
})


