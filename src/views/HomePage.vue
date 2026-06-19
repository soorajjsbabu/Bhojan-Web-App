<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { authStore } from '../stores/auth.js'
import DonateForm from './DonateForm.vue'
import AuthModal from '../components/AuthModal.vue'
import { HeartIcon } from '@heroicons/vue/24/solid'

const router = useRouter()
const showForm = ref(false)
const showAuthModal = ref(false)

function donate() {
  if (authStore.signedIn) {
    showForm.value = !showForm.value
  } else {
    showAuthModal.value = true
  }
}

function onAuthSuccess({ isAdmin }) {
  showAuthModal.value = false
  if (isAdmin) {
    router.push('/admin')
  } else {
    showForm.value = true
  }
}
</script>

<template>
  <div class="relative min-h-[calc(100vh-4rem)]">
    <div
      class="absolute inset-0 bg-cover bg-center bg-no-repeat"
      style="background-image: url('/bg1.jpg');"
    >
      <div class="absolute inset-0 bg-black/50" />
    </div>

    <div class="relative mx-auto max-w-7xl px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
      <div class="grid gap-12 lg:grid-cols-2 lg:items-center">
        <div class="space-y-6">
          <div class="inline-flex items-center gap-2 rounded-full bg-white/10 px-3 py-1 text-sm font-medium text-white backdrop-blur-sm">
            <HeartIcon class="h-4 w-4 text-rose-400" />
            Make a difference today
          </div>
          <h1 class="text-4xl font-bold tracking-tight text-white sm:text-5xl lg:text-6xl">
            Donate Food to<br>
            <span class="text-primary-400">help feed the hungry</span>
          </h1>
          <p class="text-lg text-gray-200 max-w-lg">
            Any contribution you make today will build a better future for someone.
          </p>
          <button
            @click="donate"
            class="inline-flex items-center gap-2 rounded-xl bg-primary-600 px-6 py-3 text-base font-semibold text-white shadow-lg hover:bg-primary-700 transition-all hover:shadow-xl active:scale-95"
          >
            {{ showForm ? 'Cancel' : 'Donate' }}
          </button>
        </div>

        <div class="flex flex-col justify-center">
          <div
            v-if="!showForm"
            class="rounded-2xl bg-white/10 p-8 backdrop-blur-md border border-white/10"
          >
            <blockquote class="text-xl font-medium text-white italic">
              "If you can't feed hundred people, then feed just one."
            </blockquote>
            <p class="mt-4 text-primary-300 font-semibold">— Mother Teresa</p>
          </div>

          <DonateForm
            v-else
            @submitted="showForm = false"
            @cancel="showForm = false"
          />
        </div>
      </div>
    </div>
  </div>

  <AuthModal
    v-if="showAuthModal"
    @close="showAuthModal = false"
    @success="onAuthSuccess"
  />
</template>
