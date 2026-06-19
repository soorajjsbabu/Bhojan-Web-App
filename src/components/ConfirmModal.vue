<script setup>
import { confirmState } from '../composables/useConfirm.js'
</script>

<template>
  <Teleport to="body">
    <Transition name="fade">
      <div v-if="confirmState.show" class="fixed inset-0 z-[90] flex items-center justify-center p-4">
        <div class="absolute inset-0 bg-black/40 backdrop-blur-sm" @click="confirmState.resolve(false)" />
        <div class="relative w-full max-w-sm rounded-xl bg-white p-6 shadow-2xl">
          <h3 class="text-lg font-semibold text-gray-900 mb-2">{{ confirmState.title }}</h3>
          <p class="text-gray-600 mb-6" v-html="confirmState.message" />
          <div class="flex justify-end gap-3">
            <button
              @click="confirmState.resolve(false)"
              class="rounded-lg px-4 py-2 text-sm font-medium text-gray-700 bg-gray-100 hover:bg-gray-200 transition-colors"
            >
              Cancel
            </button>
            <button
              @click="confirmState.resolve(true)"
              class="rounded-lg px-4 py-2 text-sm font-medium text-white bg-rose-600 hover:bg-rose-700 transition-colors"
            >
              Delete
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
