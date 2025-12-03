<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-100 py-12 px-4 sm:px-6 lg:px-8">
    <div class="w-full max-w-md space-y-8 bg-white p-8 rounded-lg shadow-lg">
      <div>
        <h2 class="text-center text-3xl font-bold text-gray-900">Crear Cuenta</h2>
        <p class="mt-2 text-center text-sm text-gray-600">Regístrate con tu correo y contraseña</p>
      </div>

      <form @submit.prevent="checkForm" class="space-y-6">
        <!-- Email -->
        <div>
          <label for="email" class="block text-sm font-medium text-gray-700">Correo</label>
          <input
            id="email"
            v-model="email"
            type="email"
            :class="['mt-1 block w-full px-4 py-2 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 outline-none transition', emailError ? 'border-red-500' : 'border-gray-300']"
            placeholder="tu@email.com"
          />
        </div>

        <!-- Password -->
        <div>
          <label for="password" class="block text-sm font-medium text-gray-700">Contraseña</label>
          <input
            id="password"
            v-model="password"
            type="password"
            :class="['mt-1 block w-full px-4 py-2 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 outline-none transition', passwordError ? 'border-red-500' : 'border-gray-300']"
            placeholder="••••••••"
          />
        </div>

        <!-- Confirm Password -->
        <div>
          <label for="confirm-password" class="block text-sm font-medium text-gray-700">Confirmar Contraseña</label>
          <input
            id="confirm-password"
            v-model="confirmPassword"
            type="password"
            :class="['mt-1 block w-full px-4 py-2 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 outline-none transition', confirmPasswordError ? 'border-red-500' : 'border-gray-300']"
            placeholder="••••••••"
          />
        </div>

        <!-- Submit Button -->
        <div>
          <button
            type="submit"
            class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition"
          >
            Registrar
          </button>
        </div>

        <!-- Mensajes -->
        <div v-if="errorMessage" class="p-4 bg-red-50 border border-red-200 rounded-md text-red-700 text-sm">
          {{ errorMessage }}
        </div>
        <div v-if="successMessage" class="p-4 bg-green-50 border border-green-200 rounded-md text-green-700 text-sm">
          {{ successMessage }}
        </div>

        <!-- Link a login -->
        <p class="text-sm text-center text-gray-600">
          ¿Ya tienes cuenta?
          <router-link to="/login" class="text-indigo-600 hover:text-indigo-700 font-medium">Inicia sesión</router-link>
        </p>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "RegisterView",
  
  // Datos reactivos
  data() {
    return {
      email: "",
      password: "",
      confirmPassword: "",
      emailError: false,
      passwordError: false,
      confirmPasswordError: false,
      errorMessage: "",
      successMessage: ""
    };
  },
  methods: {
    async checkForm() {
      // Reset errores
      this.emailError = false;
      this.passwordError = false;
      this.confirmPasswordError = false;
      this.errorMessage = "";
      this.successMessage = "";

      // Validación campos vacíos
      if (!this.email || !this.password || !this.confirmPassword) {
        if (!this.email) this.emailError = true;
        if (!this.password) this.passwordError = true;
        if (!this.confirmPassword) this.confirmPasswordError = true;

        this.errorMessage = (!this.email && !this.password && !this.confirmPassword)
          ? "Error: Todos los campos son obligatorios."
          : (!this.email ? "Error: El Email no puede estar vacío."
            : !this.password ? "Error: La Contraseña no puede estar vacía."
            : "Error: Debes confirmar la contraseña.");

        setTimeout(() => this.errorMessage = "", 3000);
        return;
      }

      // Validación contraseñas coinciden
      if (this.password !== this.confirmPassword) {
        this.passwordError = true;
        this.confirmPasswordError = true;
        this.errorMessage = "Error: Las contraseñas no coinciden.";
        setTimeout(() => this.errorMessage = "", 3000);
        return;
      }

      // Enviar datos al backend
      try {
        const res = await fetch("http://localhost:5000/api/register", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email: this.email, password: this.password })
        });

        const json = await res.json();

        // Manejar respuesta
        if (res.ok) {
          this.successMessage = json.message || "Registro correcto";
          setTimeout(() => this.successMessage = "", 3000);
        } else {
          this.errorMessage = json.error || json.message || "Error al registrar";
          setTimeout(() => this.errorMessage = "", 3000);
        }
      } catch (err) {
        this.errorMessage = "Error de conexión. Intenta de nuevo.";
        setTimeout(() => this.errorMessage = "", 3000);
      }
    }
  }
};
</script>

<style lang="scss" scoped></style>
