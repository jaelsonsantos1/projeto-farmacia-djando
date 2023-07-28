# projeto-farmacia-djando
Este é um projeto relacionado a um desafio Python+Vue para uma vaga de Programador Junior. Ainda estou trabalhando neste projeto, e qualquer 

### 🌱 Status: Em Desenvolvimento
O projeto encontra-se em fase de desenvolvimento e estou trabalhando para implementar todas as funcionalidades planejadas. Estou abertos a dicas, sugestões e melhorias para tornar o sistema mais eficiente e útil para o propósito da farmácia.

### 🎯 Objetivo do projeto
Este projeto consiste em desenvolver um sistema que permitirá que o proprietário de uma farmácia, monitore os preços de referência dos medicamentos. O sistema possibilitará consultas detalhadas dos preços por meio de diferentes filtros e disponibilizará a opção de exportar os resultados em formato xls. Abaixo estão as informações e requisitos do projeto:

### 📊 Fonte de Dados
Os dados de referência dos medicamentos serão obtidos a partir do PMVG (Preço de Medicamentos de Referência) em formato xls. A fonte desses dados é o site da Agência Nacional de Vigilância Sanitária (ANVISA):

PMVG - XLS da ANVISA

### 👨‍💻 Tecnologias Utilizadas
Para o desenvolvimento do sistema, serão utilizadas as seguintes tecnologias:

- Frontend
  - Vue.js

- Backend
  - Django Rest Framework
  - Banco de Dados
  - Postgres

## ⚙️ Configuração Inicial

Antes de executar o projeto, é necessário configurar as variáveis de ambiente necessárias. Para isso, siga os passos abaixo:

1. Renomeie o arquivo `.env-example` para apenas `.env` e abra o arquivo em um editor de texto:

   ```bash
   mv .env-example .env
   ```

2. Preencha as variáveis de ambiente no arquivo `.env` com as informações corretas:

   ```plaintext
   SECRET_KEY="sua-chave-secreta-aqui"
   DEBUG="1"
   ALLOWED_HOSTS="127.0.0.1,localhost"

   DB_ENGINE="django.db.backends.postgresql"
   POSTGRES_DB="seu-nome-db"
   POSTGRES_USER="seu-usuario-db"
   POSTGRES_PASSWORD="sua-senha-db"
   POSTGRES_HOST="host-do-banco-de-dados"
   POSTGRES_PORT="5432"

   PGADMIN_DEFAULT_EMAIL="seu-email-do-pgadmin"
   PGADMIN_DEFAULT_PASSWORD="sua-senha-do-pgadmin"
   PGADMIN_CONFIG_SERVER_MODE=False

   DEFAULT_FROM_EMAIL="sua-conta-de-email@example.com"
   EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
   EMAIL_HOST="seu-host-de-email"
   EMAIL_PORT=587
   EMAIL_HOST_USER="seu-usuario-de-email"
   EMAIL_HOST_PASSWORD="sua-senha-de-email"
   EMAIL_USE_TLS=True
   ```

   Certifique-se de substituir todas as informações entre aspas pelas configurações adequadas para o seu ambiente.

## 🕹️ Executando o Projeto

Após configurar as variáveis de ambiente, você pode prosseguir com as etapas para executar o projeto:

1. Clonar o projeto e entrar na pasta do projeto:

   ```bash
   git clone https://github.com/jaelsonsantos1/projeto-farmacia-djando.git
   cd projeto-farmacia-djando
   ```

2. Executar o Docker Compose para configurar o ambiente:

   ```bash
   docker-compose up --build
   ```

3. Acessar o shell do container do Django para executar a raspagem de dados:

   ```bash
   docker exec -it djangoapp sh
   python raspagem_dados.py
   ```

4. Iniciar o servidor do frontend:

   ```bash
   cd frontend
   npm run serve
   ```

Acesse a aplicação no seu navegador e utilize os recursos disponíveis para consultar os preços de referência dos medicamentos na farmácia. Lembre-se de proteger adequadamente o arquivo `.env` com as informações sensíveis e nunca compartilhá-lo em locais não autorizados.
