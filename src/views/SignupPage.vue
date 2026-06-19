<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { createUserWithEmailAndPassword } from 'firebase/auth'
import { auth } from '../firebase.js'
import { useToast } from '../composables/useToast.js'
import { useAlert } from '../composables/useAlert.js'
import { UserPlusIcon } from '@heroicons/vue/24/outline'

const router = useRouter()
const { success } = useToast()
const { alert } = useAlert()

const email = ref('')
const password = ref('')
const passCheck = ref('')

async function register() {
  if (!email.value) { alert('Enter your email.', 'error'); return }
  if (!password.value || !passCheck.value) { alert('Enter your password.', 'error'); return }
  if (password.value !== passCheck.value) { alert('Passwords do not match.', 'error'); return }

  try {
    await createUserWithEmailAndPassword(auth, email.value, password.value)
    success('Account created! You can now donate.')
    router.push('/')
  } catch (err) {
    const map = {
      'auth/email-already-in-use': 'Email is already registered.',
      'auth/weak-password': 'Password must be at least 6 characters.',
      'auth/invalid-email': 'Invalid email address.',
    }
    alert(map[err.code] || 'Signup failed.', 'error')
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
        <h1 class="text-2xl font-bold text-gray-900">Create account</h1>
        <p class="mt-1 text-sm text-gray-500">Sign up to start donating and track your history.</p>
      </div>

      <form @submit.prevent="register" class="space-y-4">
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
            placeholder="Min. 6 characters"
            required
            class="w-full rounded-lg border border-gray-300 px-4 py-2 text-sm focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all"
          />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Confirm Password</label>
          <input
            v-model="passCheck"
            type="password"
            placeholder="Re-enter password"
            required
            @keyup.enter="register"
            class="w-full rounded-lg border border-gray-300 px-4 py-2 text-sm focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all"
          />
        </div>
        <button
          type="submit"
          class="flex w-full items-center justify-center gap-2 rounded-lg bg-primary-600 px-4 py-2.5 text-sm font-semibold text-white hover:bg-primary-700 transition-colors"
        >
          <UserPlusIcon class="h-4 w-4" />
          Create account
        </button>
      </form>

      <p class="mt-4 text-center text-sm text-gray-500">
        Already have an account?
        <RouterLink to="/login" class="font-medium text-primary-600 hover:text-primary-700">Log in</RouterLink>
      </p>
    </div>
  </div>
</template>
