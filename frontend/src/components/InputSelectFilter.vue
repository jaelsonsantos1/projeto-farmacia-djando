<template>
    <div class="areaInput">
        <span>{{ title }}</span>
        <select name="" id="">
            <option value="" selected>{{ defaultValue }}</option>
            <option
                v-for="option in options" :key="option"
                :value="option">
                {{ option }}
            </option>
        </select>
    </div>
</template>

<script>
export default {
    name: 'InputSelectFilter',
    props: {
        options: Array,
        title: String,
        defaultValue: String
    }
}
</script>

<style scoped>
.areaInput, span, select {
    width: 100%;
    margin: 5px 0;
}

.areaInput span {
    text-align: start;
    font-size: .7rem;
    font-weight: 600;
    color: var(--link-color-grey-base);
}

select {

    /* Defina a altura do select */
    height: 30px;

    /* Defina a cor do texto */
    color: #333;

    /* Defina a cor do fundo */
    background-color: #f2f2f2;

    /* Adicione uma borda */
    border: 1px solid #ccc;

    /* Adicione um espaçamento interno para o texto */
    padding: 5px;

    /* Adicione uma margem para separá-lo de outros elementos */
    margin: 10px 0;
}

/* Estilo para quando o usuário passa o mouse sobre o select */
select:hover {
    border-color: #999;
}

/* Estilo para quando o select está focado (quando o usuário clica nele) */
select:focus {
    outline: none;
    border-color: #007bff;
    box-shadow: 0 0 5px #007bff;
}

/* Estilo para as setas do dropdown */
select::-ms-expand {
    display: none; /* Remove a seta do Internet Explorer */
}

/* Estilo para o texto exibido no select */
select option {
    color: #333;
}
</style>