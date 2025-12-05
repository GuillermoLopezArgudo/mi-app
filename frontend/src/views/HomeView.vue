<template>
    <div>
        <Navbar></Navbar>
        <button @click="showModal = true" class="m-4 p-2 bg-indigo-600 text-white rounded" >Añadir Clase</button>
        <div class="min-h-screen bg-gray-50 py-8 px-4">
            <h1 class="text-3xl font-bold mb-8 text-gray-900 text-center">Nuestros Cafés</h1>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mx-auto" id="a">
                <!-- Renderizar las tarjetas de café -->
                <Card
                    v-for="(card, index) in cards"
                    :key="index"
                    :title="card.title"
                    :description="card.description"
                    :image="card.image"
                    :link="card.link"
                />
            </div>
        </div>
        <Modal :open="showModal" @close="reciveModal"></Modal>
    </div>
</template>

<script setup>
import Card from '@/components/Card.vue';
import Modal from '@/components/Modal.vue';
import Navbar from '@/components/Navbar.vue';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const cards = ref([]);
const showModal = ref(false)

// Verificar token al montar el componente
onMounted(() => {
    const token = localStorage.getItem('token');
    if (!token) {
        router.push('/login');
    }
});

// Función para recibir datos del modal
function reciveModal(valor) {
    showModal.value = false;

    //  Agregar nueva tarjeta si los datos son válidos
    if (valor && valor.title && valor.description) {
        cards.value.push({
            title: valor.title,
            description: valor.description,
            image: valor.imageUrl || "",
            link: "#"
        });
    }
}

</script>

<style lang="scss" scoped></style>