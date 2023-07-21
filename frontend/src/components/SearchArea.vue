<template>
    <div class="containerArea">
        <div class="categoryArea">
            <!-- Area especifica para os filtros -->
            <div class="titleCategoryArea">
                <span class="textTitleCategoryArea">
                    Busca por categorias
                </span>
            </div>

            <div class="categoryFilters">
                <InputSelectFilterVue v-for="categorie in categoriesList" :key="categorie"
                    :options="categoriesList"
                    :title="categorie"
                    defaultValue="Selecione"
                />
            </div>
        </div>
        <div class="searchArea">
            <!-- Area onde mostra o campo de buscar pelo nome do produto -->
            Area com input buscar produto
        </div>
        <div class="resultsArea">
            <!-- Area onde aparecerá os resultados -->
            Area para visualizar resultados buscados
        </div>
    </div>
</template>

<script>
import InputSelectFilterVue from './InputSelectFilter.vue'

export default {
    name: "SearchArea",
    components: {
        InputSelectFilterVue
    },
    data() {
        return {
            categoriesValueList: [],
            categoriesList: []
        }
    }
}
</script>

<style scoped>
.containerArea {
  display: grid;
  max-width: 800px;
  margin: 0 auto;
  grid-template-columns: 1fr 2fr; /* Define a proporção das colunas: 1 parte para categoryArea e 2 partes para o resto */
  grid-template-rows: 1fr auto; /* Define a proporção das linhas: 1 parte para a altura total de categoryArea, auto para o resto */
  gap: 20px; /* Define o espaçamento entre as áreas */
  height: 100%;
  margin-top: 15px;
}

.categoryArea {
    grid-column: 1;
    grid-row: span 2;
    border: 1px solid var(--color-neutral-100);
    border-radius: 10px;
}

.categoryArea .titleCategoryArea {
    padding: 8px;
    background-color: #F9F9F9;
    border-radius: 10px 10px 0 0;
    text-align: center;
}
.categoryArea .titleCategoryArea .textTitleCategoryArea {
    font-size: 1.1em;
    font-weight: 500;
}

.categoryArea .categoryFilters {
    padding: 10px 5px;
}

.searchArea {
    grid-column: 2; /* Ocupa a segunda coluna */
    height: 80px;
    border: 1px solid var(--color-neutral-100);
    border-radius: 10px;
    text-align: center;
}

.resultsArea {
    grid-column: 2; /* Ocupa a segunda coluna */
    border: 1px solid var(--color-neutral-100);
    border-radius: 10px;
    text-align: center;
}

</style>