# Chat API

## Suba a api:
```
docker-compose up
```

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

## Problemas pendentes:
- O sistema de chat foi ainda está limitado, as respostas da api precisam ser melhoradas.

- O tutorial não utilizava o sistema de respostas do django rest. Precisa, então, adaptar para utiliza-lo.

- É necessário fazer os endpoints de login e criação de usuário.

- É necessário restringir a criação de mensagens a usuários logados

## Referencias:

[Tutorial utilizado para fazer o sistema de chat](https://steemit.com/utopian-io/@ajmaln/part-1-creating-a-simple-chat-app-with-djangorestframework)