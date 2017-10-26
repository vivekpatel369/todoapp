import Vue from 'vue'
import App from './App.vue'
import Vuetify from 'vuetify'
import router from '@/router'
import axios from 'axios'
import Toasted from 'vue-toasted';
import './../node_modules/vuetify/dist/vuetify.min.css'
import './../node_modules/vue-multiselect/dist/vue-multiselect.min.css'


var toasted_options = {
  duration : 6000 // 6 sec
}

var VueScrollTo = require('vue-scrollto');
Vue.use(Vuetify)
Vue.use(VueScrollTo)
Vue.use(Toasted, toasted_options)

new Vue({
  el: '#app',
  router,
  render: h => h(App),
})
