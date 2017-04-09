import Vue from 'vue';
import App from './App';
import router from './router';
import VueMaterial from 'vue-material';
import VeeValidate from 'vee-validate';
import 'vue-material/dist/vue-material.css';
import store from './store/store';
import GSignInButton from 'vue-google-signin-button'

Vue.use(GSignInButton)
Vue.use(VueMaterial);
Vue.use(VeeValidate);

Vue.material.registerTheme('default', {
  primary: 'blue',
  accent: 'red',
  warn: 'red',
  background: 'white'
})

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
