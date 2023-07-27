import { createApp } from 'vue';
import App from './App.vue';
import InfiniteScroll from 'vue-infinite-scroll';

const app = createApp(App);
app.use(InfiniteScroll);

app.mount('#app');
