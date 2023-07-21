# projeto-farmacia-djando
Este é um projeto relacionado a um desafio Python+Vue para uma vaga de Programador Junior.



## Configuração inicial
Clonar o projeto
```
git clone https://github.com/jaelsonsantos1/projeto-farmacia-djando.git
cd myproject
```
Criar o container docker e instalar as imagens necessárias
```
docker-compose up --build
```
Entrar no shell do docker para execultar a raspagem de dados
```
docker exec -it djangoapp sh
```
Rodando a raspagem de dados
```
python raspagem_dados.py
```
Subir o servidor do frontend
```
cd frontend
npm run serve
```
