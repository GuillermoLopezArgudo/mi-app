<template>
    <div v-if="open" class="fixed inset-0 bg-black/50 flex justify-center items-center z-50">
        <div class="bg-white rounded-xl p-6 shadow-lg w-80">
            <div class="flex justify-between mb-4">
                <h2 class="text-xl font-bold ">Nueva Clase</h2>
                <button class="text-xl font-bold text-red-600" @click="closeModal">X</button>
            </div>

            <slot>
                <input type="text" placeholder="Título de la clase"
                    class="w-full mb-3 p-2 border border-gray-300 rounded" v-model="title" />
                <textarea placeholder="Descripción de la clase" class="w-full mb-3 p-2 border border-gray-300 rounded"
                    v-model="description"></textarea>
                <input type="text" placeholder="URL de la imagen" class="w-full mb-3 p-2 border border-gray-300 rounded"
                    v-model="imageUrl" />
            </slot>
            <button class="mt-4 px-4 py-2 bg-indigo-600 text-white rounded hover:bg-indigo-700" @click="submitModal">
                Enviar
            </button>
        </div>
    </div>
</template>

<script setup>

import { ref } from 'vue';
// Definición de las props del componente
defineProps({
    open: Boolean,
})
// Definición de los eventos emitidos por el componente
const emit = defineEmits(['close']);

const title = ref('');
const description = ref('');
const imageUrl = ref('');

// Función para enviar datos al componente padre
function submitModal() {

   emit('close', { title: title.value, description: description.value, imageUrl: imageUrl.value });
    resetFields();
}

// Función para cerrar el modal sin enviar datos
function closeModal() {
    emit('close');
    resetFields();
}

// Función para resetear los campos del modal
function resetFields() {
    title.value = '';
    description.value = '';
    imageUrl.value = '';
}

</script>
