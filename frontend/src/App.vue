<template>
  <nav>
    <router-link :to="navLink">{{ navText }}</router-link> |
    <router-link to="/" @click="handleNavClick">{{ logoutText }}</router-link>
  </nav>
  <router-view />
</template>

<script>
import { mapGetters } from "vuex";
import { mapActions } from "vuex";

export default {
  computed: {
    ...mapGetters(["isAuthenticated"]),
    navLink() {
      return this.isAuthenticated ? "/home" : "/";
    },
    navText() {
      return this.isAuthenticated ? "Home" : "Login";
    },
    logoutText() {
      return this.isAuthenticated ? "Logout" : "";
    },
  },
  methods: {
    ...mapGetters(["isAuthenticated"]),
    ...mapActions(["logOut"]),
    handleNavClick() {
      if (this.isAuthenticated) {
        this.logOut();
      }
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
