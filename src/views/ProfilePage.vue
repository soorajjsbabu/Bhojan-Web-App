<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { authStore } from '../stores/auth.js'
import { api } from '../api.js'
import { UserIcon, EnvelopeIcon, PencilSquareIcon } from '@heroicons/vue/24/outline'

const router = useRouter()

onMounted(() => {
  api.get('/userProfile')
    .then((response) => {
      authStore.profile.name = response.data.profile.name
      authStore.oldUser = true
    })
    .catch(() => {
      authStore.oldUser = false
    })
})
</script>

<template>
  <div class="relative flex min-h-[calc(100vh-4rem)] items-center justify-center p-4">
    <div class="absolute inset-0 bg-cover bg-center bg-no-repeat" style="background-image: url('/bg1.jpg');">
      <div class="absolute inset-0 bg-black/50" />
    </div>

    <div class="relative w-full max-w-md rounded-2xl bg-white p-8 shadow-2xl">
      <div class="mb-6 text-center">
        <div class="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-primary-100">
          <UserIcon class="h-8 w-8 text-primary-600" />
        </div>
        <h1 class="mt-4 text-2xl font-bold text-gray-900">Profile</h1>
      </div>

      <div class="space-y-4">
        <div class="flex items-center gap-3 rounded-lg bg-gray-50 px-4 py-3">
          <EnvelopeIcon class="h-5 w-5 text-gray-400" />
          <div>
            <p class="text-xs text-gray-500">Email</p>
            <p class="text-sm font-medium text-gray-900">{{ authStore.email }}</p>
          </div>
        </div>
        <div class="flex items-center gap-3 rounded-lg bg-gray-50 px-4 py-3">
          <UserIcon class="h-5 w-5 text-gray-400" />
          <div>
            <p class="text-xs text-gray-500">Name</p>
            <p class="text-sm font-medium text-gray-900">{{ authStore.profile.name || '—' }}</p>
          </div>
        </div>
      </div>

      <button
        @click="router.push('/profile-edit')"
        class="mt-6 flex w-full items-center justify-center gap-2 rounded-lg bg-primary-600 px-4 py-2.5 text-sm font-semibold text-white hover:bg-primary-700 transition-colors"
      >
        <PencilSquareIcon class="h-4 w-4" />
        Edit
      </button>
    </div>
  </div>
</template>
