<script setup>
import { alertState } from '../composables/useAlert.js'
</script>

<template>
  <Teleport to="body">
    <Transition name="fade">
      <div v-if="alertState.show" class="fixed inset-0 z-[90] flex items-center justify-center p-4">
        <div class="absolute inset-0 bg-black/40 backdrop-blur-sm" @click="alertState.resolve()" />
        <div class="relative w-full max-w-sm rounded-xl bg-white p-6 shadow-2xl">
          <h3 class="text-lg font-semibold text-gray-900 mb-2">Notice</h3>
          <p class="text-gray-600 mb-6">{{ alertState.message }}</p>
          <div class="flex justify-end">
            <button
              @click="alertState.resolve()"
              class="rounded-lg px-4 py-2 text-sm font-medium text-white"
              :class="alertState.type === 'error' ? 'bg-rose-600 hover:bg-rose-700' : 'bg-gray-900 hover:bg-gray-800'"
            >
              OK
            </button>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
