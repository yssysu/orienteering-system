<template>
  <div class="login-container">
    <div class="login-box">
      <h2>注册/登录</h2>
      <input v-model="studentId" placeholder="请输入学号" class="input-field" />
      <button @click="handleRegisterOrLogin" class="submit-btn">确定</button>
    </div>

    <!-- 右侧图片 -->
    <img src="@/assets/小男孩.png" alt="Right Image" class="right-image" />
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      studentId: ''  
    };
  },
  methods: {
    
    handleRegisterOrLogin() {
      // 发送请求到后端，判断是注册还是登录
      axios.post('http://127.0.0.1:8000/api/check_user/', { studentId: this.studentId })
        .then(response => {
          if (response.data.exists) {
            // 已存在，进行登录操作
            this.$store.commit('setStudentId', this.studentId); 
            this.$emit('loggedIn'); 
          } else {
            // 不存在，进行注册操作
            this.registerUser();
          }
        })
        .catch(error => {
          console.error('检查用户时出错:', error);
        });
    },
    registerUser() {
      axios.post('http://127.0.0.1:8000/api/register/', { studentId: this.studentId })
        .then(() => {
          console.log('注册成功');
          this.$store.commit('setStudentId', this.studentId); // 更新 Vuex 中的学生 ID 状态
          this.$emit('loggedIn'); // 通知父组件已登录
        })
        .catch(error => {
          console.error('注册失败:', error);
        });
    }
  }
};
</script>

<style scoped>
/* 设置左图 */
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-image: url('@/assets/小女孩.png'); 
  background-size: contain;
  background-position: left; 
  background-repeat: no-repeat; 
  position: relative; 
}

/* 登录框样式 */
.login-box {
  background-color: rgba(255, 255, 255, 0.8); 
  padding: 60px;
  border-radius: 8px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
  width: 500px;
  z-index: 1; /* 确保登录框在图片之上 */
}

/* 标题样式 */
h2 {
  text-align: center;
  margin-bottom: 20px;
}

/* 输入框样式 */
.input-field {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ccc;
  border-radius: 4px;
}

/* 按钮样式 */
.submit-btn {
  width: 100%;
  padding: 12px;
  background: linear-gradient(45deg, #ff5733, #ffbb33); 
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  cursor: pointer;
}

.submit-btn:hover {
  background: linear-gradient(45deg, #ff4500, #ffa500); 
}

/* 右侧图片样式 */
.right-image {
  position: absolute;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  z-index: 0;
  max-width: 30%;
}
</style>
