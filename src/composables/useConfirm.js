import { reactive } from 'vue'

export const confirmState = reactive({
  show: false,
  title: '',
  message: '',
  resolve: null,
})

export function useConfirm() {
  const confirm = ({ title, message }) => {
    return new Promise((resolve) => {
      confirmState.show = true
      confirmState.title = title || 'Confirm'
      confirmState.message = message
      confirmState.resolve = (value) => {
        confirmState.show = false
        resolve(value)
      }
    })
  }
  return { confirm, confirmState }
}
