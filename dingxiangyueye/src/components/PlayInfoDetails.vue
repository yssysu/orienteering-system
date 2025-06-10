<template>
  <div>
    <h2>玩家信息</h2>
    <p v-if="playerInfo.student_id">学号: {{ playerInfo.student_id }}</p>
    <p v-if="playerInfo.task1_active !== undefined">任务 1 激活状态: {{ playerInfo.task1_active }}</p>
    <p v-if="playerInfo.task1_completed !== undefined">任务 1 完成状态: {{ playerInfo.task1_completed }}</p>
    <p v-if="playerInfo.task2_active !== undefined">任务 2 激活状态: {{ playerInfo.task2_active }}</p>
    <p v-if="playerInfo.task2_completed !== undefined">任务 2 完成状态: {{ playerInfo.task2_completed }}</p>
    <p v-if="playerInfo.task3_active !== undefined">任务 3 激活状态: {{ playerInfo.task3_active }}</p>
    <p v-if="playerInfo.task3_completed !== undefined">任务 3 完成状态: {{ playerInfo.task3_completed }}</p>
    <p v-if="playerInfo.task4_active !== undefined">任务 4 激活状态: {{ playerInfo.task4_active }}</p>
    <p v-if="playerInfo.task4_completed !== undefined">任务 4 完成状态: {{ playerInfo.task4_completed }}</p>
    <p v-else>加载中...</p>
  </div>
</template>

<script>
import axios from 'axios';
import { useStore } from 'vuex';

export default {
  name: 'PlayerInfoDetail',
  data() {
    return {
      playerInfo: {}
    };
  },
  mounted() {
    const store = useStore();
    const studentId = store.getters.getStudentId;
    
    // 检查是否获取到学生 ID
    if (!studentId) {
      console.error('未获取到学生 ID');
      return;
    }

    axios.get(`http://127.0.0.1:8000/api/player_info/?studentId=${studentId}`)
      .then(response => {
        this.playerInfo = response.data;
      })
      .catch(error => {
        console.error('获取玩家信息失败:', error);
      });
  }
};
</script>