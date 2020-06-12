# Chat API

## Suba a api:

```
docker-compose up
```

Após o comando a api estará rodando em:

```
http://localhost:8000/
```

## Endpoints

### Autenticação
#### `/api/auth/register/`:

**POST** - Faz o registro do usuário, retornando o usuário logado e o token.

```json
{
    "username": "exemplo",
    "first_name": "Joao",
    "last_name": "Da Silva Sauro",
    "password": "senha123"
}
```

**username**: *username* único de escolha do usuário

**first_name**: nome do usuário.

**last_name**: sobrenome do usuário.

**password**: senha de acesso.


#### `/api/auth/login/`:

**POST** - Faz o login do usuário, retornando o usuário logado e o token.

```json
{
    "username": "exemplo",
    "password": "senha123"
}
```

**username**: *username* do usuário cadastrado.

**password**: senha de acesso.


#### `/api/auth/logout/`:

**POST** - Faz o logout do usuário.

*Obs.:* É necessário passar o `token` no header da requisição.


#### `/api/auth/password_change/`:

**POST** - Atualiza a senha do usuário.

```json
{
    "current_password": "senhaantiga123",
    "new_password": "novasenha123"
}
```

*Obs.:* É necessário passar o `token` no header da requisição.


### Users

#### `/api/users/`

**GET** - Retorna lista com todos os usuários cadastrados na aplicação.

*Obs.:* É necessário passar o `token` no header da requisição.


### Messages

*Obs.:* É necessário passar o `token` no header da requisição para acessar todos os *endpoints* de mensagem.

#### `/api/messages/`: 

**GET** - Retorna todas as mensagens relacionadas ao usuário logado.  

**POST** - Manda novas mensagens.  

```json
{
    "receiver": "<USERNAME>",
    "message": "<MENSAGEM>"
}
```

* **receiver**: *username* do usuário destinatário.

* **message**: Mensagem a ser enviada.


#### `/api/messages/<ID>/`:

**GET** - Retorna a mensagem com o *id* especificado.

**DELETE** - Deleta a mensagem.


#### `/api/messages/?chat_with=<USERNAME>`: 

**GET** - Retorna a lista de mensagens trocadas do usuário logado com o usuário do *username* especificado.


### Chats

#### `/api/chatting_with/`

**GET** - Retorna lista de todos os usuários dos quais o usuário logado está trocando mensagens.

*Obs.:* É necessário passar o `token` no header da requisição.

## Requisições com token:

Algumas consultas a api exigem que o `token` esteja presente no `header` da requisição, pois são restritas a usuários logados. Veja abaixo um exemplo de header com token.

``` json
header: {
    "Authorization": "Token 63c986fba4901025b7f1a0069f1636cd4"
}
```
*Obs.: O token apresentado no exemplo é ficticio. Está apenas representando a estrutura final do header.*

O `token` é disponibilizado nas respostas dos endpoints de login e cadastro.



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

Com o super usuário é possivel logar na parte `admin` da aplicação, no endpoint `/admin`

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

