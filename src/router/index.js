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
import ReportView from "@/views/ReportView.vue";
import DepartmentOverviewView from "@/views/DepartmentOverviewView.vue";
import ReviewReportsView from "@/views/ReviewReportsView.vue";
import UrgentTasksView from "@/views/UrgentTasksView.vue";
import ManageStaffView from "@/views/ManageStaffView.vue";
import LoginView from "@/views/LoginView.vue";
import AddTask from "@/components/AddTask.vue";

const routes = [
  { path: '/', name: 'Home', component: HomeView },
  { path: '/SuperAdmin', name: 'SuperAdmin', component: SuperAdminView },
  { path: '/ChairManagement', name: 'ChairManagement', component: ChairManagementView, props: true },
  { path: '/ManageUsers', name: 'ManageUsers', component: ManageUsersView },
  { path: '/SystemSettings', name: 'SystemSettings', component: SystemSettingsView },
  { path: '/DepartmentHead', name: 'DepartmentHead', component: DepartmentHeadView },
  { path: '/Employee', name: 'Employee', component: EmployeeView },
  { path: '/EditEmpInfo', name: 'EditEmpInfoView', component: EditEmployeeInfoView, props: true },
  { path: '/Tasks', name: 'Tasks', component: TasksView },
  { path: '/AddTask', name: 'AddTask', component: AddTask },
  { path: '/PerformanceReports', name: 'PerformanceReports', component: PerformanceReportsView },
  { path: '/MajorRequests', name: 'MajorRequests', component: MajorRequestsView },
  { path: '/EmployeeLeaves', name: 'EmployeeLeaves', component: EmployeeLeavesView },
  { path: '/ReportViewer', name: 'ReportViewer', component: ReportView },
  { path: '/ReportView', name: 'ReportView', component: ReportView },
  { path: '/DepartmentOverview', name: 'DepartmentOverview', component: DepartmentOverviewView },
  { path: '/ReviewReports', name: 'ReviewReports', component: ReviewReportsView },
  { path: '/ManageStaff', name: 'ManageStaff', component: ManageStaffView },
  { path: '/UrgentTasks', name: 'UrgentTasks', component: UrgentTasksView },
  { path: '/login', name: 'Login', component: LoginView },
];

const router = createRouter({
  history: createWebHistory('/'),
  routes: routes
});

router.beforeEach(() => {
  const loggedIn = localStorage.getItem('loggedIn')
  if (!loggedIn) {
    this.$router.push({ name: '/login' })
  }
})
export default router;
