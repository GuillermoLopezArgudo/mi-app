<script setup>
import { useRoute } from 'vue-router';
import Navbar from '@/components/Navbar.vue';

const route = useRoute();

// Show navbar only on home page
const showNavbar = route.path === '/home';
</script>

<template>
    <Navbar v-if="showNavbar" />
    <router-view />
</template>
