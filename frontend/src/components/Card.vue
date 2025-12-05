<template>
  <div class="bg-white rounded-xl shadow-md overflow-hidden hover:shadow-lg transition cursor-pointer" @click="handleClick">
    <img
      class="w-full h-48 object-cover"
      :src="image"
      :alt="title"
    />
    <div class="p-4">
      <h2 class="text-xl font-bold mb-1">{{title}}</h2>
      <p class="text-gray-700 text-sm mb-3">
        {{ description }}
      </p>
    </div>
  </div>
</template>


<script setup>
import { useRouter } from 'vue-router';
import { defineProps } from 'vue';

//  Definición de las props del componente
const props = defineProps({
  title: { type: String, required: true },
  description: { type: String, required: true },
  image: { type: String, default: "" },
  link: { type: String, default: null }
})

const router = useRouter();

// Manejar el clic en la tarjeta
function handleClick() {
  if (props.link && props.link !== "#") {
    router.push(props.link);
  }
}

</script>

<style scoped lang="scss">
</style>
