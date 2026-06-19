import { reactive } from 'vue'

export const toasts = reactive([])

let idCounter = 0

export function useToast() {
  const add = (message, type = 'info', duration = 3000) => {
    const id = ++idCounter
    toasts.push({ id, message, type })
    setTimeout(() => {
      const idx = toasts.findIndex(t => t.id === id)
      if (idx > -1) toasts.splice(idx, 1)
    }, duration)
  }

  const success = (message, duration = 3000) => add(message, 'success', duration)
  const error = (message, duration = 4000) => add(message, 'error', duration)

  return { add, success, error, toasts }
}
