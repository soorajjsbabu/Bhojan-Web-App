<script setup>
import { authStore } from '../stores/auth.js'
import { useRouter } from 'vue-router'
import {
  Bars3Icon,
  HomeIcon,
  ArrowRightOnRectangleIcon,
  ArrowLeftOnRectangleIcon,
  UserPlusIcon,
} from '@heroicons/vue/24/outline'

const emit = defineEmits(['toggle-sidebar'])
const router = useRouter()

function signOut() {
  authStore.signOut()
  router.push('/')
}
</script>

<template>
  <nav class="sticky top-0 z-50 bg-gray-900 text-white shadow-md">
    <div class="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
      <div class="flex items-center gap-4">
        <button
          v-if="authStore.signedIn && !authStore.isAdmin"
          @click="emit('toggle-sidebar')"
          class="rounded-lg p-2 hover:bg-gray-800 transition-colors"
          aria-label="Open menu"
        >
          <Bars3Icon class="h-6 w-6" />
        </button>
        <button
          v-if="!authStore.isAdmin"
          @click="router.push('/')"
          class="flex items-center gap-2 rounded-lg px-3 py-2 text-sm font-medium hover:bg-gray-800 transition-colors"
        >
          <HomeIcon class="h-5 w-5" />
          <span class="hidden sm:inline">Home</span>
        </button>
      </div>

      <div class="flex items-center gap-2">
        <template v-if="!authStore.signedIn">
          <button
            @click="router.push('/signup')"
            class="flex items-center gap-1.5 rounded-lg bg-primary-600 px-4 py-2 text-sm font-semibold hover:bg-primary-700 transition-colors"
          >
            <UserPlusIcon class="h-4 w-4" />
            Sign up
          </button>
          <button
            @click="router.push('/login')"
            class="flex items-center gap-1.5 rounded-lg border border-gray-600 px-4 py-2 text-sm font-medium hover:bg-gray-800 transition-colors"
          >
            <ArrowRightOnRectangleIcon class="h-4 w-4" />
            Log in
          </button>
        </template>
        <template v-else>
          <button
            @click="signOut"
            class="flex items-center gap-1.5 rounded-lg bg-primary-600 px-4 py-2 text-sm font-semibold hover:bg-primary-700 transition-colors"
          >
            <ArrowLeftOnRectangleIcon class="h-4 w-4" />
            Sign Out
          </button>
        </template>
      </div>
    </div>
  </nav>
</template>
