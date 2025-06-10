<template>
  <header> <!-- 添加 header 包裹导航栏 -->
    <nav>
      <ul>
        <li>
          <router-link to="/game-map">
            <img src="@/assets/地图.svg" alt="游戏地图" class="nav-icon" />
            游戏地图
          </router-link>
        </li>
        <li>
          <router-link to="/task-list">
            <img src="@/assets/卷轴.png" alt="任务列表" class="nav-icon" />
            任务列表
          </router-link>
        </li>
        <li>
          <router-link to="/game-guide">
            <img src="@/assets/游戏说明.svg" alt="游戏说明" class="nav-icon" />
            游戏说明
          </router-link>
        </li>
        <li>
          <router-link to="/activate-game">
            <img src="@/assets/帮助.svg" alt="帮助" class="nav-icon" />
            帮助
          </router-link>
        </li>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'NavigationBar'
};
</script>

<style scoped>
/* 使所有元素的宽度计算包括内边距和边框 */
*,
*::before,
*::after {
  box-sizing: border-box;
}

/* 设置 header 样式 */
header {
  background: linear-gradient(45deg, #ff6f61, #f1c40f); 
  color: white; 
  padding: 15px 0; 
  border-radius: 0; 
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3), 0 4px 8px rgba(0, 0, 0, 0.2); 
  display: flex; 
  justify-content: center; 
  align-items: center; 
  transition: box-shadow 0.3s ease; 
  margin: 0; 
  margin-bottom: 10px;
  width: 100%;
}

/* header hover 样式 */
header:hover {
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.4), 0 6px 12px rgba(0, 0, 0, 0.3); 
}

/* 设置导航栏样式 */
nav ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
  display: flex; 
  flex-wrap: wrap; 
  justify-content: center; 
}

nav ul li {
  margin-right: 80px; 
  display: flex;
  align-items: center;
}

nav ul li a {
  text-decoration: none; 
  color: white;
  font-weight: bold;
  font-size: 18px; 
  letter-spacing: 1px; 
  position: relative; 
  transition: color 0.3s, transform 0.3s ease-in-out; 
  font-family: 'Poppins', sans-serif; 
}

nav ul li a:hover {
  color: #ffd700; 
  transform: translateY(-3px);
}

/* 设置图标样式 */
.nav-icon {
  width: 25px;
  height: 25px;
  margin-right: 10px; 
  vertical-align: middle;
}

/* 设置 main 内容区的样式 */
main {
  margin-top: 20px; 
  padding: 20px; 
}
</style>
