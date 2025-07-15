import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
    state: () => ({
        user: {
            isAuthenticated: true,
            email: null,
            token: null
        }
    }),
    actions: {
        initStore() {
            this.user.isAuthenticated = false
            if (localStorage.getItem('user.token')) {
                this.user.email = localStorage.getItem('user.email')
                this.user.token = localStorage.getItem('user.token')
                this.user.isAuthenticated = true
            }
        },
        setToken(token, email) {
            this.user.token = token
            this.user.email = email
            this.user.isAuthenticated = true
            localStorage.setItem('user.token', token)
            localStorage.setItem('user.email', email)
        },
        removeToken() {
            this.user.token = null
            this.user.email = null
            this.user.isAuthenticated = false
            localStorage.setItem('user.token', '')
            localStorage.setItem('user.email', '')
        }
    }
})