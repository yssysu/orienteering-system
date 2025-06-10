<template>
  <div class="container">
    <div>
      <!-- 问题 1 -->
      <div class="question-card">
        <h2>题目 1：以下哪个是常见的 web GIS 地图服务接口？</h2>
        <div class="options">
          <div>
            <input type="radio" id="q1a1" v-model="userAnswer[0]" :value="1">
            <label for="q1a1">A. RESTful API</label>
          </div>
          <div>
            <input type="radio" id="q1a2" v-model="userAnswer[0]" :value="2">
            <label for="q1a2">B. FTP</label>
          </div>
          <div>
            <input type="radio" id="q1a3" v-model="userAnswer[0]" :value="3">
            <label for="q1a3">C. SMTP</label>
          </div>
          <div>
            <input type="radio" id="q1a4" v-model="userAnswer[0]" :value="4">
            <label for="q1a4">D. SSH</label>
          </div>
        </div>
      </div>

      <!-- 问题 2 -->
      <div class="question-card">
        <h2>题目 2：在 web GIS 中，用于存储地理空间数据的常见文件格式是？</h2>
        <div class="options">
          <div>
            <input type="radio" id="q2a1" v-model="userAnswer[1]" :value="1">
            <label for="q2a1">A. .txt</label>
          </div>
          <div>
            <input type="radio" id="q2a2" v-model="userAnswer[1]" :value="2">
            <label for="q2a2">B. .shp</label>
          </div>
          <div>
            <input type="radio" id="q2a3" v-model="userAnswer[1]" :value="3">
            <label for="q2a3">C. .docx</label>
          </div>
          <div>
            <input type="radio" id="q2a4" v-model="userAnswer[1]" :value="4">
            <label for="q2a4">D. .xlsx</label>
          </div>
        </div>
      </div>

      <!-- 问题 3 -->
      <div class="question-card">
        <h2>题目 3：以下哪个不是 web GIS 中常用的地图投影方式？</h2>
        <div class="options">
          <div>
            <input type="radio" id="q3a1" v-model="userAnswer[2]" :value="1">
            <label for="q3a1">A. 墨卡托投影</label>
          </div>
          <div>
            <input type="radio" id="q3a2" v-model="userAnswer[2]" :value="2">
            <label for="q3a2">B. 高斯 - 克吕格投影</label>
          </div>
          <div>
            <input type="radio" id="q3a3" v-model="userAnswer[2]" :value="3">
            <label for="q3a3">C. 透视投影</label>
          </div>
          <div>
            <input type="radio" id="q3a4" v-model="userAnswer[2]" :value="4">
            <label for="q3a4">D. 兰伯特投影</label>
          </div>
        </div>
      </div>

      <!-- 问题 4 -->
      <div class="question-card">
        <h2>题目 4：在 web GIS 开发中，用于处理地理空间数据的 JavaScript 库是？</h2>
        <div class="options">
          <div>
            <input type="radio" id="q4a1" v-model="userAnswer[3]" :value="1">
            <label for="q4a1">A. jQuery</label>
          </div>
          <div>
            <input type="radio" id="q4a2" v-model="userAnswer[3]" :value="2">
            <label for="q4a2">B. Leaflet</label>
          </div>
          <div>
            <input type="radio" id="q4a3" v-model="userAnswer[3]" :value="3">
            <label for="q4a3">C. React</label>
          </div>
          <div>
            <input type="radio" id="q4a4" v-model="userAnswer[3]" :value="4">
            <label for="q4a4">D. Vue.js</label>
          </div>
        </div>
      </div>

      <!-- 问题 5 -->
      <div class="question-card">
        <h2>题目 5：Web GIS 中的空间数据库常用的数据库系统是？</h2>
        <div class="options">
          <div>
            <input type="radio" id="q5a1" v-model="userAnswer[4]" :value="1">
            <label for="q5a1">A. MySQL</label>
          </div>
          <div>
            <input type="radio" id="q5a2" v-model="userAnswer[4]" :value="2">
            <label for="q5a2">B. Oracle</label>
          </div>
          <div>
            <input type="radio" id="q5a3" v-model="userAnswer[4]" :value="3">
            <label for="q5a3">C. PostgreSQL/PostGIS</label>
          </div>
          <div>
            <input type="radio" id="q5a4" v-model="userAnswer[4]" :value="4">
            <label for="q5a4">D. MongoDB</label>
          </div>
        </div>
      </div>

      <!-- 提交按钮 -->
      <div class="submit-button-container">
        <button @click="checkAnswer" class="submit-button">提交答案</button>
      </div>

      <!-- 弹出窗口 -->
      <div v-if="showPopup" class="popup">
        <div class="popup-content">
          <p>{{ popupMessage }}</p>
          <p v-if="wrongQuestions.length > 0" class="wrong-questions">
            错误题目：{{ wrongQuestions.join(', ') }}
          </p>
          <button @click="confirmAnswer" class="confirm-button">确定</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { useStore } from 'vuex';

