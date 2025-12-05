<template>
  <nav class="bg-white shadow-md">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <!-- Logo -->
        <router-link to="/home" class="flex items-center space-x-2">
          <img src="/images/favicon.ico" alt="Logo" class="h-10 w-10 rounded">
          <span class="text-2xl font-bold text-indigo-600">Mi App</span>
        </router-link>

        <!-- Navigation Links -->
        <div class="hidden md:flex items-center space-x-8">
          <router-link to="/home" class="text-gray-700 hover:text-indigo-600 transition font-medium">Home</router-link>
          <button @click="closesession" class="px-4 py-2 bg-indigo-600 text-white rounded-md hover:bg-indigo-700 transition">Cerrar Sesión</button>
        </div>

        <!-- Mobile Menu Button -->
        <div class="md:hidden">
          <button @click="toggleMenu" class="text-gray-700 hover:text-indigo-600 transition">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path v-if="!mobileMenuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
              <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>
      </div>

      <!-- Mobile Menu -->
      <div v-if="mobileMenuOpen" class="md:hidden bg-gray-50 border-t">
        <router-link to="/home" class="block px-4 py-3 text-gray-700 hover:bg-gray-100 transition">Home</router-link>
        <button @click="closesession" class="w-full text-left block px-4 py-3 text-indigo-600 font-medium hover:bg-gray-100 transition">Cerrar Sesión</button>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

// Estado del menú móvil
const router = useRouter();
const mobileMenuOpen = ref(false);

// Función para alternar el menú móvil
const toggleMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value;
};

// Función para cerrar sesión
const closesession = () => {
  localStorage.removeItem('token');
  router.push('/login');
};

</script>

<style lang="scss" scoped>

</style>