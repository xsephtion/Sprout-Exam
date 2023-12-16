import axios from "axios";

const state = {
  users: null,
  isAuthenticated: false,
};

const getters = {
  isAuthenticated: (state) => state.isAuthenticated,
  getEmployees: (state) => state.users,
};

const actions = {
  async logIn({ commit }, user) {
    try {
      // Assuming you get user data from the login response
      const { data } = await axios.post("login", user);
      commit("setAuthentication", true); // Assuming data contains user information
      return data ? true : false;
    } catch (error) {
      console.error("Error logging in:", error);
    }
  },
  async getEmployees({ commit }) {
    try {
      const { data } = await axios.get("employees");
      commit("setEmployees", data);
    } catch (error) {
      console.error("Error fetching users:", error);
    }
  },
  async addEmployee(_, user) {
    try {
      await axios.post("employees", user);
    } catch (error) {
      console.error("Error adding user:", error);
    }
  },
  async updateEmployee(_, user) {
    try {
      await axios.put(`employees/${user.id}`, user);
    } catch (error) {
      console.error("Error updating user:", error);
    }
  },
  async deleteEmployee(_, id) {
    try {
      const { data } = await axios.delete(`employees/${id}`);
      return data ? true : false;
    } catch (error) {
      console.error("Error deleting user:", error);
    }
  },
  async logOut({ commit }) {
    commit("setAuthentication", false);
  },
};

const mutations = {
  setAuthentication(state, status) {
    state.isAuthenticated = status;
  },
  setEmployees(state, users) {
    state.users = users;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
