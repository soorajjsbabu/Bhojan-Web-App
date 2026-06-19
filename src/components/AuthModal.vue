<script setup>
import { ref } from 'vue'
import { signInWithEmailAndPassword, createUserWithEmailAndPassword } from 'firebase/auth'
import { auth } from '../firebase.js'
import { useAlert } from '../composables/useAlert.js'
import {
  XMarkIcon,
  ArrowRightOnRectangleIcon,
  UserPlusIcon,
} from '@heroicons/vue/24/outline'

const emit = defineEmits(['close', 'success'])
const { alert } = useAlert()

const ADMIN_EMAIL = import.meta.env.VITE_ADMIN_EMAIL || ''

const tab = ref('login')
const email = ref('')
const password = ref('')
const passCheck = ref('')
const loading = ref(false)

function switchTab(t) {
  tab.value = t
  password.value = ''
  passCheck.value = ''
}

async function login() {
  if (!email.value || !password.value) { alert('Fill in all fields.', 'error'); return }
  loading.value = true
  try {
    const cred = await signInWithEmailAndPassword(auth, email.value, password.value)
    emit('success', { isAdmin: !!ADMIN_EMAIL && cred.user.email === ADMIN_EMAIL })
  } catch (err) {
    alert(friendlyError(err.code), 'error')
  } finally {
    loading.value = false
  }
}

async function signup() {
  if (!email.value || !password.value || !passCheck.value) { alert('Fill in all fields.', 'error'); return }
  if (password.value !== passCheck.value) { alert('Passwords do not match.', 'error'); return }
  loading.value = true
  try {
    const cred = await createUserWithEmailAndPassword(auth, email.value, password.value)
    emit('success', { isAdmin: !!ADMIN_EMAIL && cred.user.email === ADMIN_EMAIL })
  } catch (err) {
    alert(friendlyError(err.code), 'error')
  } finally {
    loading.value = false
  }
}

function friendlyError(code) {
  const map = {
    'auth/user-not-found': 'No account found with this email.',
    'auth/invalid-credential': 'Incorrect email or password.',
    'auth/wrong-password': 'Incorrect password.',
    'auth/email-already-in-use': 'Email is already registered.',
    'auth/weak-password': 'Password must be at least 6 characters.',
    'auth/invalid-email': 'Invalid email address.',
  }
  return map[code] || 'Something went wrong. Please try again.'
}
</script>

<template>
  <Teleport to="body">
    <Transition name="fade">
      <div class="fixed inset-0 z-[80] flex items-center justify-center p-4">
        <div class="absolute inset-0 bg-black/50 backdrop-blur-sm" @click="emit('close')" />

        <div class="relative w-full max-w-md rounded-2xl bg-white shadow-2xl overflow-hidden">
          <!-- Tab header -->
          <div class="flex border-b border-gray-100">
            <button
              @click="switchTab('login')"
              class="flex-1 py-4 text-sm font-semibold transition-colors"
              :class="tab === 'login' ? 'text-primary-600 border-b-2 border-primary-600' : 'text-gray-500 hover:text-gray-700'"
            >
              Log in
            </button>
            <button
              @click="switchTab('signup')"
              class="flex-1 py-4 text-sm font-semibold transition-colors"
              :class="tab === 'signup' ? 'text-primary-600 border-b-2 border-primary-600' : 'text-gray-500 hover:text-gray-700'"
            >
              Sign up
            </button>
            <button @click="emit('close')" class="px-4 text-gray-400 hover:text-gray-600 transition-colors">
              <XMarkIcon class="h-5 w-5" />
            </button>
          </div>

          <div class="p-8">
            <!-- Login tab -->
            <template v-if="tab === 'login'">
              <p class="mb-6 text-sm text-gray-500">Welcome back! Log in to submit your donation.</p>
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
                    class="w-full rounded-lg border border-gray-300 px-4 py-2 text-sm focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all"
                  />
                </div>
                <button
                  type="submit"
                  :disabled="loading"
                  class="flex w-full items-center justify-center gap-2 rounded-lg bg-primary-600 px-4 py-2.5 text-sm font-semibold text-white hover:bg-primary-700 transition-colors disabled:opacity-60"
                >
                  <ArrowRightOnRectangleIcon class="h-4 w-4" />
                  {{ loading ? 'Logging in…' : 'Log in & Donate' }}
                </button>
              </form>
            </template>

            <!-- Signup tab -->
            <template v-else>
              <p class="mb-6 text-sm text-gray-500">Create a free account to start donating and track your history.</p>
              <form @submit.prevent="signup" class="space-y-4">
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
                    class="w-full rounded-lg border border-gray-300 px-4 py-2 text-sm focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all"
                  />
                </div>
                <button
                  type="submit"
                  :disabled="loading"
                  class="flex w-full items-center justify-center gap-2 rounded-lg bg-primary-600 px-4 py-2.5 text-sm font-semibold text-white hover:bg-primary-700 transition-colors disabled:opacity-60"
                >
                  <UserPlusIcon class="h-4 w-4" />
                  {{ loading ? 'Creating account…' : 'Create account & Donate' }}
                </button>
              </form>
            </template>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active { transition: opacity 0.2s ease; }
.fade-enter-from,
.fade-leave-to { opacity: 0; }
</style>
