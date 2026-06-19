<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { authStore } from './stores/auth.js'
import NavBar from './components/NavBar.vue'
import SideBar from './components/SideBar.vue'
import Footer from './components/Footer.vue'
import ToastContainer from './components/ToastContainer.vue'
import AlertModal from './components/AlertModal.vue'
import ConfirmModal from './components/ConfirmModal.vue'

const route = useRoute()
const router = useRouter()
const sidebarOpen = ref(false)

const showFooter = computed(() => {
  const hiddenRoutes = ['/login', '/signup']
  if (hiddenRoutes.includes(route.path)) return false
  return authStore.showFooter
})

// authStore.init() already ran in main.js before mount, so state is ready
onMounted(() => {
  if (authStore.isAdmin) {
    router.replace('/admin')
  }
})
</script>

<template>
  <div class="flex min-h-screen flex-col bg-gray-50">
    <NavBar @toggle-sidebar="sidebarOpen = true" />
    <SideBar v-model="sidebarOpen" />

    <main class="flex-1">
      <RouterView v-slot="{ Component }">
        <Transition name="page" mode="out-in">
          <component :is="Component" :key="route.path" />
        </Transition>
      </RouterView>
    </main>

    <Footer v-if="showFooter" />

    <ToastContainer />
    <AlertModal />
    <ConfirmModal />
  </div>
</template>

<style>
.page-enter-active,
.page-leave-active {
  transition: opacity 0.2s ease, transform 0.2s ease;
}
.page-enter-from {
  opacity: 0;
  transform: translateY(6px);
}
.page-leave-to {
  opacity: 0;
  transform: translateY(-6px);
}
</style>
