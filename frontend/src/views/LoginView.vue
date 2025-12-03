<template>
  <div
    class="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-100 py-12 px-4 sm:px-6 lg:px-8">
    <div class="w-full max-w-md space-y-8 bg-white p-8 rounded-lg shadow-lg">
      <div>
        <h2 class="text-center text-3xl font-bold text-gray-900">Iniciar Sesión</h2>
        <p class="mt-2 text-center text-sm text-gray-600">Ingresa tus credenciales</p>
      </div>

      <form @submit.prevent="checkForm" class="space-y-6">
        <div>
          <label for="email" class="block text-sm font-medium text-gray-700">Correo</label>
          <input id="email" v-model="email" type="email" name="email"
            :class="['mt-1 block w-full px-4 py-2 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 outline-none transition', emailError ? 'border-red-500' : 'border-gray-300']"
            placeholder="tu@email.com" />
        </div>

        <div>
          <label for="password" class="block text-sm font-medium text-gray-700">Contraseña</label>
          <input id="password" v-model="password" type="password" name="password"
            :class="['mt-1 block w-full px-4 py-2 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 outline-none transition', passwordError ? 'border-red-500' : 'border-gray-300']"
            placeholder="••••••••" />
        </div>

        <div>
          <button type="submit"
            class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition">
            Enviar
          </button>
        </div>

        <div v-if="errorMessage" class="p-4 bg-red-50 border border-red-200 rounded-md text-red-700 text-sm">
          {{ errorMessage }}
        </div>

        <div v-if="successMessage" class="p-4 bg-green-50 border border-green-200 rounded-md text-green-700 text-sm">
          {{ successMessage }}
        </div>
        <p class="text-sm text-center text-gray-600">
          ¿No tienes una cuenta?
          <router-link to="/register" class="text-indigo-600 hover:text-indigo-700 font-medium">Regístrate</router-link>
        </p>
      </form>
    </div>
  </div>
</template>

<script></script>

<style lang="scss" scoped></style>
<script>

export default {
  name: "HomeView",

  // Datos reactivos
  data() {
    return {
      email: "",
      password: "",
      emailError: false,
      passwordError: false,
      errorMessage:"",
      successMessage:"", 
    };
  },
  methods: {
    async checkForm() {
      
 // Resetear errores y mensajes
    this.emailError = false;
    this.passwordError = false;
    this.errorMessage = "";
    this.successMessage = "";

    // Validar campos
    if (!this.email || !this.password) {
      if (!this.email) this.emailError = true;
      if (!this.password) this.passwordError = true;

      this.errorMessage = (!this.email && !this.password)
        ? "Error: Todos los campos son obligatorios."
        : (!this.email ? "Error: El Email no puede estar vacío." : "Error: La Contraseña no puede estar vacía.");

      // Ocultar mensaje después de 3 segundos
      setTimeout(() => this.errorMessage = "", 3000);
      return;
    }

    // Enviar datos al backend
    try {
      const res = await fetch("http://localhost:5000/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email: this.email, password: this.password })
      });

      const json = await res.json();

      // Manejar respuesta
      if (res.ok) {
        this.successMessage = json.message || "Ingreso correcto";
        if (json.token) localStorage.setItem("token", json.token);

        // Navegar a home después de un breve retraso
          setTimeout(() => {
            this.successMessage = ""
            this.$router.push({name: 'home'});
          }, 500);
        
      } else {
        this.errorMessage = json.message || "Error al iniciar sesión";
        setTimeout(() => this.errorMessage = "", 3000);
      }
    } catch (err) {
      this.errorMessage = "Error de conexión. Intenta de nuevo.";
      setTimeout(() => this.errorMessage = "", 3000);
    }
  }
}
}
</script>