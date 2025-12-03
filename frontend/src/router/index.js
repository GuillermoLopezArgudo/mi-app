import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // Ruta para la vista de inicio de sesión
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    // Ruta para la vista de registro
    {
      path: '/register',
      name: 'register',
      component: RegisterView,
    },
  ],
})

export default router
