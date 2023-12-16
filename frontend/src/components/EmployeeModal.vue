<template>
  <div>
    <Teleport to="body">
      <Transition name="modal-fade">
        <div
          class="modal-wrapper"
          v-if="showModal"
          aria-modal="true"
          role="dialog"
          tabindex="-1"
        >
          <div class="form-container">
            <div class="modal-header">
              <button class="close-button" @click="editEmployee">X</button>
            </div>
            <form @submit.prevent="saveChanges">
              <div class="form-group">
                <label for="first_name">First Name</label>
                <input
                  :disabled="isView"
                  v-model="editedEmployee.first_name"
                  type="text"
                  class="form-control"
                  id="first_name"
                  required
                />
              </div>
              <div class="form-group">
                <label for="last_name">Last Name</label>
                <input
                  :disabled="isView"
                  v-model="editedEmployee.last_name"
                  type="text"
                  class="form-control"
                  id="last_name"
                  required
                />
              </div>
              <div class="form-group">
                <label for="email">Email</label>
                <input
                  :disabled="isView"
                  v-model="editedEmployee.email"
                  type="email"
                  class="form-control"
                  id="email"
                  required
                />
              </div>
              <div class="form-group">
                <label for="employee_type">Employee Type</label>
                <select
                  :disabled="isView"
                  v-model="editedEmployee.employee_type"
                  class="form-control"
                  id="employee_type"
                  required
                >
                  <option value="regular">Regular</option>
                  <option value="contractual">Contractual</option>
                </select>
              </div>
              <div class="form-group">
                <label for="number_of_leaves">Number of Leaves</label>
                <input
                  :disabled="isView || editedEmployee.employee_type !== 'regular'"
                  v-model="editedEmployee.number_of_leaves"
                  type="number"
                  class="form-control"
                  id="number_of_leaves"
                />
              </div>
              <div class="form-group">
                <label for="benefits">Benefits</label>
                <input
                  :disabled="isView || editedEmployee.employee_type !== 'regular'"
                  v-model="editedEmployee.benefits"
                  type="text"
                  class="form-control"
                  id="benefits"
                />
              </div>
              <div class="form-group">
                <label for="contract_end_date">Contract End Date</label>
                <input
                  :disabled="isView || editedEmployee.employee_type === 'regular'"
                  v-model="editedEmployee.contract_end_date"
                  type="date"
                  class="form-control"
                  id="contract_end_date"
                />
              </div>
              <div class="form-group">
                <label for="project">Project</label>
                <input
                  :disabled="isView || editedEmployee.employee_type === 'regular'"
                  v-model="editedEmployee.project"
                  type="text"
                  class="form-control"
                  id="project"
                />
              </div>
              <button type="submit" class="btn btn-primary">Save Changes</button>
            </form>
          </div>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  props: {
    employee: Object,
  },
  data() {
    return {
      showModal: false,
      isView: false,
      isAdd: false,
      isModalVisible: false,
      editedEmployee: { ...this.employee },
    };
  },
  methods: {
    ...mapActions(["updateEmployee", "deleteEmployee", "addEmployee"]),
    addEmployee() {
      this.showModal = !this.showModal;
      this.isView = false;
      this.isAdd = true;
    },
    viewEmployee() {
      this.showModal = !this.showModal;
      this.isView = !this.isView;
    },
    editEmployee() {
      this.isView = false;
      this.showModal = !this.showModal;
    },
    async deleteEmployee({ id }) {
      const res = await this.deleteEmployee(id);
      if (res.message) {
        alert(res.message);
      }
      this.showModal = !this.showModal;
    },
    async saveChanges() {
      if (!this.isAdd) {
        this.updateEmployee(this.editedEmployee);
        this.showModal = !this.showModal;
      } else {
        await this.$store.dispatch("addEmployee", this.editedEmployee);
        this.showModal = !this.showModal;
      }
    },
    resetForm() {
      // Reset the form when the modal is hidden
      this.editedEmployee = { ...this.employee };
    },
  },
};
</script>

<style scoped>
.modal-actions {
  display: flex;
  justify-content: flex-end;
  margin-top: 20px;
}
.form-group {
  margin-bottom: 15px;
}
.form-container {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
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
