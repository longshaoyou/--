import App from "./App.vue";
import {
  Button,
  Message,
  Form,
  FormItem,
  Input,
} from "element-ui";
// fade/zoom 等
import "element-ui/lib/theme-chalk/base.css";
// collapse 展开折叠
import Vue from "vue";
Vue.config.productionTip = false;
Vue.prototype.$message = Message;
Vue.component(Button.name, Button);
Vue.component(Input.name, Input);
Vue.component(Form.name, Form);
Vue.component(FormItem.name, FormItem);
new Vue({
  render: (h) => h(App),
  mounted() {},
}).$mount("#app");