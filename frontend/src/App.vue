<template>
  <div class="container">
    <Header />
    <SearchAreaVue
      :dados="dados"
      :tem-proxima-pagina="temProximaPagina"
      :ocupado="ocupado"
      :carregarMedicamentos="carregarMedicamentos"
    />
  </div>
</template>

<script>
import './css/style.css'
import Header from './components/Header.vue';
import SearchAreaVue from './components/SearchArea.vue';
import axios from 'axios';

export default {
  name: 'App',
  components: {
    Header,
    SearchAreaVue
  },
  data() {
    return {
      dados: [],
      pagina: 1,
      temProximaPagina: true,
      ocupado: false
    };
  },
  methods: {
    async carregarMedicamentos() {
      if(this.ocupado) return;
      this.ocupado = true;

      await axios.get(`http://127.0.0.1:8000/medicamentos/lista_medicamentos/?pagina=${this.pagina}`)
        .then(response => {
          console.log(response.data);
      })

              
      // this.dados.push(...data.medicamentos);
      // this.temProximaPagina = this.dados.tem_proxima_pagina;
      // this.pagina += 1;
      

      this.ocupado = false;
    }
  },
  mounted() {
    this.carregarMedicamentos();
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
}

.container {
  height: 100%;
}
</style>
