<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { signInWithEmailAndPassword } from 'firebase/auth'
import { auth } from '../firebase.js'
import { useAlert } from '../composables/useAlert.js'
import { ArrowRightOnRectangleIcon } from '@heroicons/vue/24/outline'

const router = useRouter()
const { alert } = useAlert()

const ADMIN_EMAIL = import.meta.env.VITE_ADMIN_EMAIL || ''

const email = ref('')
const password = ref('')

async function login() {
  if (!email.value) { alert('Enter your email.', 'error'); return }
  if (!password.value) { alert('Enter your password.', 'error'); return }

  try {
    const cred = await signInWithEmailAndPassword(auth, email.value, password.value)
    if (ADMIN_EMAIL && cred.user.email === ADMIN_EMAIL) {
      router.push('/admin')
    } else {
      router.push('/')
    }
  } catch (err) {
    const map = {
      'auth/user-not-found': 'No account found with this email.',
      'auth/invalid-credential': 'Incorrect email or password.',
      'auth/wrong-password': 'Incorrect password.',
      'auth/invalid-email': 'Invalid email address.',
    }
    alert(map[err.code] || 'Login failed.', 'error')
  }
}
</script>

<template>
  <div class="relative flex min-h-[calc(100vh-4rem)] items-center justify-center p-4">
    <div class="absolute inset-0 bg-cover bg-center bg-no-repeat" style="background-image: url('/bg1.jpg');">
      <div class="absolute inset-0 bg-black/50" />
    </div>

    <div class="relative w-full max-w-md rounded-2xl bg-white p-8 shadow-2xl">
      <div class="mb-6 text-center">
        <h1 class="text-2xl font-bold text-gray-900">Log in</h1>
        <p class="mt-1 text-sm text-gray-500">Welcome back! Sign in to continue.</p>
      </div>

      <form @submit.prevent="login" class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Email</label>
          <input
            v-model="email"
            type="email"
            placeholder="you@example.com"
            required
            class="w-full rounded-lg border border-gray-300 px-4 py-2 text-sm focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all"
          />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Password</label>
          <input
            v-model="password"
            type="password"
            placeholder="Your password"
            required
            @keyup.enter="login"
            class="w-full rounded-lg border border-gray-300 px-4 py-2 text-sm focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all"
          />
        </div>
        <button
          type="submit"
          class="flex w-full items-center justify-center gap-2 rounded-lg bg-primary-600 px-4 py-2.5 text-sm font-semibold text-white hover:bg-primary-700 transition-colors"
        >
          <ArrowRightOnRectangleIcon class="h-4 w-4" />
          Log in
        </button>
      </form>

      <p class="mt-4 text-center text-sm text-gray-500">
        Don't have an account?
        <RouterLink to="/signup" class="font-medium text-primary-600 hover:text-primary-700">Sign up</RouterLink>
      </p>
    </div>
  </div>
</template>
