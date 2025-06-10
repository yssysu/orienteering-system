<template>
  <div class="game-page">
    <h1 class="task-title">任务: {{ taskNumber }}</h1>
    <div v-if="taskNumber == 1" class="iframe-container">
      <iframe
        :src="gameUrl"
        width="100%" 
        height="100%" 
        frameborder="0" 
        scrolling="no" 
        title="2048 Game"
        @load="checkScore"
      ></iframe>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Swal from 'sweetalert2'; 

export default {
  name: 'GameOne',
  props: ['taskNumber'],
  data() {
    return {
      randomParam: Math.random().toString(36).substring(7), 
      studentId: null,
      gameStarted: false // 用于控制游戏是否已经开始
    };
  },
  computed: {
    gameUrl() {
      if (!this.studentId) {
        return '/2048-master/index.html?error=studentId_missing'; 
      }
      // 通过随机参数刷新游戏页面，确保每次都加载新的游戏
      return `/2048-master/index.html?studentId=${this.studentId}&refresh=${this.randomParam}`;
    }
  },
  methods: {
    checkScore() {
      const iframe = document.querySelector('iframe');
      const iframeWindow = iframe.contentWindow;
      const interval = setInterval(() => {
        const scoreContainer = iframeWindow.document.querySelector('.score-container');
        if (scoreContainer) {
          const score = parseInt(scoreContainer.textContent);
          if (score >= 1000) {  // 改为1000分过关
            clearInterval(interval);
            // 使用 SweetAlert2 来显示任务完成的提示
            Swal.fire({
              icon: 'success', 
              title: '恭喜您达到1000分！', 
              text: '任务已完成，是否返回任务选择页面？',
              showCancelButton: true, 
              confirmButtonText: '返回任务选择', 
              cancelButtonText: '继续游戏',
              confirmButtonColor: '#FFB74D',
              cancelButtonColor: '#FF7043',
              customClass: {
                popup: 'custom-popup', // 自定义弹窗样式
                title: 'custom-title', // 自定义标题样式
                content: 'custom-content', // 自定义内容样式
                confirmButton: 'custom-confirm-button', // 自定义确认按钮样式
                cancelButton: 'custom-cancel-button' // 自定义取消按钮样式
              }
            }).then((result) => {
              if (result.isConfirmed) {
                this.confirmAnswer();
              }
            });
          }
        }
      }, 1000);
    },
    confirmAnswer() {
      const data = {
        studentId: this.studentId,
        taskId: 1,
      };
      axios.post('http://127.0.0.1:8000/api/submit_task_answer/', data)
        .then(() => {
          this.$router.push('/task-list');
        })
        .catch((error) => {
          console.error('更新任务状态失败:', error);
        });
    },
    fetchstudentId() {
      const urlParams = new URLSearchParams(window.location.search);
      const studentId = urlParams.get('studentId');
      if (!studentId) {
        console.error('URL 参数中缺少 studentId');
        alert('无法加载任务：缺少用户 ID，请检查 URL 参数！');
      }
      this.studentId = studentId;
    },
    showRules() {
      // 使用 SweetAlert2 来显示规则介绍
      Swal.fire({
        icon: 'info',
        title: '2048 游戏规则',
        html: `
          <p>欢迎来到2048游戏！这是一个数字合并游戏，您的目标是通过合并相同的数字来创建一个更大的数字，最终达到2048。</p>
          <p>游戏的操作非常简单，您只需要使用方向键来控制数字的移动。每次移动时，两个相同的数字会合并成一个新的数字，直到达到2048。</p>
          <p>但是，您的任务并不要求您必须达到2048！任务完成的标准是，当您的分数达到1000分时，任务就算完成了。</p>
          <p>祝您好运，尽情享受游戏吧！</p>
        `,
        confirmButtonText: '开始游戏',
        confirmButtonColor: '#FFB74D',
        customClass: {
          popup: 'custom-popup', // 自定义弹窗样式
          title: 'custom-title', // 自定义标题样式
          content: 'custom-content', // 自定义内容样式
          confirmButton: 'custom-confirm-button', // 自定义确认按钮样式
        }
      }).then(() => {
        this.gameStarted = true;  // 游戏开始
      });
    }
  },
  mounted() {
    this.fetchstudentId();
    this.showRules(); // 在页面加载时显示规则介绍
  }
};
</script>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

.game-page {
  background-image: url('@/assets/qianse_banck.jpg');
  background-size: cover;
  background-position: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  text-align: center;
  overflow: hidden; 
}

.task-title {
  font-family: 'Poppins', sans-serif; 
  font-size: 36px; 
  font-weight: 600; 
  color: #817474; 
  margin-bottom: 20px; 
  padding: 10px; 
  border-radius: 10px; 
}

.iframe-container {
  width: 100%;
  height: 100%;
  position: relative;
  overflow: hidden;
}

iframe {
  width: 100%;
  height: 100%;
  border: none;
  overflow: hidden; 
}

/* 美化弹窗 */
.custom-popup {
  background-color: #f7f7f7 !important;
  border-radius: 20px;
  padding: 40px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  width: 80%;
  max-width: 1000px; /* 设置最大宽度 */
  font-family: 'Poppins', sans-serif; /* 设置Poppins字体 */
}

.custom-title {
  font-family: 'Poppins', sans-serif;
  font-size: 32px;
  font-weight: 700;
  color: #FF7043;
  margin-bottom: 20px;
  text-align: center;
}

.custom-content {
  font-family: 'Poppins', sans-serif; /* 设置Poppins字体 */
  font-size: 18px;
  color: #333;
  line-height: 1.8;
  text-align: left;
}

.custom-confirm-button {
  background-color: #FFB74D !important;
  color: white !important;
  font-weight: 600;
  border-radius: 10px;
  padding: 14px 28px;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
  transition: background-color 0.3s ease;
  display: block;
  margin: 20px auto 0;
  font-family: 'Poppins', sans-serif; /* 设置Poppins字体 */
}

.custom-confirm-button:hover {
  background-color: #FF9800 !important;
}

.custom-cancel-button {
  background-color: #FF7043 !important;
  color: white !important;
  font-weight: 600;
  border-radius: 10px;
  padding: 14px 28px;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
  transition: background-color 0.3s ease;
  display: block;
  margin: 20px auto 0;
  font-family: 'Poppins', sans-serif; /* 设置Poppins字体 */
}

.custom-cancel-button:hover {
  background-color: #FF5722 !important;
}

</style>


