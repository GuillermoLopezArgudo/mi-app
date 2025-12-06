<template>
    <div class="w-full bg-white p-6 rounded shadow">

        <!-- Header -->
        <div class="grid grid-cols-3 gap-4 mb-6">
            <div>
                <p class="font-semibold">Evaluación</p>
                <p class="text-sm text-gray-600">Grupo</p>
                <p class="text-sm text-gray-600">Tutor/a</p>
            </div>
            <div></div>
            <div>
                <p class="font-semibold text-right">Observaciones</p>
            </div>
        </div>

        <!-- Grid Container -->
        <div class="grid grid-cols-2 gap-6">

            <!-- Left Table -->
            <table class="w-full border-collapse border border-gray-300 text-sm">
                <thead class="h-12">
                    <tr>
                        <th class="border border-gray-300 w-10 text-center">#</th>
                        <th class="border border-gray-300 w-36">Nombre y apellidos</th>
                        <th v-for="n in 20" :key="n" class="border border-gray-300 w-8"></th>
                    </tr>
                </thead>

                <tbody>
                    <tr v-for="i in 40" :key="i">
                        <td class="border border-gray-300 text-center">{{ i }}</td>
                        <td class="border border-gray-300 w-36"></td>
                        <td v-for="n in 20" :key="n" class="border border-gray-200"></td>
                    </tr>
                </tbody>
            </table>

            <!-- Right Table -->
            <table class="w-full border-collapse border border-gray-300 text-sm">
                <thead class="h-12">
                    <tr>
                        <th class="border border-gray-300 w-10 text-center">#</th>
                        <th v-for="n in 20" :key="n" class="border border-gray-300 w-8"></th>
                        <th class="border border-gray-300 w-36">Observaciones</th>
                    </tr>
                </thead>

                <tbody>
                    <tr v-for="i in 40" :key="i">
                        <td class="border border-gray-300 text-center">{{ i }}</td>
                        <td v-for="n in 20" :key="n" class="border border-gray-200"></td>
                        <td class="border border-gray-300"></td>
                    </tr>
                </tbody>
            </table>

        </div>
    </div>
</template>

<script setup>
</script>
