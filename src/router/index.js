
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ChairManagementView from '@/views/ChairManagementView.vue'

const ManageUsers = () => import('@/components/ManageUsers.vue')
const SystemSettings = () => import('@/components/SystemSettings.vue')
const SuperAdmin = () => import('@/components/SuperAdmin.vue')

const routes = [
  { path: '/', name: 'Home', component: HomeView },
  { path: '/ChairManagement', name: 'ChairManagement', component: ChairManagementView },
  { path: '/ManageUsers', name: 'ManageUsers', component: ManageUsers },
  { path: '/SystemSettings', name: 'SystemSettings', component: SystemSettings },
  { path: '/SuperAdmin', name: 'SuperAdmin', component: SuperAdmin },
  
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
