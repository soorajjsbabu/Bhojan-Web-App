<script setup>
import { ref, computed, onMounted } from 'vue'
import { api } from '../api.js'
import { ArrowUpIcon, ArrowDownIcon } from '@heroicons/vue/24/solid'

const donationDetails = ref([])
const sortKey = ref('')
const sortOrder = ref('asc')

const columns = [
  { key: 'name', label: 'Name' },
  { key: 'phoneNumber', label: 'Contact Phone' },
  { key: 'addLine1', label: 'Address Line 1' },
  { key: 'addLine2', label: 'Address Line 2' },
  { key: 'servedFor', label: 'Served For' },
  { key: 'foodType', label: 'Food Type' },
  { key: 'dateTime', label: 'Date/Time' },
]

onMounted(() => {
  api.get('/userDonations')
    .then((response) => {
      donationDetails.value = response.data.donations.map((d) => ({
        ...d,
        dateTime: new Date(d.dateTime).toLocaleString(),
      }))
    })
})

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
  return [...donationDetails.value].sort((a, b) => {
    if (a[key] < b[key]) return -1 * order
    if (a[key] > b[key]) return 1 * order
    return 0
  })
})
</script>

<template>
  <div class="mx-auto max-w-7xl px-4 py-10 sm:px-6 lg:px-8">
    <h1 class="text-3xl font-bold text-gray-900 mb-8">Your Donations</h1>

    <div class="overflow-hidden rounded-xl border border-gray-200 bg-white shadow-sm">
      <div class="overflow-x-auto">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th
                v-for="col in columns"
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
            <tr v-for="row in sortedDonations" :key="row.id || row.phoneNumber + row.dateTime" class="hover:bg-gray-50 transition-colors">
              <td class="whitespace-nowrap px-6 py-4 text-sm text-gray-900">{{ row.name }}</td>
              <td class="whitespace-nowrap px-6 py-4 text-sm text-gray-900">{{ row.phoneNumber }}</td>
              <td class="whitespace-nowrap px-6 py-4 text-sm text-gray-900">{{ row.addLine1 }}</td>
              <td class="whitespace-nowrap px-6 py-4 text-sm text-gray-900">{{ row.addLine2 }}</td>
              <td class="whitespace-nowrap px-6 py-4 text-sm text-gray-900">{{ row.servedFor }}</td>
              <td class="whitespace-nowrap px-6 py-4 text-sm text-gray-900">{{ row.foodType }}</td>
              <td class="whitespace-nowrap px-6 py-4 text-sm text-gray-500">{{ row.dateTime }}</td>
            </tr>
            <tr v-if="donationDetails.length === 0">
              <td :colspan="columns.length" class="px-6 py-8 text-center text-sm text-gray-500">
                No donations found.
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
