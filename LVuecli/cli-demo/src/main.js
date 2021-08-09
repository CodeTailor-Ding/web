import {createApp} from 'vue'
import App from './App.vue'
import { DatePicker } from 'ant-design-vue'
import 'ant-design-vue/dist/antd.css'

const globalApp = createApp(App)
globalApp.use(DatePicker)
globalApp.mount('#app')

// createApp(App).mount('#app')
