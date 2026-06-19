import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import LoginPage from '../views/LoginPage.vue'
import SignupPage from '../views/SignupPage.vue'
import HistoryPage from '../views/HistoryPage.vue'
import AdminPage from '../views/AdminPage.vue'

const routes = [
  { path: '/', name: 'home', component: HomePage },
  { path: '/login', name: 'login', component: LoginPage },
  { path: '/signup', name: 'signup', component: SignupPage },
  { path: '/history', name: 'history', component: HistoryPage },
  { path: '/admin', name: 'admin', component: AdminPage },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
