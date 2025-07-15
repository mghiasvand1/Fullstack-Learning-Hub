<script setup>
import { ref, onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'

const userStore = useUserStore()
const router = useRouter()

const jobCategories = ref([])

let category = ''
let title = ''
let description = ''
let position_salary = ''
let position_location = ''
let company_name = ''
let company_location = ''
let company_email = ''
let errors = ref([])

onMounted(async () => {
    if (!userStore.user.isAuthenticated) {
        router.push('/login')
    } else {
        const response = await $fetch('http://127.0.0.1:8000/api/v1/jobs/categories/')
        jobCategories.value = response
    }
})

async function submitForm() {

    errors.value = []

    if (category == '') { errors.value.push('You must select a category') }
    if (title == '') { errors.value.push('The title field is missing') }
    if (description == '') { errors.value.push('The description field is missing') }
    if (position_salary == '') { errors.value.push('The position salary field is missing') }
    if (position_location == '') { errors.value.push('The position location field is missing') }
    if (company_name == '') { errors.value.push('The company name field is missing') }
    if (company_location == '') { errors.value.push('The company location field is missing') }
    if (company_email == '') { errors.value.push('The company email field is missing') }

    if (errors.value.length == 0) {
        await $fetch('http://127.0.0.1:8000/api/v1/jobs/create/', {
            method: 'POST',
            headers: {
                'Authorization': 'token ' + userStore.user.token,
                'Content-Type': 'application/json'
            },
            body: {
                category: category,
                title: title,
                description: description,
                position_salary: position_salary,
                position_location: position_location,
                company_name: company_name,
                company_location: company_location,
                company_email: company_email
            }
        })
            .then(response => {
                console.log(response);
                
                router.push({ path: '/myjobs' })
            })
            .catch(error => {
                if (error.response) {
                    for (const property in error.response._data) {
                        errors.value.push(`${property}: ${error.response._data[property]}`)
                    }
                } else if (error.message) {
                    errors.value.push('Something went wrong. Please try again')
                }
            })
    }
}
</script>

<template>
    <div class="py-10 px-6">
        <h1 class="mb-6 text-2xl">Create job</h1>

        <form v-on:submit.prevent="submitForm" class="space-y-4">
            <div>
                <label>Category</label>

                <select v-model="category" class="w-full mt-2 p-4 rounded-xl bg-gray-100">
                    <option value="">Select category</option>
                    <option v-for="category in jobCategories" v-bind:key="category.id" v-bind:value="category.id">
                        {{ category.title }}
                    </option>
                </select>
            </div>

            <div>
                <label>Title</label>
                <input v-model="title" type="text" class="w-full mt-2 p-4 rounded-xl bg-gray-100">
            </div>

            <div>
                <label>Description</label>
                <textarea v-model="description" class="w-full mt-2 p-4 rounded-xl bg-gray-100"></textarea>
            </div>

            <div>
                <label>Salary</label>
                <input type="text" v-model="position_salary" class="w-full mt-2 p-4 rounded-xl bg-gray-100">
            </div>

            <div>
                <label>Location</label>
                <input type="text" v-model="position_location" class="w-full mt-2 p-4 rounded-xl bg-gray-100">
            </div>

            <div>
                <label>Company name</label>
                <input type="text" v-model="company_name" class="w-full mt-2 p-4 rounded-xl bg-gray-100">
            </div>

            <div>
                <label>Company location</label>
                <input type="text" v-model="company_location" class="w-full mt-2 p-4 rounded-xl bg-gray-100">
            </div>

            <div>
                <label>Company e-mail</label>
                <input type="text" v-model="company_email" class="w-full mt-2 p-4 rounded-xl bg-gray-100">
            </div>

            <div v-if="errors.length" class="mb-6 py-4 px-6 bg-rose-400 text-white rounded-xl">
                <p v-for="error in errors" v-bind:key="error">
                    {{ error }}
                </p>
            </div>

            <button class="py-4 px-6 bg-teal-700 text-white rounded-xl">Submit</button>
        </form>
    </div>
</template>