import axios from 'axios'
import { auth } from './firebase.js'

export const api = axios.create({
  baseURL: 'http://127.0.0.1:5000',
  timeout: 30000,
  headers: { 'Content-Type': 'application/json' },
})

api.interceptors.request.use(async (config) => {
  const user = auth.currentUser
  if (user) {
    const token = await user.getIdToken()
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})
