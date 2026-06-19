<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { authStore } from '../stores/auth.js'
import { api } from '../api.js'
import { useToast } from '../composables/useToast.js'
import { UserIcon, CheckIcon, XMarkIcon } from '@heroicons/vue/24/outline'

const router = useRouter()
const { success } = useToast()

const name = ref('')

onMounted(() => {
  name.value = authStore.profile.name
})

function save() {
  authStore.profile.name = name.value

  if (authStore.oldUser) {
    api.put('/update_user', { name: name.value })
  } else {
    api.post('/add_user_profile', { name: name.value })
    authStore.oldUser = true
  }

  success('Profile updated')
  router.push('/profile')
}
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
        <h1 class="mt-4 text-2xl font-bold text-gray-900">Edit Profile</h1>
      </div>

      <form @submit.prevent="save" class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Email</label>
          <div class="rounded-lg bg-gray-100 px-4 py-2.5 text-sm text-gray-500">
            {{ authStore.email }}
          </div>
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Name</label>
          <input
            v-model="name"
            type="text"
            required
            class="w-full rounded-lg border border-gray-300 px-4 py-2 text-sm focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all"
          />
        </div>
        <div class="flex items-center gap-3 pt-2">
          <button
            type="submit"
            class="flex items-center gap-2 rounded-lg bg-primary-600 px-5 py-2.5 text-sm font-semibold text-white hover:bg-primary-700 transition-colors"
          >
            <CheckIcon class="h-4 w-4" />
            Save
          </button>
          <button
            type="button"
            @click="router.push('/profile')"
            class="flex items-center gap-2 rounded-lg border border-gray-300 px-5 py-2.5 text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors"
          >
            <XMarkIcon class="h-4 w-4" />
            Cancel
          </button>
        </div>
      </form>
    </div>
  </div>
</template>
