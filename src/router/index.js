import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import SuperAdminView from "@/views/SuperAdminView.vue";
import ChairManagementView from "@/views/ChairManagementView.vue";
import ManageUsersView from "@/views/ManageUsersView.vue";
import SystemSettingsView from "@/views/SystemSettingsView.vue";
import DepartmentHeadView from "@/views/DepartmentHeadView.vue";
import EmployeeView from "@/views/EmployeeView.vue";

const router = createRouter({
    history: createWebHistory('/'),
    routes: [
        {
            path: '/',
            name: 'Home',
            component: HomeView
        },
        {
            path: '/SuperAdmin',
            name: 'SuperAdmin',
            component: SuperAdminView
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
            component: ManageUsersView
        },
        {
            path: '/SystemSettings',
            name: 'SystemSettings',
            component: SystemSettingsView
        },
        {
            path: '/DepartmentHead',
            name: 'DepartmentHead',
            component: DepartmentHeadView
        },
        {
            path: '/Employee',
            name: 'Employee',
            component: EmployeeView
        },
        {
  path: '/PerformanceReports',
  name: 'PerformanceReports',
 component: () => import('@/views/PerformanceReports.vue')

},
{
  path: '/MajorRequests',
  name: 'MajorRequests',
  component: () => import('@/views/MajorRequests.vue')
},
{
  path: '/EmployeeView',
  name: 'EmployeeView',
  component: () => import('@/views/EmployeeView.vue')
},
{
  path: '/Tasks',
  name: 'Tasks',
  component: () => import('@/views/Tasks View.vue')
}



    ]
})

export default router;