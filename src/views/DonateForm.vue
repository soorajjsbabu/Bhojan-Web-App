<script setup>
import { reactive, computed } from 'vue'
import { api } from '../api.js'
import { useToast } from '../composables/useToast.js'

const emit = defineEmits(['submitted', 'cancel'])
const { success } = useToast()

const form = reactive({
  name: '',
  phoneNumber: '',
  addLine1: '',
  addLine2: '',
  servedFor: '',
  foodTypeVeg: false,
  foodTypeNonVeg: false,
})

const foodType = computed(() => {
  if (form.foodTypeVeg && form.foodTypeNonVeg) return 'Both'
  if (form.foodTypeNonVeg) return 'Non Veg'
  if (form.foodTypeVeg) return 'Veg'
  return ''
})

function postNow() {
  api.post('/add_donation', {
    name: form.name,
    phoneNumber: form.phoneNumber,
    addLine1: form.addLine1,
    addLine2: form.addLine2,
    servedFor: form.servedFor,
    foodType: foodType.value,
  })
  success("Form submitted! You've made someone happy :)")
  emit('submitted')
}
</script>

<template>
  <div class="rounded-2xl bg-white p-6 sm:p-8 shadow-xl">
    <h2 class="text-2xl font-bold text-gray-900 mb-6">Donate here!</h2>
    <form @submit.prevent="postNow" class="space-y-4">
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Name</label>
        <input
          v-model="form.name"
          type="text"
          required
          class="w-full rounded-lg border border-gray-300 px-4 py-2 text-sm focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all"
        />
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Contact Phone</label>
        <input
          v-model="form.phoneNumber"
          type="tel"
          required
          placeholder="For pickup coordination"
          class="w-full rounded-lg border border-gray-300 px-4 py-2 text-sm focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all"
        />
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Address Line 1</label>
        <input
          v-model="form.addLine1"
          type="text"
          required
          class="w-full rounded-lg border border-gray-300 px-4 py-2 text-sm focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all"
        />
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Address Line 2</label>
        <input
          v-model="form.addLine2"
          type="text"
          required
          class="w-full rounded-lg border border-gray-300 px-4 py-2 text-sm focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all"
        />
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Served For (no. of people)</label>
        <input
          v-model="form.servedFor"
          type="number"
          required
          class="w-full rounded-lg border border-gray-300 px-4 py-2 text-sm focus:border-primary-500 focus:ring-2 focus:ring-primary-200 outline-none transition-all"
        />
      </div>
      <div class="flex items-center gap-6 pt-1">
        <label class="flex items-center gap-2 text-sm text-gray-700 cursor-pointer">
          <input v-model="form.foodTypeVeg" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-primary-600 focus:ring-primary-500" />
          Veg
        </label>
        <label class="flex items-center gap-2 text-sm text-gray-700 cursor-pointer">
          <input v-model="form.foodTypeNonVeg" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-primary-600 focus:ring-primary-500" />
          Non Veg
        </label>
      </div>
      <div class="flex items-center gap-3 pt-2">
        <button
          type="submit"
          class="rounded-lg bg-primary-600 px-5 py-2.5 text-sm font-semibold text-white hover:bg-primary-700 transition-colors"
        >
          Submit
        </button>
        <button
          type="button"
          @click="emit('cancel')"
          class="rounded-lg border border-gray-300 px-5 py-2.5 text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors"
        >
          Cancel
        </button>
      </div>
    </form>
  </div>
</template>
