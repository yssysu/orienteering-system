<template>
  <div>
    <!-- 如果没有输入学号，只显示 PlayerInfo 组件 -->
    <PlayerInfo v-if="!isLoggedIn" @loggedIn="onLoggedIn" />
    <!-- 如果输入了学号，显示导航和其他组件 -->
    <div v-else>
      <NavigationBar />
      <router-view />
    </div>
  </div>
</template>

<script>
import PlayerInfo from './components/PlayerInfo.vue';
import NavigationBar from './components/NavigationBar.vue';

export default {
  components: {
    PlayerInfo,
    NavigationBar
  },
  data() {
    return {
      isLoggedIn: false
    };
  },
  methods: {
    onLoggedIn() {
      this.isLoggedIn = true;
    }
  }
};
</script>
