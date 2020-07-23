import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
// import G2 from '@antv/g2'
// import axios from './util/axios'
import 'element-ui/lib/theme-chalk/index.css'
// import 'lib-flexible'
import './css/global.css'

// Vue.prototype.$ajax = axios
Vue.config.productionTip = false
Vue.use(ElementUI)
// Vue.use(G2)

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
