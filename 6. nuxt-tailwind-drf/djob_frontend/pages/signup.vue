<script setup>
const router = useRouter()

let email = ''
let password1 = ''
let password2 = ''
let errors = ref([])

async function submitForm() {
    errors.value = []
    if (password1 === password2) {
        await $fetch('http://127.0.0.1:8000/api/v1/users/', {
            method: 'POST',
            body: {
                username: email,
                password: password1
            }
        }).then(response => {
            router.push({ path: '/login/' })
        }).catch(error => {
            if (error.response) {
                for (const property in error.response._data) {
                    errors.value.push(`${property}: ${error.response._data[property]}`)
                }
            } else if (error.message) {
                errors.value.push('Something went wrong. Please try again')
            }
        })
    }
    else {
        errors.value.push('The password is not confirmed correctly.')
    }
}
</script>

<template>
    <div class="py-10 px-6">
        <div class="max-w-sm mx-auto py-10 px-6 bg-gray-100 rounded-xl">
            <h1 class="mb-6 text-2xl">Sign up</h1>
            <form v-on:submit.prevent="submitForm">
                <input type="email" v-model="email" placeholder="Your email address..."
                    class="bg-white outline-none w-full mb-4 py-4 px-6 rounded-xl">
                <input type="password" v-model="password1" placeholder="Your password..."
                    class="bg-white outline-none w-full mb-4 py-4 px-6 rounded-xl">
                <input type="password" v-model="password2" placeholder="Repeat password..."
                    class="bg-white outline-none w-full mb-4 py-4 px-6 rounded-xl">

                <div v-if="errors.length" class="mb-6 y-4 px-6 bg-rose-400 text-white rounded-xl">
                    <p v-for="error in errors" :key="error">{{ error }}</p>
                </div>

                <button class="py-4 px-6 bg-teal-700 text-white rounded-2xl">Submit</button>
            </form>
        </div>
    </div>
</template>
