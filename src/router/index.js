import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import SuperAdminView from "@/views/SuperAdminView.vue";
import ChairManagementView from "@/views/ChairManagementView.vue";
import ManageUsersView from "@/views/ManageUsersView.vue";
import SystemSettingsView from "@/views/SystemSettingsView.vue";
import DepartmentHeadView from "@/views/DepartmentHeadView.vue";
import EmployeeView from "@/views/EmployeeView.vue";
import EditEmployeeInfoView from "@/views/EditEmployeeInfoView.vue";
import TasksView from "@/views/TasksView.vue";
import PerformanceReportsView from "@/views/PerformanceReportsView.vue";
import MajorRequestsView from "@/views/MajorRequestsView.vue";
import EmployeeLeavesView from "@/views/EmployeeLeavesView.vue";

const router = createRouter({
  history: createWebHistory('/'),
  routes: [
    { path: '/', name: 'Home', component: HomeView },
    { path: '/SuperAdmin', name: 'SuperAdmin', component: SuperAdminView },
    { path: '/ChairManagement', name: 'ChairManagement', component: ChairManagementView, props: true },
    { path: '/ManageUsers', name: 'ManageUsers', component: ManageUsersView },
    { path: '/SystemSettings', name: 'SystemSettings', component: SystemSettingsView },
    { path: '/DepartmentHead', name: 'DepartmentHead', component: DepartmentHeadView },
    { path: '/Employee', name: 'Employee', component: EmployeeView },
    { path: '/EditEmpInfo', name: 'EditEmpInfo', component: EditEmployeeInfoView },
    { path: '/Tasks', name: 'Tasks', component: TasksView },
    { path: '/PerformanceReports', name: 'PerformanceReports', component: PerformanceReportsView },
    { path: '/MajorRequests', name: 'MajorRequests', component: MajorRequestsView },
    { path: '/Employee/Leaves', name: 'EmployeeLeaves', component: EmployeeLeavesView },
  ]
});

export default router;
