import Vue from 'vue';
import Router from 'vue-router';
import Actors from '../components/Actors.vue';
import Ping from '../components/Ping.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Actors',
      component: Actors,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});
