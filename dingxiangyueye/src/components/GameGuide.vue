<template>
  <div class="game-guide-container">
    <div class="game-guide">
      <h1>游戏说明</h1>
      <p>欢迎来到我们的定向越野游戏！这里是游戏说明页面，您将在这里找到关于游戏的规则、玩法和技巧。</p>

      <h2>游戏规则</h2>
      <ul>
        <li>规则 1: 玩家需要到达任务的指定地点获取任务</li>
        <li>规则 2: 任务位于中山大学东校园内。</li>
        
      </ul>

      <h2>玩法简介</h2>
      <p>玩家将通过各种任务探索游戏地图，并最终成为游戏的胜利者！</p>

      <!-- 居中按钮 -->
      <div class="btn-container">
        <button @click="goToGameMap" class="btn-go-register">我已知晓游戏规则</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "GameGuide",
  methods: {
    goToGameMap() {
    
      this.$router.push('/game-map');    
    }
  }
};
</script>

<style scoped>
.game-guide-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-image: url('@/assets/th.jpg'); 
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  position: relative;
}

.game-guide-container::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5); /* 设置半透明黑色遮罩，使文字更加清晰 */
  z-index: 0;
}

.game-guide {
  background-color: #ffffff;
  border-radius: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1), 0 4px 16px rgba(0, 0, 0, 0.1);
  padding: 30px;
  max-width: 800px;
  width: 100%;
  font-family: 'Arial', sans-serif;
  text-align: left;
  line-height: 1.6;
  position: relative;
  z-index: 1;
}

.game-guide h1 {
  font-size: 2.5rem;
  color: #ff5722;
  margin-bottom: 15px;
  text-align: center;
  font-weight: bold;
}

.game-guide h2 {
  font-size: 1.8rem;
  color: #ff5722;
  margin-top: 20px;
  font-weight: bold;
}

.game-guide ul {
  list-style-type: disc;
  margin-left: 20px;
}

.game-guide p {
  font-size: 1.1rem;
  color: #333;
  margin-top: 10px;
  line-height: 1.8;
}

/* 按钮容器的样式，确保按钮居中 */
.btn-container {
  display: flex;
  justify-content: center; /* 水平居中 */
  margin-top: 30px;
}

/* 新增按钮样式 */
.btn-go-register {
  background-color: #ff5722; /* 按钮颜色调整为与标题一致 */
  color: white;
  padding: 12px 30px;
  border-radius: 8px;
  font-size: 1.2rem;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
  text-align: center;
}

.btn-go-register:hover {
  background-color: #e64a19; /* 按钮悬停颜色 */
}
</style>
