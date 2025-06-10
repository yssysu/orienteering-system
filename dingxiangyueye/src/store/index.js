// src/store/index.js
import { createStore } from 'vuex';

const store = createStore({
  state: {
    studentId: '' // 用于存储学生 ID 的共享状态
  },
  mutations: {
    setStudentId(state, studentId) {
      state.studentId = studentId;
    }
  },
  actions: {
    setStudentId({ commit }, studentId) {
      commit('setStudentId', studentId);
    }
  },
  getters: {
    getStudentId: state => state.studentId
  }
});

export default store;