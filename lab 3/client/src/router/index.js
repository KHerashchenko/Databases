import Vue from 'vue';
import Router from 'vue-router';
import Actors from '../components/Actors.vue';
import Directors from '../components/Directors.vue';
import Movies from '../components/Movies.vue';
import Ping from '../components/Ping.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/actors',
      name: 'Actors',
      component: Actors,
    },
    {
      path: '/directors',
      name: 'Directors',
      component: Directors,
    },
    {
      path: '/movies',
      name: 'Movies',
      component: Movies,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});
