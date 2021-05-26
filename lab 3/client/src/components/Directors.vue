<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Directors</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm"
            v-b-modal.director-modal>Add Director</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">ID</th>
              <th scope="col">Name</th>
              <th scope="col">Gender</th>
              <th scope="col">Date of birth</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(director, index) in directors" :key="index">
              <td>{{ director.id }}</td>
              <td>{{ director.name }}</td>
              <td>{{ director.gender }}</td>
              <td>{{ director.date_of_birth }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.director-update-modal
                          @click="editDirector(director)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteDirector(director)">
                      Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addDirectorModal"
            id="director-modal"
            title="Add a new director"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-name-group"
                    label="Name:"
                    label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addDirectorForm.name"
                        required
                        placeholder="Enter name">
          </b-form-input>
        </b-form-group>

      <b-form-group id="form-gender-group"
                    label="Gender:"
                    label-for="form-gender-input">
          <b-form-select v-model="addDirectorForm.gender" :options="options"></b-form-select>

        </b-form-group>
      <b-form-group id="form-date-group"
                    label="Date of birth:"
                    label-for="form-date-input">
          <b-form-input id="form-date-input"
                        type="date"
                        v-model="addDirectorForm.date_of_birth"
                        required
                        placeholder="DD.MM.YYYY">
          </b-form-input>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="editDirectorModal"
            id="director-update-modal"
            title="Update"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-name-edit-group"
                    label="ID:"
                    label-for="form-id-edit-input">
          <b-form-input id="form-id-edit-input"
                        type="text"
                        v-model="editForm.id"
                        required
                        placeholder="Enter ID">
          </b-form-input>
        </b-form-group>
      <b-form-group id="form-name-edit-group"
                    label="Name:"
                    label-for="form-name-edit-input">
          <b-form-input id="form-name-edit-input"
                        type="text"
                        v-model="editForm.name"
                        required
                        placeholder="Enter name">
          </b-form-input>
        </b-form-group>
      <b-form-group id="form-gender-edit-group"
                    label="Gender:"
                    label-for="form-gender-edit-input">
          <b-form-select v-model="editForm.gender" :options="options"></b-form-select>
        </b-form-group>
      <b-form-group id="form-date-edit-group"
                    label="Date of birth:"
                    label-for="form-date-edit-input">
          <b-form-input id="form-name-date-input"
                        type="date"
                        v-model="editForm.date_of_birth"
                        required
                        placeholder="DD.MM.YYYY">
          </b-form-input>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      options: [
        { value: null, text: 'Please select a gender' },
        { value: 'male', text: 'Male' },
        { value: 'female', text: 'Female' },
      ],
      directors: [],
      addDirectorForm: {
        name: '',
        gender: null,
        date_of_birth: '',
      },
      message: '',
      showMessage: false,
      editForm: {
        id: '',
        name: '',
        gender: '',
        date_of_birth: '',
      },
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getDirectors() {
      const path = 'http://localhost:8000/api/directors';
      axios.get(path)
        .then((res) => {
          this.directors = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addDirector(payload) {
      const path = 'http://localhost:8000/api/director';
      axios.post(path, payload)
        .then(() => {
          this.getDirectors();
          this.message = 'director added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.message = error;
          this.showMessage = true;
          this.getDirectors();
        });
    },
    initForm() {
      this.addDirectorForm.name = '';
      this.addDirectorForm.gender = null;
      this.addDirectorForm.date_of_birth = '';
      this.editForm.id = '';
      this.editForm.name = '';
      this.editForm.gender = null;
      this.editForm.date_of_birth = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addDirectorModal.hide();
      const payload = {
        name: this.addDirectorForm.name,
        gender: this.addDirectorForm.gender,
        date_of_birth: this.addDirectorForm.date_of_birth,
      };
      this.addDirector(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addDirectorModal.hide();
      this.initForm();
    },
    editDirector(director) {
      this.editForm = director;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editDirectorModal.hide();
      const payload = {
        id: this.editForm.id,
        name: this.editForm.name,
        gender: this.editForm.gender,
        date_of_birth: this.editForm.date_of_birth,
      };
      this.updateDirector(payload);
    },
    updateDirector(payload) {
      const path = 'http://localhost:8000/api/director';
      axios.put(path, payload)
        .then(() => {
          this.getDirectors();
          this.message = 'director updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getDirectors();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editDirectorModal.hide();
      this.initForm();
      this.getDirectors(); // why?
    },
    removeDirector(payload) {
      const path = 'http://localhost:8000/api/director';

      axios.delete(path, { data: payload })
        .then(() => {
          this.getDirectors();
          this.message = 'director removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getDirectors();
        });
    },
    onDeleteDirector(director) {
      const payload = {
        id: director.id,
      };
      this.removeDirector(payload);
    },
  },
  created() {
    this.getDirectors();
  },
};
</script>
