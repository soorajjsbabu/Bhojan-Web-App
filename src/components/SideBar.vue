<script setup>
import { ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import { authStore } from '../stores/auth.js'
import {
  XMarkIcon,
  GiftIcon,
  InformationCircleIcon,
} from '@heroicons/vue/24/outline'

const props = defineProps({
  modelValue: Boolean,
})
const emit = defineEmits(['update:modelValue'])

const router = useRouter()
const open = ref(props.modelValue)

watch(() => props.modelValue, (val) => {
  open.value = val
})

watch(open, (val) => {
  emit('update:modelValue', val)
})

function goToHistory() {
  open.value = false
  router.push('/history')
}
</script>

<template>
  <Teleport to="body">
    <Transition name="sidebar">
      <div v-if="open" class="fixed inset-0 z-[60]">
        <div class="absolute inset-0 bg-black/40 backdrop-blur-sm" @click="open = false" />
        <div class="absolute left-0 top-0 h-full w-72 bg-white shadow-2xl">
          <div class="flex items-center justify-between border-b border-gray-100 px-6 py-4">
            <h2 class="text-xl font-bold text-gray-900">Food<br>Donation</h2>
            <button @click="open = false" class="rounded-lg p-2 hover:bg-gray-100 transition-colors">
              <XMarkIcon class="h-5 w-5 text-gray-500" />
            </button>
          </div>
          <nav class="p-4 space-y-1">
            <button
              @click="goToHistory"
              class="flex w-full items-center gap-3 rounded-lg px-4 py-3 text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors"
            >
              <GiftIcon class="h-5 w-5 text-gray-400" />
              Your Donations
            </button>
            <button
              class="flex w-full items-center gap-3 rounded-lg px-4 py-3 text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors"
            >
              <InformationCircleIcon class="h-5 w-5 text-gray-400" />
              About
            </button>
          </nav>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<style scoped>
.sidebar-enter-active,
.sidebar-leave-active {
  transition: opacity 0.25s ease;
}
.sidebar-enter-from,
.sidebar-leave-to {
  opacity: 0;
}
.sidebar-enter-active > div:last-child,
.sidebar-leave-active > div:last-child {
  transition: transform 0.25s ease;
}
.sidebar-enter-from > div:last-child,
.sidebar-leave-to > div:last-child {
  transform: translateX(-100%);
}
</style>
