<template>
  <div class="task-list-container">
    <h2 class="title">
      <img src="@/assets/制作任务列表.png" alt="任务列表" class="title-image" />
    </h2>
    <p v-if="loading" class="loading">加载中...</p>
    <p v-else-if="error" class="error">{{ error }}</p>
    <div v-else class="task-cards">
      <!-- 显示四个任务 -->
      <div v-for="taskNumber in [1, 2, 3, 4]" :key="taskNumber" class="task-card">
        <h3 class="task-title">
          <!-- 在标题左侧添加待办图片 -->
          <img src="@/assets/待办.png" alt="待办" class="todo-image" />
          任务 {{ taskNumber }}
        </h3>
        <p class="task-status">激活状态: {{ playerInfo[`task${taskNumber}_active`] ? '已激活' : '未激活' }}</p>
        <p class="task-status">完成状态: {{ playerInfo[`task${taskNumber}_completed`] ? '已完成' : '未完成' }}</p>
        <button 
          :class="{
            'start-btn': true,
            'disabled': !playerInfo[`task${taskNumber}_active`], 
            'completed': playerInfo[`task${taskNumber}_active`] && playerInfo[`task${taskNumber}_completed`]
          }" 
          :disabled="!playerInfo[`task${taskNumber}_active`] || playerInfo[`task${taskNumber}_completed`]"
          @click="startGame(taskNumber)">
          {{ playerInfo[`task${taskNumber}_active`] && playerInfo[`task${taskNumber}_completed`] ? '已完成' : '开始游戏' }}
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { useStore } from 'vuex';

export default {
  name: 'TaskList',
  data() {
    return {
      playerInfo: {},
      loading: true,
      error: null
    };
  },
  mounted() {
    const store = useStore();
    const studentId = store.getters.getStudentId;
    axios.get(`http://127.0.0.1:8000/api/player_info/?studentId=${studentId}`)
      .then(response => {
        this.playerInfo = response.data;
        this.loading = false;
      })
      .catch(error => {
        this.error = '获取玩家信息失败';
        this.loading = false;
        console.error('获取玩家信息失败:', error);
      });
  },
  methods: {
    startGame(taskNumber) {
      const taskActiveKey = `task${taskNumber}_active`;
      const taskCompletedKey = `task${taskNumber}_completed`;

      const isActive = this.playerInfo[taskActiveKey];
      const isCompleted = this.playerInfo[taskCompletedKey];

      if (isActive && !isCompleted) {
        const store = this.$store;
        const studentId = store.getters.getStudentId;

        let targetRouteName;
        switch (taskNumber) {
          case 1:
            targetRouteName = 'GameOne';
            break;
          case 2:
            targetRouteName = 'GameTwo';
            break;
          case 3:
            targetRouteName = 'GameThree';
            break;
          case 4:
            targetRouteName = 'GameFour';
            break;
          default:
            targetRouteName = 'DefaultRoute';
        }

        const navigateToRoute = (routeName, params, query) => {
          this.$router.push({
            name: routeName,
            params,
            query
          });
        };

        const routeParams = { taskNumber };
        const routeQuery = { studentId };

        navigateToRoute(targetRouteName, routeParams, routeQuery);
        console.log('启动任务，进入游戏');
      } else {
        console.log('任务未激活或已完成，无法开始');
      }
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');

.task-list-container {
  background-image: url('@/assets/qianse_banck.jpg');
  background-size: cover;
  background-position: center;
  padding: 40px;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  font-family: 'Poppins', sans-serif;
}

.title {
  margin: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 30px;
  font-family: 'Poppins', sans-serif;
}

.title-image {
  max-width: 50%;
  height: auto;
}

.loading,
.error {
  font-size: 18px;
  color: white;
  margin-top: 20px;
  font-family: 'Poppins', sans-serif;
}

.task-cards {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  justify-content: center;
  align-items: center;
  width: 100%;
  max-width: 900px;
  font-family: 'Poppins', sans-serif;
}

.task-card {
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  height: 250px;
}

.task-card:hover {
  transform: translateY(-5px);
}

.task-title {
  font-size: 35px;
  font-weight: bold;
  margin-bottom: 15px;
  font-family: 'Poppins', sans-serif;
  display: flex;
  align-items: center;
}
/* 待办图片 */
.todo-image {
  width: 60px; 
  height: auto;
}

.task-status {
  font-size: 16px;
  color: #333;
  margin: 5px 0;
  font-family: 'Poppins', sans-serif;
}

.start-btn {
  margin-top: 20px;
  padding: 12px 20px;
  background: linear-gradient(45deg, #ff5733, #ffbb33);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.3s ease, transform 0.3s ease;
  font-family: 'Poppins', sans-serif;
}

.start-btn:hover {
  background: linear-gradient(45deg, #ff4500, #ffa500);
  transform: translateY(-3px);
}

.start-btn:active {
  transform: translateY(1px);
}

.start-btn.disabled {
  background: #d3d3d3;
  cursor: not-allowed;
}

.start-btn.completed {
  background: #e38913;
  cursor: not-allowed;
}

.start-btn:disabled {
  opacity: 0.7;
}

</style>