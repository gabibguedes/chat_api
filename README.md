# Chat API

## Suba a api:
```
docker-compose up
```
Após o comando a api estará rodando em `localhost:8000`

## Crie um super usuário:
Após subir o docker, entre no container da api com o comando:

```
docker exec -it chat_api bash
```

Dentro da container execute o comando:

```
python manage.py createsuperuser
```

E preencha os campos exigidos.

## Migrações:
As migrações são feitas ao subir o docker da api, mas caso seja necessário fazê-las novamente, siga os comandos:

```
python manage.py makemigrations
python manage.py migrate
```

Dependendo das alterações feitas, é possivel que ao fazer as migrações tenha algum conflito no banco de dados pelas tabelas que já foram criadas, caso isso ocorra, rode o comando abaixo para **apagar o banco**, e todos os outros volumes criados por esse repositório:

```
docker-compose down --volumes
```

## Endpoints
### Messages
`localhost:8000/messages`: Retorna todas as mensagens relacionadas ao usuário logado.

`localhost:8000/messages/?chat_with=<ID>`: Retorna as mensagens do usuário logado com o usuário do `ID`especificado.



## Problemas pendentes:
- O sistema de chat foi ainda está limitado, as respostas da api precisam ser melhoradas.

- É necessário fazer os endpoints de login e criação de usuário.

- Falta uma url que retorne uma lista de chats que o usuário possui
