<template>
    <div>
        <Navbar></Navbar>
        <button @click="showModal = true" class="m-4 p-2 bg-indigo-600 text-white rounded">Añadir Clase</button>
        <div class="min-h-screen bg-gray-50 py-8 px-4">
            <h1 class="text-3xl font-bold mb-8 text-gray-900 text-center">Nuestros Cards</h1>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mx-auto" id="a">
                <!-- Renderizar las tarjetas de café -->
                <Card v-for="card in cards" :key="card.id" :id="card.id" :title="card.title" :description="card.description"
                    :image="card.image" :link="card.link"  @deleted="deletedCard"/>
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
const BASE_URL = "http://localhost:5000";

// Verificar token al montar el componente
onMounted(() => {
    const token = localStorage.getItem('token');
    if (!token) {
        router.push('/login');
    } else {
        getCards();
    }
});

// Función para recibir datos del modal
function reciveModal(valor) {
    showModal.value = false;

    //  Agregar nueva tarjeta si los datos son válidos
    if (valor && valor.title && valor.description) {
        const newCard = {
            title: valor.title,
            description: valor.description,
            file: valor.file,
            link: "#"
        };

        cards.value.push(newCard);
        addCard(newCard);
    }
}

// Función para agregar una nueva tarjeta al backend
async function addCard(card) {
    try {
        const token = localStorage.getItem("token");
        const formData = new FormData();
        formData.append("title", card.title);
        formData.append("description", card.description);
        if (card.file) formData.append("image", card.file);

        const res = await fetch(`${BASE_URL}/api/cards`, {
            method: "POST",
            headers: {
                "Authorization": `Bearer ${token}`
            },
            body: formData
        });

        const json = await res.json();

        if (!res.ok) {
            console.error("Error:", json.error || json.message || "Error al enviar card");
        } else {
            console.log("Card creada exitosamente");
            if (json.card.urlimage) {
                const lastCard = cards.value[cards.value.length - 1];
                lastCard.image = json.card.urlimage
                    ? `${BASE_URL}${json.card.urlimage}`
                    : `${BASE_URL}/static/images/clase1.jpg`;

            }
        }
    } catch (err) {
        console.error("Error de conexión:", err);
    }
}

// Función para obtener las tarjetas desde el backend
async function getCards() {
    const token = localStorage.getItem("token");
    if (!token) {
        console.error("No hay token, inicia sesión primero.");
        return;
    }

    try {
        const res = await fetch(`${BASE_URL}/api/cards`, {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json"
            }
        });

        const json = await res.json();

        if (res.ok) {
            cards.value = json.cards.map(card => ({
                id: card.id,
                title: card.title,
                description: card.description,
                image: card.urlimage ? `${BASE_URL}${card.urlimage}` : `${BASE_URL}/static/images/clase1.jpg`,
                link: "#"
            }));
        } else {
            console.error("Error:", json.error || json.message);
        }
    } catch (err) {
        console.error("Error de conexión:", err);
    }
}

// Función para eliminar una tarjeta
async function deletedCard(valor) {
    try {
        const res = await fetch(`${BASE_URL}/api/cards/${valor.id}`, {
            method: "DELETE",
            headers: {
                "Authorization": `Bearer ${localStorage.getItem("token")}`
            }
        });

        if (!res.ok) {
            console.error("Error eliminando card");
            return;
        }

        cards.value = cards.value.filter(c => c.id !== valor.id);
        
    } catch (error) {
        console.error("Error de conexión", error);
    }
}


</script>

<style lang="scss" scoped></style>