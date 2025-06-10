<template>
  <div id="game-container">
    <canvas id="gameCanvas" class="canvas"></canvas>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'TaskGame2',
  props: ['taskNumber'],
  data() {
    return {
      randomParam: Math.random().toString(36).substring(7), 
      studentId: null
    };
  },
  computed: {
    gameUrl() {
      if (!this.studentId) {
        return '/game-error.html?error=studentId_missing';
      }
      return `/game.html?studentId=${this.studentId}&refresh=${this.randomParam}`;
    }
  },
  mounted() {
  this.fetchStudentId(); 
  this.showGameInstructions();  // 显示游戏说明
},

  methods: {
    
    showGameInstructions() {
    const modal = document.createElement('div');
    modal.id = 'gameInstructions';
    modal.style.position = 'fixed';
    modal.style.top = '0';
    modal.style.left = '0';
    modal.style.width = '100vw';
    modal.style.height = '100vh';
    modal.style.backgroundColor = 'rgba(0, 0, 0, 0.6)';
    modal.style.display = 'flex';
    modal.style.flexDirection = 'column';
    modal.style.justifyContent = 'center';
    modal.style.alignItems = 'center';
   modal.style.color = '#fff';
    modal.style.fontFamily = 'Arial, sans-serif';
    modal.style.fontSize = '18px';
    modal.style.zIndex = '9999';
    modal.style.overflow = 'hidden';

    modal.innerHTML = `
      <div style="text-align: center; max-width: 500px; padding: 30px; background-color: rgba(0, 0, 0, 0.85); border-radius: 15px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.6);">
        <h2 style="font-size: 24px; margin-bottom: 20px; color: #ffcc00;">游戏说明</h2>
        <p style="line-height: 1.6; margin-bottom: 20px;">欢迎来到我们的游戏！在游戏中，你将控制一个方块，避开朝你而来的方块并消灭它们。</p>
        <p style="line-height: 1.6; margin-bottom: 20px;">点击“开始游戏”按钮，开始游戏！</p>
        <button id="startGameBtn" style="
          padding: 15px 30px; 
          background-color: #4CAF50; 
          border: none; 
          border-radius: 8px; 
          color: white; 
          font-size: 18px; 
          cursor: pointer;
          transition: all 0.3s ease;
        ">开始游戏</button>
      </div>
    `;

    // 将弹窗添加到页面
    document.body.appendChild(modal);

    // 给开始游戏按钮绑定点击事件
    const startGameBtn = document.getElementById('startGameBtn');
    startGameBtn.addEventListener('click', () => {
      document.body.removeChild(modal); // 移除弹窗
      this.initGame();  // 初始化游戏
    });
  },

    fetchStudentId() {
      const urlParams = new URLSearchParams(window.location.search);
      const studentId = urlParams.get('studentId');
      if (!studentId) {
        console.error('URL 参数中缺少 studentId');
        alert('无法加载任务：缺少用户 ID，请检查 URL 参数！');
      }
      this.studentId = studentId;
    },

    initGame() {
      const canvas = document.getElementById('gameCanvas');
      const context = canvas.getContext('2d');

      const resizeCanvas = () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
      };
      resizeCanvas();
      window.addEventListener('resize', resizeCanvas);

      const player = {
        x: canvas.width / 2 - 15,
        y: canvas.height - 60,
        width: 30,
        height: 30,
        speed: 5,
        bullets: []
      };

      const enemies = [];
      let score = 0;
      let gameOver = false;

      const drawPlayer = () => {
        context.fillStyle = 'blue';
        context.fillRect(player.x, player.y, player.width, player.height);
      };

      const drawBullets = () => {
        context.fillStyle = 'red';
        player.bullets.forEach((bullet, index) => {
          context.fillRect(bullet.x, bullet.y, bullet.width, bullet.height);
          bullet.y -= bullet.speed;
          if (bullet.y < 0) {
            player.bullets.splice(index, 1);
          }
        });
      };

      const drawEnemies = () => {
        context.fillStyle = 'green';
        enemies.forEach((enemy) => {
          context.fillRect(enemy.x, enemy.y, enemy.width, enemy.height);
          enemy.y += enemy.speed;
          if (enemy.y > canvas.height) {
            gameOver = true;
            alert('很遗憾，任务失败了');
            this.$router.push('/task-list');
          }
        });
      };

      const drawScore = () => {
        context.fillStyle = 'white';
        context.font = '16px Arial';
        context.fillText(`Score: ${score}`, canvas.width - 80, 20);
      };

      const createEnemy = () => {
        const x = Math.random() * (canvas.width - 30);
        const y = -30;
        const width = 30;
        const height = 30;
        const speed = 2 + score * 0.1;
        enemies.push({ x, y, width, height, speed });
      };

      const handleCollisions = () => {
        player.bullets.forEach((bullet, bulletIndex) => {
          enemies.forEach((enemy, enemyIndex) => {
            if (
              bullet.x < enemy.x + enemy.width &&
              bullet.x + bullet.width > enemy.x &&
              bullet.y < enemy.y + enemy.height &&
              bullet.y + bullet.height > enemy.y
            ) {
              player.bullets.splice(bulletIndex, 1);
              enemies.splice(enemyIndex, 1);
              score += 1;
              if (score >= 10) {
                gameOver = true;
                alert('恭喜你，任务完成了！');
                this.updateTaskStatus(true);
              }
            }
          });
        });
      };

      const update = () => {
        handleCollisions();
      };

      const draw = () => {
        const gradient = context.createLinearGradient(0, 0, 0, canvas.height);
        gradient.addColorStop(0, '#142760');
        gradient.addColorStop(1, '#0a1a33');
        context.fillStyle = gradient;
        context.fillRect(0, 0, canvas.width, canvas.height);

        drawPlayer();
        drawBullets();
        drawEnemies();
        drawScore();
      };

      const gameLoop = () => {
        if (!gameOver) {
          update();
          draw();
          requestAnimationFrame(gameLoop);
        }
      };

      const handleMove = (event) => {
        const rect = canvas.getBoundingClientRect();
        const mouseX = (event.clientX || event.touches[0].clientX) - rect.left;
        player.x = mouseX - player.width / 2;
      };

      canvas.addEventListener('mousemove', handleMove);
      canvas.addEventListener('touchmove', handleMove);
      canvas.addEventListener('touchstart', handleMove);

      setInterval(() => {
        player.bullets.push({
          x: player.x + player.width / 2 - 2.5,
          y: player.y,
          width: 5,
          height: 10,
          speed: 5
        });
      }, 200);

      setInterval(createEnemy, 1000);
      gameLoop();
    },

    updateTaskStatus(isTaskCompleted) {
      const data = {
        studentId: this.studentId,
        taskId: 3, 
        isCompleted: isTaskCompleted 
      };

      console.log('Request Data:', data);

      axios.post('http://127.0.0.1:8000/api/submit_task_answer/', data)
        .then(response => {
          console.log('Response:', response);  
          this.$router.push('/task-list');
        })
        .catch(error => {
          console.error('更新任务状态失败:', error.response ? error.response.data : error);
        });
    }
  }
};
</script>

<style scoped>
html, body {
  margin: 0;
  padding: 0;
  height: 100%;
  overflow: hidden;
}

#gameInstructions {
  z-index: 9999; /* 确保弹窗显示在最上层 */
}

#game-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
  position: relative; /* 确保画布背景不覆盖弹窗 */
}

</style>
