import { defineStore } from "pinia";

// Read Pinia docs here: https://pinia.vuejs.org/
export const useAuthStore = defineStore("authStore", {
  state: () => ({
    someData: {}
  }),
  getters: {},
  actions: {}
});
