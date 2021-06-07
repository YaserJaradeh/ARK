import Vue from "vue";
import App from "./App.vue";
import shell from "vue-shell";
import { Streamlit } from "streamlit-component-lib";

Vue.config.productionTip = false;
Vue.use(shell);
new Vue({
  render: h => h(App)
}).$mount("#app");

Streamlit.setComponentReady();

Streamlit.setFrameHeight(600);
