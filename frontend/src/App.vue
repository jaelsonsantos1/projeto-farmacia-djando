<template>
  <div class="container">
    <Header />
    <SearchAreaVue />
  </div>
</template>

<script>
// import axios from 'axios';
import './css/style.css'
import Header from './components/Header.vue';
import SearchAreaVue from './components/SearchArea.vue';

export default {
  name: 'App',
  components: {
    Header,
    SearchAreaVue
  },
  data() {
    return {
      dados: [{"MedicamentoRegistro": "1781708900042", "MedicamentoPrincipioAtivo": "BUTILBROMETO DE ESCOPOLAMINA", "MedicamentoCnpj": "61.082.426/0002-07", "MedicamentoLaboratorio": "COSMED INDUSTRIA DE COSMETICOS E MEDICAMENTOS S.A.", "MedicamentoCodGgrem": 540921040046917, "MedicamentoEan1": "7896094921313", "MedicamentoEan2": "    -     ", "MedicamentoEan3": "    -     ", "MedicamentoProduto": "BUSCOPAN", "MedicamentoApresentacao": "20 MG SOL INJ CT 5 AMP VD TRANS X 1 ML", "MedicamentoClasseTerapeutica": "A3A - ANTIESPASM\u00d3DICOS E ANTICOLIN\u00c9RGICOS PUROS", "MedicamentoTipoProduto": "Novo", "MedicamentoRegimePreco": "Regulado", "MedicamentoPfSemImposto": 22.23, "MedicamentoPf0": 24.9, "MedicamentoPf12": 28.77, "MedicamentoPf17": 30.77, "MedicamentoPf17Alc": 26.79, "MedicamentoPf17Meio": 30.98, "MedicamentoPf17MeioAlc": 26.95, "MedicamentoPf18": 31.2, "MedicamentoPf18Alc": 27.11, "MedicamentoPf19": 31.65, "MedicamentoPf20": 32.11, "MedicamentoPf21": 32.58, "MedicamentoPf22": 33.06, "MedicamentoPmvgSemImposto": 17.44, "MedicamentoPmvg0": 19.54, "MedicamentoPmvg12": 22.58, "MedicamentoPfPmvg17": 24.15, "MedicamentoPmvg17Alc": 21.02, "MedicamentoPmvg17Meio": 24.31, "MedicamentoPmvg17MeioAlc": 21.15, "MedicamentoPmvg18": 24.48, "MedicamentoPmvg18Alc": 21.27, "MedicamentoPmvg19": 24.84, "MedicamentoPmvg20": 25.2, "MedicamentoPmvg21": 25.57, "MedicamentoPmvg22": 25.94, "MedicamentoRestricaoHospitalar": "N\u00e3o", "MedicamentoCap": "N\u00e3o", "MedicamentoComfaz87": "N\u00e3o", "MedicamentoIcms0": "N\u00e3o", "MedicamentoAnaliseRecursal": "(9)", "MedicamentoPisConfins": "Negativa", "MedicamentoComercializacao2022": "Sim", "MedicamentoTarja": "Tarja Vermelha (**)"}]
    }
  },
  mounted() {
    // console.log("App Criado!");
    // axios.get('http://127.0.0.1:8000/medicamento/')
    //   .then(response => {
    //     this.dados = response.data;
    //   })
    //   .catch(err => {
    //     console.log(err);
    //   })
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
