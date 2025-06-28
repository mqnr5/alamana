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
            path: '/ChairManagement',
            name: 'ChairManagement',
            component: ChairManagementView
        },
        {
  path: '/ManageUsers',
  name: 'ManageUsers',
  component: () => import('@/components/ManageUsers.vue')
},
{
  path: '/SystemSettings',
  name: 'SystemSettings',
  component: () => import('@/components/SystemSettings.vue')
}


    ]
})


