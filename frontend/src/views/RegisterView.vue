<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-100 py-12 px-4 sm:px-6 lg:px-8">
    <div class="w-full max-w-md space-y-8 bg-white p-8 rounded-lg shadow-lg">
      <div>
        <h2 class="text-center text-3xl font-bold text-gray-900">Crear Cuenta</h2>
        <p class="mt-2 text-center text-sm text-gray-600">Regístrate con tu correo y contraseña</p>
      </div>

      <form id="app" @submit="checkForm" action="" method="post" class="space-y-6">
        <div>
          <label for="email" class="block text-sm font-medium text-gray-700">Correo</label>
          <input 
            id="email" 
            v-model="email" 
            type="email" 
            name="email"
            class="mt-1 block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 outline-none transition"
            placeholder="tu@email.com"
          />
        </div>

        <div>
          <label for="password" class="block text-sm font-medium text-gray-700">Contraseña</label>
          <input 
            id="password" 
            v-model="password" 
            type="password"
            name="password"
            class="mt-1 block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 outline-none transition"
            placeholder="••••••••"
          />
        </div>

          <div>
            <label for="confirm-password" class="block text-sm font-medium text-gray-700">Confirmar Contraseña</label>
            <input 
              id="confirm-password" 
              v-model="confirmPassword" 
              type="password"
              name="confirmPassword"
              class="mt-1 block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 outline-none transition"
              placeholder="••••••••"
            />
          </div>

        <div>
          <button
            type="submit"
            class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition"
          >
            Registrar
          </button>
        </div>

        <div
          id="error-message"
          hidden
          class="p-4 bg-red-50 border border-red-200 rounded-md text-red-700 text-sm"
        ></div>
        <p class="text-sm text-center text-gray-600">
          ¿Ya tienes cuenta?
          <router-link to="/login" class="text-indigo-600 hover:text-indigo-700 font-medium">Inicia sesión</router-link>
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
  data() {
    return {
      email: "",
      password: "",
      confirmPassword: "",
    };
  },
  methods: {
    async checkForm(e) {
      e.preventDefault();

      //Componentes para mostrar mensajes de error o exito
      const aEl = document.getElementById("error-message");

      // Comprobar que los campos no esten vacios
      if (this.email === "" || this.password === "" || this.confirmPassword === "") {
        aEl.className = 'p-4 bg-red-50 border border-red-200 rounded-md text-red-700 text-sm';
        aEl.removeAttribute("hidden");
        if (this.email === "" && this.password === "" && this.confirmPassword === "") {
          document.getElementById("email").style.borderColor = "red";
          document.getElementById("password").style.borderColor = "red";
          document.getElementById("confirm-password").style.borderColor = "red";
          aEl.innerText = "Error: Todos los campos son obligatorios.";
        } else if (this.email === "") {
          document.getElementById("email").style.borderColor = "red";
          aEl.innerText = "Error: El Email no puede estar vacio.";
        } else if (this.password === "") {
          document.getElementById("password").style.borderColor = "red";
          aEl.innerText = "Error: La Contraseña no puede estar vacia.";
        } else {
          document.getElementById("confirm-password").style.borderColor = "red";
          aEl.innerText = "Error: Debes confirmar la contraseña.";
        }

        //Tiempo para ocultar el mensaje de error y resetear los bordes
        setTimeout(() => {
          aEl.setAttribute("hidden", "hidden");
          document.getElementById("email").style.borderColor = "#d1d5db";
          document.getElementById("password").style.borderColor = "#d1d5db";
          const cp = document.getElementById("confirm-password");
          if (cp) cp.style.borderColor = "#d1d5db";
        }, 3000);

        return;
      }

      // Comprobar que las contraseñas coincidan
      if (this.password !== this.confirmPassword) {
        aEl.className = 'p-4 bg-red-50 border border-red-200 rounded-md text-red-700 text-sm';
        aEl.removeAttribute("hidden");
        aEl.innerText = "Error: Las contraseñas no coinciden.";
        document.getElementById("password").style.borderColor = "red";
        document.getElementById("confirm-password").style.borderColor = "red";

        //Tiempo para ocultar el mensaje de error y resetear los bordes
        setTimeout(() => {
          aEl.setAttribute("hidden", "hidden");
          document.getElementById("password").style.borderColor = "#d1d5db";
          document.getElementById("confirm-password").style.borderColor = "#d1d5db";
        }, 3000);

        return;
      }

      //Enviar datos al backend para registrar usuario
      try {
        const res = await fetch("http://localhost:5000/api/register", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email: this.email, password: this.password }),
        });

        const json = await res.json();

        //Mostrar mensaje de exito o error segun la respuesta del backend
        if (res.ok) {
          aEl.className = 'p-4 bg-green-50 border border-green-200 rounded-md text-green-700 text-sm';
          aEl.removeAttribute("hidden");
          aEl.innerText = json.message || "Registro correcto";
        } else {
          aEl.className = 'p-4 bg-red-50 border border-red-200 rounded-md text-red-700 text-sm';
          aEl.removeAttribute("hidden");
          aEl.innerText = json.error || json.message || "Error al registrar";
        }
      } catch (err) {
        aEl.className = 'p-4 bg-red-50 border border-red-200 rounded-md text-red-700 text-sm';
        aEl.removeAttribute("hidden");
        aEl.innerText = "Error de conexión. Intenta de nuevo.";
      }

      //Ocultar mensaje despues de 3 segundos
      setTimeout(() => {
        const a = document.getElementById("error-message");
        if (a) a.setAttribute("hidden", "hidden");
      }, 3000);
    },
  },
};

</script>