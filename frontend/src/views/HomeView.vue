<template>
  <div class="home">
    <div class="employee-row">
      <EmployeeComponent v-for="user in users" :key="user.id" :employee="user" />
    </div>
    <button class="add-button" @click="this.$refs.employeeModalRef.addEmployee()">
      Add
    </button>
    <div>
      <EmployeeModal ref="employeeModalRef" :employee="employee" />
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import EmployeeComponent from "@/components/EmployeeComponent.vue";
import EmployeeModal from "@/components/EmployeeModal.vue";
export default {
  name: "HomeView",
  computed: {
    ...mapGetters(["getEmployees"]),
    users() {
      return this.getEmployees;
    },
  },
  components: {
    EmployeeComponent,
    EmployeeModal,
  },
  methods: {
    ...mapActions(["addEmployee"]),
    addEmployee() {
      // Dispatch the action to add a new employee
      this.addEmployee(/* Provide necessary parameters for adding an employee */);
    },
  },
  mounted() {
    // Dispatch the action to fetch users when the component is mounted
    this.$store.dispatch("getEmployees");
  },
};
</script>

<style scoped>
.employee-row {
  display: flex;
  flex-wrap: wrap; /* Wrap to the next line if the space is not enough */
  gap: 10px; /* Adjust the gap between EmployeeComponents */
  justify-content: center; /* Center the items horizontally */
}

.add-button {
  position: fixed;
  top: 10px;
  right: 10px;
}
</style>
