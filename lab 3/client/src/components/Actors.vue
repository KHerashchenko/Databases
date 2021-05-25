<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Actors</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm"
            v-b-modal.actor-modal>Add Actor</button>
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
            <tr v-for="(actor, index) in actors" :key="index">
              <td>{{ actor.id }}</td>
              <td>{{ actor.name }}</td>
              <td>{{ actor.gender }}</td>
              <td>{{ actor.date_of_birth }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.actor-update-modal
                          @click="editActor(actor)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteActor(actor)">
                      Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addActorModal"
            id="actor-modal"
            title="Add a new actor"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-name-group"
                    label="Name:"
                    label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addActorForm.name"
                        required
                        placeholder="Enter name">
          </b-form-input>
        </b-form-group>

      <b-form-group id="form-gender-group"
                    label="Gender:"
                    label-for="form-gender-input">
          <b-form-input id="form-gender-input"
                        type="text"
                        v-model="addActorForm.gender"
                        required
                        placeholder="Enter gender">
          </b-form-input>
        </b-form-group>
      <b-form-group id="form-date-group"
                    label="Date of birth:"
                    label-for="form-date-input">
          <b-form-input id="form-date-input"
                        type="text"
                        v-model="addActorForm.date_of_birth"
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
    <b-modal ref="editActorModal"
            id="actor-update-modal"
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
          <b-form-input id="form-gender-edit-input"
                        type="text"
                        v-model="editForm.gender"
                        required
                        placeholder="Enter gender">
          </b-form-input>
        </b-form-group>
      <b-form-group id="form-date-edit-group"
                    label="Date of birth:"
                    label-for="form-date-edit-input">
          <b-form-input id="form-name-date-input"
                        type="text"
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
      actors: [],
      addActorForm: {
        name: '',
        gender: '',
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
    getActors() {
      const path = 'http://localhost:8000/api/actors';
      axios.get(path)
        .then((res) => {
          this.actors = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addActor(payload) {
      const path = 'http://localhost:8000/api/actor';
      axios.post(path, payload)
        .then(() => {
          this.getActors();
          this.message = 'actor added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.message = error;
          this.showMessage = true;
          this.getActors();
        });
    },
    initForm() {
      this.addActorForm.name = '';
      this.addActorForm.gender = '';
      this.addActorForm.date_of_birth = '';
      this.editForm.id = '';
      this.editForm.title = '';
      this.editForm.author = '';
      this.editForm.read = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addActorModal.hide();
      const payload = {
        name: this.addActorForm.name,
        gender: this.addActorForm.gender,
        date_of_birth: this.addActorForm.date_of_birth,
      };
      this.addActor(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addActorModal.hide();
      this.initForm();
    },
    editActor(actor) {
      this.editForm = actor;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editActorModal.hide();
      const payload = {
        id: this.editForm.id,
        name: this.editForm.name,
        gender: this.editForm.gender,
        date_of_birth: this.editForm.date_of_birth,
      };
      this.updateActor(payload);
    },
    updateActor(payload) {
      const path = 'http://localhost:8000/actor';
      axios.put(path, payload)
        .then(() => {
          this.getActors();
          this.message = 'actor updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getActors();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editActorModal.hide();
      this.initForm();
      this.getActors(); // why?
    },
    removeActor(payload) {
      const path = 'http://localhost:8000/actor/';
      axios.delete(path, payload)
        .then(() => {
          this.getActors();
          this.message = 'actor removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getActors();
        });
    },
    onDeleteActor(actor) {
      const payload = {
          id: actor.id,
        };
      this.removeActor(payload);
    },
  },
  created() {
    this.getActors();
  },
};
</script>
