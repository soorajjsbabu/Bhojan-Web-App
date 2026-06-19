import { reactive } from 'vue'

export const alertState = reactive({
  show: false,
  message: '',
  type: 'info',
  resolve: null,
})

export function useAlert() {
  const alert = (message, type = 'info') => {
    return new Promise((resolve) => {
      alertState.show = true
      alertState.message = message
      alertState.type = type
      alertState.resolve = () => {
        alertState.show = false
        resolve()
      }
    })
  }
  return { alert, alertState }
}
