<template>
  <div class="bg-white rounded-xl shadow-md overflow-hidden hover:shadow-lg transition cursor-pointer" @click="handleClick">
    <img
      class="w-full h-48 object-cover"
      :src="image"
      :alt="title"
      loading="lazy"
    />
    <div class="p-4">
      <h2 class="text-xl font-bold mb-1">{{title}}</h2>
      <p class="text-gray-700 text-sm mb-3">
        {{ description }}
      </p>
    </div>
    <div class="flex justify-between mb-4">
      <button @click.stop="editeClass" type="submit" class="m-2 py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500 transition">Editar</button>
      <button @click.stop="deletedClass" type="submit" class="m-2 py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 transition">Eliminar</button>
    </div>
  </div>
</template>


<script setup>
import { useRouter } from 'vue-router';
import { defineProps } from 'vue';

//  Definición de las props del componente
const props = defineProps({
  id: { type: Number, default: null },
  title: { type: String, required: true },
  description: { type: String, required: true },
  image: { type: String, default: "" },
  link: { type: String, default: "" }
})

const router = useRouter();
const emit = defineEmits(['deleted']);

// Manejar el clic en la tarjeta
function handleClick() {
  if (props.link && props.link !== "#") {
    router.push(props.link);
  }
}

// Función para eliminar la tarjeta
function deletedClass() {
  emit('deleted',{ id: props.id});
}

// Función para editar la tarjeta
function editeClass() {
  emit('edited',{ id: props.id});
}

</script>

<style scoped lang="scss">
</style>
