import { reactive } from 'vue'
import { auth } from '../firebase.js'
import { onAuthStateChanged, signOut as firebaseSignOut } from 'firebase/auth'

const ADMIN_EMAIL = import.meta.env.VITE_ADMIN_EMAIL || ''

export const authStore = reactive({
  email: '',
  uid: '',
  signedIn: false,
  isAdmin: false,
  showFooter: true,

  init() {
    return new Promise((resolve) => {
      let resolved = false
      onAuthStateChanged(auth, (user) => {
        if (user) {
          this.email = user.email || ''
          this.uid = user.uid
          this.signedIn = true
          this.isAdmin = !!ADMIN_EMAIL && user.email === ADMIN_EMAIL
          this.showFooter = !this.isAdmin
        } else {
          this.email = ''
          this.uid = ''
          this.signedIn = false
          this.isAdmin = false
          this.showFooter = true
        }
        if (!resolved) { resolved = true; resolve() }
      })
    })
  },

  async signOut() {
    await firebaseSignOut(auth)
  },
})
