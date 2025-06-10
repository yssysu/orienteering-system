<template>
  <div id="game-map" class="game-map-container">
    <h2 class="game-map-title">游戏地图</h2>
    <div id="map"></div> 
    <button @click="getTaskNearby" class="task-btn">获取任务</button> 
  </div>
</template>

<script>
import L from 'leaflet'; // 导入 Leaflet 地图库
import axios from 'axios'; // 导入 axios 用于发送 HTTP 请求
import { useStore } from 'vuex'; // 导入 vuex 状态管理

export default {
  name: 'GameMap',
  data() {
    return {
      map: null, // 存储地图实例
      nearbyTask: null // 存储附近任务
    };
  },
  mounted() {
    const store = useStore();
    const studentId = store.getters.getStudentId; // 获取当前学生 ID
    console.log('当前学生 ID:', studentId);

    try {
      this.initMap(); // 初始化地图
      this.getUserLocation(studentId); // 获取用户位置信息
      this.getTaskLocations(); // 获取任务地点
    } catch (error) {
      console.error('地图初始化或获取用户位置时出错:', error);
    }
  },
  methods: {
    // 初始化地图
    initMap() {
      try {
        // 创建 Leaflet 地图实例，设置初始视图和缩放级别
        this.map = L.map('map').setView([51.505, -0.09], 13);

        // 设置地图瓦片图层（使用 OpenStreetMap）
        L.tileLayer('https://tile-b.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
          maxZoom: 19
        }).addTo(this.map);
        L.Popup.prototype._animateZoom = function (e) {
          if (!this._map) {
            return;
          }
          var pos = this._map._latLngToNewLayerPoint(this._latlng, e.zoom, e.center),
            anchor = this._getAnchor();
          L.DomUtil.setPosition(this._container, pos.add(anchor));
        };
        console.log('地图已成功初始化');
      } catch (error) {
        console.error('地图初始化失败:', error);
      }
    },

    // 获取用户当前位置并发送到后端
    getUserLocation(studentId) {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          (position) => {
            const userLocation = {
              latitude: position.coords.latitude,
              longitude: position.coords.longitude
            };
            this.sendUserLocationToBackend(userLocation, studentId); // 发送用户位置到后端
            this.showUserLocationOnMap(userLocation); // 在地图上显示用户位置
          },
          (error) => {
            console.error('获取位置失败:', error);
          }
        );
      } else {
        console.error('浏览器不支持地理定位');
      }
    },

    // 在地图上显示用户位置
    showUserLocationOnMap(userLocation) {
      if (this.map) {
        try {
          // 在地图上添加标记，并弹出提示框
          const marker = L.marker([userLocation.latitude, userLocation.longitude]).addTo(this.map);
          marker.bindPopup('你的位置').openPopup();
          this.map.setView([userLocation.latitude, userLocation.longitude], 15); // 将地图视图居中
          console.log('用户位置已成功显示在地图上');
        } catch (error) {
          console.error('显示用户位置失败:', error);
        }
      } else {
        console.error('地图未初始化，无法显示用户位置');
      }
    },

    // 将用户位置信息发送到后端
    sendUserLocationToBackend(userLocation, studentId) {
      const data = {
        studentId: studentId,
        latitude: userLocation.latitude,
        longitude: userLocation.longitude
      };
      axios.post('http://127.0.0.1:8000/api/user_location/', data)
        .then(() => {
          console.log('用户位置已发送到后端');
        })
        .catch(error => {
          console.error('发送用户位置到后端失败:', error);
        });
    },

    // 获取任务地点并显示在地图上
    getTaskLocations() {
      axios.get('http://127.0.0.1:8000/api/task_locations/')
        .then(response => {
          const taskLocations = response.data; // 获取任务地点数据
          this.showTaskLocationsOnMap(taskLocations); // 在地图上显示任务地点
        })
        .catch(error => {
          console.error('获取任务地点失败:', error);
        });
    },

    // 在地图上显示任务地点
    showTaskLocationsOnMap(taskLocations) {
      if (this.map) {
        try {
          taskLocations.forEach((task, index) => {
            // 为每个任务地点添加标记，并绑定提示框
            const marker = L.marker([task.latitude, task.longitude]).addTo(this.map);
            marker.bindPopup(`任务 ${index + 1}: ${task.description}`).openPopup();
          });
          console.log('任务地点已成功显示在地图上');
        } catch (error) {
          console.error('显示任务地点失败:', error);
        }
      } else {
        console.error('地图未初始化，无法显示任务地点');
      }
    },

    // 获取附近任务并激活
    getTaskNearby() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          (position) => {
            const userLocation = {
              latitude: position.coords.latitude,
              longitude: position.coords.longitude
            };
            this.activateNearbyTask(userLocation); // 激活附近的任务
          },
          (error) => {
            console.error('获取位置失败:', error);
          }
        );
      } else {
        console.error('浏览器不支持地理定位');
      }
    },

    // 激活附近的任务
    activateNearbyTask(userLocation) {
      const store = this.$store;
      const studentId = store.getters.getStudentId; // 获取学生 ID
      const data = {
        studentId: studentId,
        latitude: userLocation.latitude,
        longitude: userLocation.longitude
      };
      axios.post('http://127.0.0.1:8000/api/activate_nearby_task/', data)
        .then(response => {
          console.log(response.data.message); // 输出服务器响应消息
          alert("任务已激活"); // 显示任务激活提示
        })
        .catch(error => {
          console.error('激活附近任务失败:', error);
        });
    }
  }
};
</script>

<style scoped>

.leaflet-container {
    height: 100vh;
    width: 100%;
}
/* 游戏地图容器样式 */
.game-map-container {
  padding: 20px;
  border-radius: 15px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 900px; 
  margin: 50px auto;
  background-color: rgba(239, 238, 238, 0.699); 
  border-radius: 15px; 
}

/* 标题样式 */
.game-map-title {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  text-align: center;
  margin-bottom: 20px; 
  font-family: 'Poppins', sans-serif;
}

/* 地图容器样式 */
#map {
  height: 450px; 
  width: 100%; 
  border-radius: 10px; 
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); 
}

/* 获取任务按钮样式 */
button.task-btn {
  background:linear-gradient(45deg, #ff5733, #ffbb33); 
  color: white;
  font-size: 16px;
  padding: 12px 25px;
  border: none;
  border-radius: 8px; 
  cursor: pointer;
  margin-top: 20px;
  width: 100%; /* 按钮宽度占满容器 */
  transition: background 0.3s, transform 0.3s; 
  font-family: 'Poppins', sans-serif;
}

/* 按钮悬停效果 */
button.task-btn:hover {
  background:linear-gradient(45deg, #ff4500, #ffa500); 
  transform: scale(1.05); 
}


button.task-btn:active {
  transform: scale(0.98); 
}

/* 按钮禁用状态 */
button.task-btn:disabled {
  background: #d3d3d3; 
  cursor: not-allowed; 
}

</style>
