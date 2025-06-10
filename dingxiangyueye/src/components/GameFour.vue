<template>
  <div class="game-container">
    <h2 class="title">任务 4：找不同</h2>

    <!-- 循环渲染2组图片 -->
    <div v-for="(group, index) in imageGroups" :key="index" class="image-group">
      <div class="image-container">
        <img :src="group.image1" alt="图片1" class="image" />
        <img :src="group.image2" alt="图片2" class="image" />
      </div>
      <p class="group-label">第{{ index + 1 }}组</p> <!-- 添加组别信息 -->
    </div>

    <div class="input-container">
      <p class="question-text">总共有多少个不同：</p>
      <input v-model="userAnswer" type="number" class="answer-input" placeholder="输入你的答案">
      <button @click="checkAnswer" class="submit-button">提交答案</button>
    </div>

    <!-- 弹出窗口，使用 v-if 控制显示隐藏 -->
    <div v-if="showPopup" class="popup">
      <p class="popup-message">{{ popupMessage }}</p>
      <button @click="confirmAnswer" class="popup-button">确定</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { useStore } from 'vuex';

export default {
  name: 'FindDifferencesComponent',
  data() {
    return {
      userAnswer: null, // 用户输入的答案
      showPopup: false, // 控制弹出窗口的显示
      popupMessage: '', // 弹出窗口的消息
      studentId: null, // 存储学生 ID
      imageGroups: [
        { image1: require('@/assets/院楼.jpg'), image2: require('@/assets/院楼_change.jpg') },
        { image1: require('@/assets/牌坊.jpg'), image2: require('@/assets/牌坊_change.jpg') }
      ]
    };
  },
  mounted() {
    const store = useStore();
    this.studentId = store.getters.getStudentId;
  },
  methods: {
    // 检查用户答案
    checkAnswer() {
      if (this.userAnswer === 5) {
        this.popupMessage = '回答正确';
        this.showPopup = true;
      } else {
        this.popupMessage = '回答错误，请重新输入';
        this.showPopup = true;
      }
    },
    // 确认答案后返回任务列表并更新数据库
    confirmAnswer() {
      if (this.popupMessage === '回答正确') {
        const data = {
          studentId: this.studentId,
          taskId: 4,
        };
        // 发送请求到后端更新数据库
        axios.post('http://127.0.0.1:8000/api/submit_task_answer/', data)
          .then(() => {
            // 请求成功，返回任务列表
            this.$router.push('/task-list');
          })
          .catch((error) => {
            console.error('更新任务状态失败:', error);
          });
      }
      // 关闭弹出窗口
      this.showPopup = false;
    }
  }
};
</script>

<style scoped>
.game-container {
 
  background-image: url('@/assets/qianse_banck.jpg');
  background-size: cover;
  background-position: center;
  padding: 50px;
 
}

.title {
  text-align: center;
  font-size: 32px;
  color: #333;
  margin-bottom: 10px;
  font-family: 'Poppins', sans-serif;
}

.image-group {
  display: flex;
  flex-direction: column;
  align-items: center;    
  margin-bottom: 20px;
}

.image-container {
  display: flex;
  justify-content: space-around;
  margin-top: 10px;  
}

.image {
  max-width: 100%;      
  width: 550px;         
  height: auto;         
  border: 2px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}


.group-label {
  font-size: 25px;
  color: #333;
  font-weight: bold;
  margin-bottom: 10px; 
  font-family: 'Poppins', sans-serif;
}

.input-container {
  text-align: center;
  margin-top: 20px;
}

.question-text {
  font-size: 25px;
  color: #333;
  margin-bottom: 10px;
  font-family: 'Poppins', sans-serif;  
  
}

.answer-input {
  padding: 10px;
  font-size: 16px;
  width: 20ch;
  border-radius: 5px;
  border: 1px solid #ddd;
  margin-right: 20px;
  font-family: 'Poppins', sans-serif;
}

.submit-button {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-button:hover {
  background-color: #45a049;
}

.popup {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
  padding: 30px;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
  text-align: center;
  width: 300px;
}

.popup-message {
  font-size: 18px;
  color: #333;
  margin-bottom: 20px;
  font-family: 'Poppins', sans-serif;
}

.popup-button {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.popup-button:hover {
  background-color: #0056b3;
}
</style>
