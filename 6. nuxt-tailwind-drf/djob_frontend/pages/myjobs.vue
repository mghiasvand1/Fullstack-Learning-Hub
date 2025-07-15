<script setup>
import { ref, onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'

const userStore = useUserStore()
const router = useRouter()

const jobs = ref([])

onMounted(() => {
  if (!userStore.user.isAuthenticated) {
    router.push('/login')
  } else {
    getJobs()
  }
})

useSeoMeta({
  title: 'My Jobs',
  ogTitle: 'My Jobs',
  description: 'The Description'
})

async function getJobs() {
  try {
    const response = await $fetch('http://127.0.0.1:8000/api/v1/jobs/my', {
      headers: {
        'Authorization': 'token ' + userStore.user.token,
        'Content-Type': 'application/json'
      }
    })

    for (const data of response) {
      jobs.value.push(data)
    }
  } catch (error) {
  }
}

function deleteJob(id) {
    jobs.value = jobs.value.filter(job => job.id !== id)
}

</script>

<template>
  <div class="py-10 px-6">
    <h1 class="mb-6 text-2xl">My Jobs</h1>

    <div class="space-y-4">
            <Job
                v-for="job in jobs"
                :key="job.id"
                :job="job" 
                :my="true"
                v-on:deleteJob="deleteJob(job.id)"
            />
        </div>
  </div>
</template>
