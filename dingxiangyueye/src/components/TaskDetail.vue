<template>
    <div>
      <h2>{{ task.name }}</h2>
      <p>{{ task.description }}</p>
      <img v-if="task.image" :src="task.image" alt="任务图片">
      <video v-if="task.video" :src="task.video" controls></video>
      <button @click="closeTaskDetail">返回任务列表</button>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      task: {
        type: Object,
        required: true
      }
    },
    methods: {
      closeTaskDetail() {
        this.$emit('close');
      }
    }
  };
  </script>
  

