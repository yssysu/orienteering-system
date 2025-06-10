<template>
  <div class="task-activation-container">
    <!-- 说明文本 -->
    <p class="info-text">
      如果您已到达任务指定地点但任务未激活，请与开发人员联系，获得任务激活代码。
    </p>

    <!-- 输入框和按钮 -->
    <input v-model="answer" type="text" placeholder="请输入激活代码" class="answer-input">
    <button @click="activateTask" class="activate-btn">激活任务</button>

    <!-- 插入图片 -->
    <img src="@/assets/两个工作人员.png" class="bottom-right-image" alt="插图">
  </div>
</template>

<script>
import axios from 'axios';
import Swal from 'sweetalert2'; // 引入 SweetAlert2

export default {
  data() {
    return {
      answer: '',
      studentId: null
    };
  },
  mounted() {
    // 在组件挂载时获取用户 ID 并存储
    this.studentId = this.$store.getters.getStudentId;
  },
  methods: {
    activateTask() {
      const data = {
        studentId: this.studentId,
        answer: this.answer
      };
      axios.post('http://127.0.0.1:8000/api/activate_task_by_answer/', data)
        .then(response => {
          console.log(response.data.message);

          // 激活任务成功后弹出美化的提示框
          Swal.fire({
            icon: 'success', // 图标
            title: '任务已激活',
            text: '您的任务已成功激活！',
            confirmButtonText: '确定',
            confirmButtonColor: '#FFB74D', // 设置按钮颜色
            background: '#fff', // 设置背景色
            showCloseButton: true, // 显示关闭按钮
            timer: 5000, // 自动关闭弹窗，单位毫秒
          });

        })
        .catch(error => {
          console.error('激活任务失败:', error);
          
          // 激活任务失败后的弹出窗口
          Swal.fire({
            icon: 'error', // 错误图标
            title: '激活任务失败',
            text: '请检查您的激活码或联系开发人员。',
            confirmButtonText: '重新尝试',
            confirmButtonColor: '#FF7043', // 错误按钮颜色
          });
        });
    }
  }
};
</script>

<style scoped>
/* 容器样式 */
.task-activation-container {
  background-image: url('@/assets/qianse_banck.jpg'); 
  background-size: cover;
  background-position: center;
  padding: 40px;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center; 
  justify-content: flex-start;
  position: relative; 
}
 /* 字体格式 */
.info-text {
  font-size: 25px;
  color: #333;
  margin-top: 180px; 
  margin-bottom: 50px; 
}
/* 回答格式 */
.answer-input {
  width: 20%;
  padding: 15px 20px;
  font-size: 18px; 
  border-radius: 8px;
  border: 1px solid #ddd;
  margin-bottom: 20px;
  outline: none;
  transition: border-color 0.3s ease;
}

.answer-input:focus {
  border-color: #FFB74D; 
}

.info-text, .answer-input, .activate-btn {
  font-family: 'Poppins', sans-serif;
}
.activate-btn {
  background-color: #FFB74D; 
  color: white;
  padding: 15px 30px;
  border: none;
  border-radius: 8px;
  font-size: 18px; 
  cursor: pointer;
  width: 20%;
  transition: background 0.3s, transform 0.3s;
}

.activate-btn:hover {
  background-color: #FFA726; 
  transform: scale(1.05);
}

.activate-btn:active {
  transform: scale(0.98);
}

.activate-btn:disabled {
  background-color: #d3d3d3;
  cursor: not-allowed;
}

/* 插入的图片样式 */
.bottom-right-image {
  position: absolute;
  bottom:70px;
  right: 50px;
  width: 30%; 
  height: auto;
}
</style>
