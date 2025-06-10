import { createApp } from 'vue';
import App from './App.vue';
import { createRouter, createWebHistory } from 'vue-router'; // 修改导入路径
import GameMap from './components/GameMap.vue';
import TaskList from './components/TaskList.vue';
import PlayerInfo from './components/PlayerInfo.vue';
import GameGuide from './components/GameGuide.vue';
import PlayInfoDetails from './components/PlayInfoDetails.vue';
import ActivateGame from './components/ActivateGame.vue';
import store from './store'; // 引入 Vuex store

// 引入游戏
import GameOne from './components/GameOne.vue';
import GameTwo from './components/GameTwo.vue';
import GameThree from './components/GameThree.vue';
import GameFour from './components/GameFour.vue';

const routes = [
  // 修正路径
  { path: '/', redirect: '/game-guide'},
  { path: '/game-map', component: GameMap },
  { path: '/task-list', component: TaskList },
  { path: '/player-info', component: PlayerInfo },
  { path: '/game-guide', component: GameGuide },
  { path: '/playinfo-details', component: PlayInfoDetails },
  // 添加的游戏
  { path: '/game-task/:taskNumber',name:'GameTwo', component: GameTwo,props: true },
  { path: '/game-task/:taskNumber', name: 'GameOne', component: GameOne, props: true },
  { path : '/game-task/:taskNumber', name :'GameThree', component: GameThree,props : true},
  { path : '/game-task/:taskNumber', name :'GameFour', component: GameFour,props : true},
  { path: '/activate-game', component: ActivateGame}
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

const app = createApp(App);
app.use(store); 
app.use(router);
app.mount('#app');