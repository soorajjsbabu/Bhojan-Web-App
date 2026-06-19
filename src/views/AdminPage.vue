<script setup>
import { ref, computed, watch } from 'vue'
import { api } from '../api.js'
import { authStore } from '../stores/auth.js'
import { ArrowUpIcon, ArrowDownIcon, TableCellsIcon } from '@heroicons/vue/24/solid'

const donationDetails = ref([])
const sortKey = ref('')
const sortOrder = ref('asc')
const loading = ref(false)

const donationColumns = [
  { key: 'name', label: 'Name' },
  { key: 'phoneNumber', label: 'Contact Phone' },
  { key: 'addLine1', label: 'Address Line 1' },
  { key: 'addLine2', label: 'Address Line 2' },
  { key: 'servedFor', label: 'Served For' },
  { key: 'foodType', label: 'Food Type' },
  { key: 'dateTime', label: 'Date/Time' },
  { key: 'userEmail', label: 'Donor Email' },
]

// Load when admin status is confirmed (handles first-login timing and page refresh)
watch(() => authStore.isAdmin, (isAdmin) => {
  if (isAdmin) loadDonations()
}, { immediate: true })

function loadDonations() {
  loading.value = true
  api.get('/donations')
    .then((r) => {
      donationDetails.value = r.data.donations.map((d) => ({
        ...d,
        dateTime: new Date(d.dateTime).toLocaleString(),
      }))
    })
    .finally(() => { loading.value = false })
}

function toggleSort(key) {
  if (sortKey.value === key) {
    sortOrder.value = sortOrder.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortKey.value = key
    sortOrder.value = 'asc'
  }
}

const sortedDonations = computed(() => {
  if (!sortKey.value) return donationDetails.value
  const key = sortKey.value
  const order = sortOrder.value === 'asc' ? 1 : -1
  return [...donationDetails.value].sort((a, b) =>
    a[key] < b[key] ? -order : a[key] > b[key] ? order : 0
  )
})
</script>

<template>
  <div class="mx-auto max-w-7xl px-4 py-10 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between mb-8">
      <h1 class="text-3xl font-bold text-gray-900">Admin</h1>
      <button
        @click="loadDonations"
        class="inline-flex items-center gap-2 rounded-lg border border-gray-300 px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 transition-colors"
      >
        <TableCellsIcon class="h-4 w-4" />
        Refresh
      </button>
    </div>

    <div class="overflow-hidden rounded-xl border border-gray-200 bg-white shadow-sm">
      <div v-if="loading" class="px-6 py-12 text-center text-sm text-gray-400">
        Loading donations…
      </div>
      <div v-else class="overflow-x-auto">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th
                v-for="col in donationColumns"
                :key="col.key"
                @click="toggleSort(col.key)"
                class="cursor-pointer px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500 hover:bg-gray-100 transition-colors select-none"
              >
                <div class="flex items-center gap-1">
                  {{ col.label }}
                  <span v-if="sortKey === col.key">
                    <ArrowUpIcon v-if="sortOrder === 'asc'" class="h-3 w-3" />
                    <ArrowDownIcon v-else class="h-3 w-3" />
                  </span>
                </div>
              </th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-200 bg-white">
            <tr
              v-for="row in sortedDonations"
              :key="row.id || row.dateTime"
              class="hover:bg-gray-50 transition-colors"
            >
              <td class="whitespace-nowrap px-6 py-4 text-sm text-gray-900">{{ row.name }}</td>
              <td class="whitespace-nowrap px-6 py-4 text-sm text-gray-900">{{ row.phoneNumber }}</td>
              <td class="whitespace-nowrap px-6 py-4 text-sm text-gray-900">{{ row.addLine1 }}</td>
              <td class="whitespace-nowrap px-6 py-4 text-sm text-gray-900">{{ row.addLine2 }}</td>
              <td class="whitespace-nowrap px-6 py-4 text-sm text-gray-900">{{ row.servedFor }}</td>
              <td class="whitespace-nowrap px-6 py-4 text-sm text-gray-900">{{ row.foodType }}</td>
              <td class="whitespace-nowrap px-6 py-4 text-sm text-gray-500">{{ row.dateTime }}</td>
              <td class="whitespace-nowrap px-6 py-4 text-sm text-gray-500">{{ row.userEmail }}</td>
            </tr>
            <tr v-if="donationDetails.length === 0">
              <td :colspan="donationColumns.length" class="px-6 py-10 text-center text-sm text-gray-400">
                No donations yet.
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
