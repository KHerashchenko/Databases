<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Movies</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm"
            v-b-modal.movie-modal>Add Movie</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">ID</th>
              <th scope="col">Name</th>
              <th scope="col">Year</th>
              <th scope="col">Genre</th>
              <th scope="col">Director ID</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(movie, index) in movies" :key="index">
              <td>{{ movie.id }}</td>
              <td>{{ movie.name }}</td>
              <td>{{ movie.year }}</td>
              <td>{{ movie.genre }}</td>
              <td>{{ movie.director_id }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.movie-update-modal
                          @click="editMovie(movie)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteMovie(movie)">
                      Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addMovieModal"
            id="movie-modal"
            title="Add a new movie"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-name-group"
                    label="Name:"
                    label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addMovieForm.name"
                        required
                        placeholder="Enter name">
          </b-form-input>
        </b-form-group>
      <b-form-group id="form-year-group"
                    label="Year:"
                    label-for="form-year-input">
          <b-form-input id="form-year-input"
                        type="text"
                        v-model="addMovieForm.year"
                        required
                        placeholder="Enter year">
          </b-form-input>
        </b-form-group>
      <b-form-group id="form-genre-group"
                    label="Genre:"
                    label-for="form-genre-input">
          <b-form-select v-model="addMovieForm.genre" :options="options"></b-form-select>
        </b-form-group>
      <b-form-group id="form-director-group"
                    label="Director ID:"
                    label-for="form-director-input">
          <b-form-input id="form-director-input"
                        type="text"
                        v-model="addMovieForm.director_id"
                        required
                        placeholder="Enter director ID">
          </b-form-input>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="editMovieModal"
            id="movie-update-modal"
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
      <b-form-group id="form-year-edit-group"
                    label="Year:"
                    label-for="form-year-edit-input">
          <b-form-input id="form-year-edit-input"
                        type="text"
                        v-model="editForm.year"
                        required
                        placeholder="Enter year">
          </b-form-input>
        </b-form-group>
      <b-form-group id="form-genre-edit-group"
                    label="Genre:"
                    label-for="form-genre-edit-input">
          <b-form-select v-model="editForm.genre" :options="options"></b-form-select>
        </b-form-group>
      <b-form-group id="form-director-edit-group"
                    label="Director ID:"
                    label-for="form-director-edit-input">
          <b-form-input id="form-director-edit-input"
                        type="text"
                        v-model="editForm.director_id"
                        required
                        placeholder="Enter director">
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
        { value: null, text: 'Please select a genre' },
        { value: 'drama', text: 'Drama' },
        { value: 'action', text: 'Action' },
        { value: 'comedy', text: 'Comedy' },
        { value: 'horror', text: 'Horror' },
      ],
      movies: [],
      addMovieForm: {
        name: '',
        genre: null,
        year: '',
        director_id: '',
      },
      message: '',
      showMessage: false,
      editForm: {
        id: '',
        name: '',
        genre: null,
        year: '',
        director_id: '',
      },
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getMovies() {
      const path = 'http://localhost:8000/api/movies';
      axios.get(path)
        .then((res) => {
          this.movies = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addMovie(payload) {
      const path = 'http://localhost:8000/api/movie';
      axios.post(path, payload)
        .then(() => {
          this.getMovies();
          this.message = 'movie added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.message = error;
          this.showMessage = true;
          this.getMovies();
        });
    },
    initForm() {
      this.addMovieForm.name = '';
      this.addMovieForm.genre = null;
      this.addMovieForm.year = '';
      this.addMovieForm.director_id = '';
      this.editForm.id = '';
      this.editForm.name = '';
      this.editForm.genre = null;
      this.editForm.year = '';
      this.editForm.director_id = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addMovieModal.hide();
      const payload = {
        name: this.addMovieForm.name,
        genre: this.addMovieForm.genre,
        year: this.addMovieForm.year,
        director_id: this.addMovieForm.director_id,
      };
      this.addMovie(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addMovieModal.hide();
      this.initForm();
    },
    editMovie(movie) {
      this.editForm = movie;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editMovieModal.hide();
      const payload = {
        id: this.editForm.id,
        name: this.editForm.name,
        genre: this.editForm.genre,
        year: this.editForm.year,
        director_id: this.editForm.director_id,
      };
      this.updateMovie(payload);
    },
    updateMovie(payload) {
      const path = 'http://localhost:8000/api/movie';
      axios.put(path, payload)
        .then(() => {
          this.getMovies();
          this.message = 'movie updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getMovies();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editMovieModal.hide();
      this.initForm();
      this.getMovies(); // why?
    },
    removeMovie(payload) {
      const path = 'http://localhost:8000/api/movie';

      axios.delete(path, { data: payload })
        .then(() => {
          this.getMovies();
          this.message = 'movie removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getMovies();
        });
    },
    onDeleteMovie(movie) {
      const payload = {
        id: movie.id,
      };
      this.removeMovie(payload);
    },
  },
  created() {
    this.getMovies();
  },
};
</script>
