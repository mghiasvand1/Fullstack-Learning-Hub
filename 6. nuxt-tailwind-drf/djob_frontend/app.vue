<script setup>
import { onMounted, ref } from 'vue';
import { useUserStore } from '@/stores/user';

const userStore = useUserStore()
const isReady = ref(false)

onMounted(() => {
  userStore.initStore()
  isReady.value = true
})
</script>

<template>
  <div v-if="isReady">
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>
