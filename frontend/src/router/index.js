import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import HomeView from '@/views/HomeView.vue'
import Notebook from '@/components/Notebook.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // Redirigir la ruta raíz a la vista de inicio de sesión
    {
      path: '/',
      redirect: '/login',
    },
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
    // Ruta para la vista principal después del inicio de sesión
    {
      path: '/home',
      name: 'home',
      component: HomeView,
    },
        // Ruta para la vista del cuaderno
    {
      path: '/notebook',
      name: 'notebook',
      component: Notebook,
    },
  ],
})

export default router
