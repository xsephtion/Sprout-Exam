<template>
  <div class="employee-box">
    <div class="employee-name">{{ employee.first_name }} {{ employee.last_name }}</div>
    <div class="employee-actions">
      <button @click="this.$refs.employeeModalRef.viewEmployee()">VIEW</button>
      <button @click="this.$refs.employeeModalRef.editEmployee()">EDIT</button>
      <button @click="this.$refs.employeeModalRef.deleteEmployee()">DELETE</button>
    </div>
  </div>
  <div>
    <EmployeeModal ref="employeeModalRef" :employee="employee" />
  </div>
</template>

<script>
import EmployeeModal from "@/components/EmployeeModal.vue";
import { mapActions } from "vuex";
export default {
  name: "EmployeeComponent",
  components: {
    EmployeeModal,
  },
  data() {
    return {
      showModal: false,
      isView: false,
    };
  },
  props: {
    employee: {
      type: Object,
      required: true,
      default: () => ({
        id: "",
        first_name: "",
        last_name: "",
        email: "",
        employee_type: "",
        number_of_leaves: null,
        benefits: null,
        contract_end_date: null,
        project: null,
      }),
    },
  },
  methods: {
    ...mapActions(["deleteEmployee", "addEmployee"]),
    addEmployee() {
      this.showModal = !this.showModal;
      this.isView = false;
    },
  },
};
</script>

<style scoped>
.employee-box {
  border: 1px solid black;
  padding: 10px;
  width: 300px;
}

.employee-name {
  font-weight: bold;
  margin-bottom: 10px;
}

.employee-actions {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}
.modal-wrapper {
  position: fixed;
  left: 0;
  top: 0;

  z-index: 500;

  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.2);

  display: grid;
  place-items: center;
}

.modal-fade-enter-from,
.modal-fade-leave-to {
  opacity: 0;
}

.modal-fade-enter-active,
.modal-fade-leave-active {
  transition: 0.25s ease all;
}
.form-container {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.modal-header {
  top: 10px;
  right: 10px;
  justify-content: flex-end;
}

.close-button {
  background: none;
  border: none;
  font-size: 16px;
  cursor: pointer;
}
</style>
