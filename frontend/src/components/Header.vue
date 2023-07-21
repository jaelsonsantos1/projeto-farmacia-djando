<template>
    <div class="header-container">
        <span>
            <a href="https://www.gov.br/anvisa/pt-br/assuntos/medicamentos/cmed/precos" target="_blank">
                Lista de preços de medicamentos
            </a>
        </span>
    </div>
</template>

<script>
export default {
    name: 'Header'
}
</script>

<style scoped>
.header-container {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    border-top: 1px solid var(--color-neutral-100);
    border-bottom: 1px solid var(--color-neutral-100);
}

.header-container span {
    font-size: 1.5rem;
    font-weight: 500;
    padding: 20px 0px;
}

.header-container span a:hover {
    text-decoration: underline;
}
.header-container span a {
    color: var(--link-color-grey-base);
    text-decoration: none;
    
}

</style>