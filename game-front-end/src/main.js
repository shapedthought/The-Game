import { createApp } from 'vue';
import App from './App.vue';
import {createRouter, createWebHistory} from 'vue-router';
import Buzzer from './components/buzzer/Buzzer.vue';
import Admin from './components/admin/Admin.vue';

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {path: '/', component: Buzzer},
        {path: '/admin', component: Admin},
    ]
})

const app = createApp(App)

app.use(router)

app.mount('#app')