export default {
  name: 'Task1Component',
  data() {
    return {
      userAnswer: Array.from({ length: 5 }, () => null),
      showPopup: false,
      popupMessage: '',
      studentId: null,
      correctAnswers: [1, 2, 3, 2, 3],  // 这里是每个问题的正确答案
      wrongQuestions: []
    };
  },
  mounted() {
    const store = useStore();
    this.studentId = store.getters.getStudentId;
  },
  methods: {
    checkAnswer() {
      const wrongQuestions = [];
      for (let i = 0; i < 5; i++) {
        if (this.userAnswer[i] !== this.correctAnswers[i]) {
          wrongQuestions.push(i + 1);
        }
      }
      if (wrongQuestions.length === 0) {
        this.popupMessage = '回答正确！';
      } else {
        this.popupMessage = '回答错误，请重新输入';
      }
      this.wrongQuestions = wrongQuestions;
      this.showPopup = true;
    },
    confirmAnswer() {
      if (this.popupMessage === '回答正确！') {
        const data = {
          studentId: this.studentId,
          taskId: 1
        };
        axios.post('http://127.0.0.1:8000/api/submit_task_answer/', data)
          .then(() => {
            this.$router.push('/task-list');
          })
          .catch((error) => {
            console.error('更新任务状态失败:', error);
          });
      }
      this.showPopup = false;
    }
  }
};
</script>

<style scoped>
/* 使用 Poppins 字体 */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

body {
  font-family: 'Poppins', sans-serif;
}

.container {
  background-image: url('@/assets/qianse_banck.jpg');
  background-size: cover;
  background-position: center;
  padding: 20px;
  min-height: 100vh;
}

.question-card {
  background: #fff;
  border-radius: 15px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
  padding: 20px;
  width: 100%;
  max-width: 800px;
  margin: 20px auto;
}

h2 {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 10px;
  font-family: 'Poppins', sans-serif;
}

label {
  font-size: 16px;
  font-family: 'Poppins', sans-serif;
}

.options {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}

.options div {
  display: flex;
  align-items: center;
  margin-right: 20px;
}

input[type="radio"] {
  margin-right: 10px;
}

/* 提交按钮容器样式 */
.submit-button-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

/* 按钮样式 */
.submit-button {
  background-color: #ff6a00; 
  color: white;
  font-size: 16px;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-family: 'Poppins', sans-serif;
}

.submit-button:hover {
  background-color: #e65c00;
}

/* 弹出窗口样式 */
.popup {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.popup-content {
  background: linear-gradient(145deg, #ff6a00, #ff9800);
  padding: 20px;
  border-radius: 15px;
  text-align: center;
  color: white;
  font-size: 18px;
  max-width: 500px;
  width: 100%;
}

.wrong-questions {
  color: #ffb3b3;
}

/* 确定按钮样式 */
.confirm-button {
  background-color: #ff6a00;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  font-family: 'Poppins', sans-serif;
}

.confirm-button:hover {
  background-color: #e65c00;
}
</style>
