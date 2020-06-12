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
É necessário passar o Token no header da requisição para acessar esses endpoint.

* `localhost:8000/messages`: 
    **GET** - Retorna todas as mensagens relacionadas ao usuário logado.  
    **POST** - Manda novas mensagens.  
    ```json
    {
        "receiver": "<USERNAME>",
        "message": "<MENSAGEM>"
    }
    ```
    **receiver**: *username* do usuário destinatário.
    **message**: Mensagem a ser enviada.


* `localhost:8000/messages/<ID>`:
    **GET** - Retorna a mensagem com o *id* especificado.
    **DELETE** - Deleta a mensagem.


* `localhost:8000/messages/?chat_with=<USERNAME>`: 
    **GET** - Retorna a lista de mensagens trocadas do usuário logado com o usuário do *username* especificado.

### Users
* `localhost:8000/api/auth/register/`:
    **POST** - Faz o registro do usuário, retornando o usuário logado e o token.
    ```json
    {
        "username": "exemplo",
        "first_name": "Joao",
        "last_name": "Da Silva",
        "password": "senha123"
    }
    ```
    **username**: *username* único de escolha do usuário
    **first_name**: nome do usuário.
    **last_name**: sobrenome do usuário.
    **password**: senha de acesso.


* `localhost:8000/api/auth/login/`:
    **POST** - Faz o login do usuário, retornando o usuário logado e o token.
    ```json
    {
        "username": "exemplo",
        "password": "senha123"
    }
    ```
    **username**: *username* do usuário cadastrado.
    **password**: senha de acesso.


* `localhost:8000/api/auth/logout/`:
    **POST** - Faz o logout do usuário.
    - *Obs.:* É necessário passar o Token no header da requisição.


* `localhost:8000/api/auth/password_change/`:
    **POST** - Atualiza a senha do usuário.
    ```json
    {
 	    "current_password": "senhaantiga123",
	    "new_password": "novasenha123"
    }
    ```
     - *Obs.:* É necessário passar o Token no header da requisição.


## Problemas pendentes:

- Falta uma url que retorne uma lista de chats que o usuário possui
