# Projeto API Cola&Bora 2.0 🤝♻️🐶

#### Cola&Bora é um projeto criado com o intuito de conectar pessoas a ONGs e ações sociais, permitindo que usuários se inscrevam, participem de eventos e façam doações a ONGs com as quais se identifiquem!


### Endpoints:
<b>URL base da API: https://api-cola-e-bora.onrender.com </b>

---

## 🔹 **Rotas de Usuário**
### ▪️ Criação de Usuário

Para a rota de criação de usuário, não é preciso estar logado na aplicação.

> POST /users/ - FORMATO DA REQUISIÇÃO

```JSON
{
    "name": "Maria",
    "email": "maria@gmail.com",
    "birth_date": "1990-10-10",
    "password": "123456",
}
```

Caso tudo dê certo, a resposta será assim:

> POST /users - FORMATO DA RESPOSTA - STATUS 201

```JSON

  {
    "id": "f1428619-6db1-4600-b4bd-2f1410bf56ab",
    "name": "Maria",
    "email": "maria@gmail.com",
    "birth_date": "1990-10-10",
    "create_at": "2023-01-06T18:00:22.095169Z",
    "update_at": "2023-01-06T18:00:22.095169Z",
    "is_superuser": false,
    "is_active": true
}

```

### ⚠️ Possíveis Erros

> POST /users/ - FORMATO DA RESPOSTA - STATUS 400

Caso você esqueça de enviar algum campo, como por exemplo o nome do usuário, a resposta de erro será assim:

```JSON
{
    "name": [ "This field is required." ]
}
```

> POST /users/ - FORMATO DA RESPOSTA - STATUS 400

Caso alguma chave do corpo da requisição esteja errada,como por exemplo, a chave "name" seja escrita "nome", a resposta de erro será assim:

```JSON
{
    "name": [ "This field is required." ]
}
```

> POST /users/ - FORMATO DA RESPOSTA - STATUS 400

Caso o email já esteja cadastrado, a resposta de erro será assim:

```JSON
{
  "email": [ "This field must be unique." ]
}
```

### ▪️ Editar Usuário

Nesta rota, o usuário precisa estar logado com o token no cabeçalho da requisição. Além disso, o usuário só poderá editar os seus próprios dados.

Nesse endpoint podemos atualizar dados do usuário, porém, não permite a atualização dos campos **id, is_superuser e is_active.**

> PATCH /users/<user_id>/ - FORMATO DA REQUISIÇÃO

```JSON
{
    "name": "Maria",
    "email": "maria@gmail.com",
    "birth_date": "1990-10-10",
    "password": "123456",
}
```

Caso tudo dê certo, a resposta será assim:

> PATCH /users/<user_id>/ - FORMATO DA RESPOSTA - STATUS 200

```JSON
{
    "id": "8af2883d-9d04-444e-acd0-750ce7bd3e20",
    "name": "Maria Edited",
    "email": "maria@gmail.com",
    "birth_date": "1990-10-10",
    "create_at": "2023-01-09T12:39:33.670638Z",
    "update_at": "2023-01-09T12:44:43.070078Z",
    "is_superuser": false,
    "is_active": true
}
```

### ⚠️ Possíveis Erros

> PATCH /users/<user_id>/ - FORMATO DA RESPOSTA - STATUS 401

Caso o token seja inválido, a resposta de erro será assim:

```JSON
 { "detail": "Given token not valid for any token type",
    "code": "token_not_valid",
    "messages": 
    [{
	"token_class": "AccessToken",
	"token_type": "access",
	"message": "Token is invalid or expired"
    }]
}
```

> PATCH /users/<user_id> - FORMATO DA RESPOSTA - STATUS 401

Caso o usuário esteja inativo, a resposta de erro será assim:

```JSON
{
  "detail": "User is inative"
}
```

> PATCH /users/<user_id>/ - FORMATO DA RESPOSTA - STATUS 403

Caso o usuário não seja dono do recurso, a resposta de erro será assim:

```JSON
{"detail": "You do not have permission to perform this action." }
```

### ▪️ Deletar Usuário (Soft Delete)

Na api Cola&Bora a rota de deleção aplica um soft delete no usuário em questão.Essa rota apenas altera o campo <b>is_active</b> para <b>false</b>.

Nesta rota, o usuário precisa estar logado com o token no cabeçalho da requisição. Além disso, o usuário só poderá deletar a si mesmo.

> DELETE /users/<user_id>/ - FORMATO DA REQUISIÇÃO

```
Não é necessário um corpo da requisição.
```

Caso tudo dê certo, a resposta será assim:

> DELETE /users/<user_id>/ - FORMATO DA RESPOSTA - STATUS 204

```
A resposta não conterá nenhuma mensagem.
```

### ⚠️ Possíveis Erros

> DELETE /users/<user_id>/ - FORMATO DA RESPOSTA - STATUS 401

Caso o token seja inválido, a resposta de erro será assim:

```JSON
{  "detail": "Given token not valid for any token type",
    "code": "token_not_valid",
    "messages": 
    [{
	"token_class": "AccessToken",
	"token_type": "access",
	"message": "Token is invalid or expired"
    }]
}
```

> DELETE /users/<user_id>/ - FORMATO DA RESPOSTA - STATUS 401

Caso o usuário esteja inativo, a resposta de erro será assim:

```JSON
{
  "detail": "User is inative"
}
```

> DELETE /users/<user_id> - FORMATO DA RESPOSTA - STATUS 403

Caso o usuário não seja dono do recurso, a resposta de erro será assim:

```JSON
{ "detail": "You do not have permission to perform this action." }
```
## 🔹 **Rotas de Pagamento**
### ▪️ Cadastro de método de pagamento

> POST /users/<user_id>/payments/ - FORMATO DE REQUISIÇÃO

```JSON
{
  "number": "5593889718264334",
  "security_code": "407",
  "due_date": "2024-08-01"
}
```

Caso tudo dê certo, a resposta será assim:

> POST /users/<user_id>/payments/ - FORMATO DE RESPOSTA - STATUS 201

```JSON
{
    "id": "fc5ee9b8-adc1-4f1c-8a59-633de360279d",
    "number": "5593889718264334",
    "security_code": "407",
    "due_date": "2024-08-01",
    "user_id": "f1428619-6db1-4600-b4bd-2f1410bf56ab"
}
```

### ⚠️ Possíveis Erros

> POST /users/<user_id>/payments/ - FORMATO DA RESPOSTA - STATUS 400

Caso você esqueça de enviar algum campo, a resposta de erro será assim:

```JSON
{
    "key": [ "This field is required." ]
}
```

> POST /users/<user_id>/payments/ - FORMATO DA RESPOSTA - STATUS 400

Caso alguma chave do corpo da requisição esteja errada, a resposta de erro será assim:

```JSON
{
    "key": [ "This field is required." ]
}
```

> POST /users/<user_id>/payments/ - FORMATO DA RESPOSTA - STATUS 400

Caso o usuário cadastre um cartão de crédito existente, a resposta de erro será assim:

```JSON
{ "number": [ "payment info with this number already exists." ] }
```

### ▪️ Editar método de pagamento

> PATCH /users/<user_id>/payments/<card_id> - FORMATO DE REQUISIÇÃO

```JSON
{
  "number": "1111222218264334",
  "security_code": "111",
  "due_date": "2030-10-01"
}
```

Caso tudo dê certo, a resposta será assim:

>  PATCH /users/<user_id>/payments/<card_id> - FORMATO DE RESPOSTA - STATUS 200

```JSON
{
    "id": "d8e9a15d-fbf1-414e-91d4-c13276c40d48",
    "number": "1111222218264334",
    "security_code": "111",
    "due_date": "2030-10-01",
    "user": "09aa5e17-186b-4577-8081-aacd38e6e70f"
}
```

### ⚠️ Possíveis Erros

>  PATCH /users/<user_id>/payments/<card_id> - FORMATO DA RESPOSTA - STATUS 400

Caso alguma chave do corpo da requição esteja errada, a resposta de erro será assim:

```JSON
{
  "key": "This field is required."
}
```

>  PATCH /users/<user_id>/payments/<card_id> - FORMATO DA RESPOSTA - STATUS 400

Caso o token seja inválido, a resposta de erro será assim:

```JSON
{  "detail": "Given token not valid for any token type",
    "code": "token_not_valid",
    "messages": 
    [{
	"token_class": "AccessToken",
	"token_type": "access",
	"message": "Token is invalid or expired"
    }]
}
```

>  PATCH /users/<user_id>/payments/<card_id> - FORMATO DA RESPOSTA - STATUS 400

Caso o usuário esteja inativo, a resposta de erro será assim:

```JSON
{
  "detail": "User is inative"
}
```

>  PATCH /users/<user_id>/payments/<card_id> - FORMATO DA RESPOSTA - STATUS 401

Caso o usuário não seja dono do recurso, a resposta de erro será assim:

```JSON
{" detail": "You do not have permission to perform this action." }
```

>  PATCH /users/<user_id>/payments/<card_id> - FORMATO DA RESPOSTA - STATUS 404

Caso não exista um método de pagamento cadastrado, a resposta de erro será assim:

```JSON
{
  "message": "Payment method does not exist"
}
```

### ▪️ Deletar método de pagamento

> DELETE /users/<user_id>/payments/<card_id> - FORMATO DA REQUISIÇÃO`

```
Não é necessário um corpo da requisição.
```

Caso tudo dê certo, a resposta será assim:

> DELETE /users/<user_id>/payments/<card_id> - FORMATO DA RESPOSTA - STATUS 204

```
A resposta não conterá nenhuma mensagem.
```

### ⚠️ Possíveis Erros


> DELETE /users/<user_id>/payments/<card_id> - FORMATO DA RESPOSTA - STATUS 400

Caso o token seja inválido, a resposta de erro será assim:

```JSON
{  "detail": "Given token not valid for any token type",
    "code": "token_not_valid",
    "messages": 
    [{
	"token_class": "AccessToken",
	"token_type": "access",
	"message": "Token is invalid or expired"
    }]
}
```



> DELETE /users/<user_id>/payments/<card_id> - FORMATO DA RESPOSTA - STATUS 400

Caso o usuário esteja inativo, a resposta de erro será assim:

```JSON
{
  "detail": "User is inative"
}
```

> DELETE /users/<user_id>/payments/<card_id> - FORMATO DA RESPOSTA - STATUS 401

Caso o usuário não seja dono do recurso, a resposta de erro será assim:

```JSON
{" detail": "You do not have permission to perform this action." }
```

> DELETE /users/payments/:userId - FORMATO DA RESPOSTA - STATUS 404

Caso não exista um método de pagamento cadastrado, a resposta de erro será assim:

```JSON
{
  "message": "Payment method does not exist"
}
```

## 🔹 **Rota de Doação**

### ▪️ Realizar uma doação

Nesta rota o Usuário precisa estar logado, e não precisa de autorização de admnistrador.

Esta rota é capaz de realizar uma doação para uma ong específica.

> POST /donations/<ong_id> - FORMATO DE REQUISIÇÃO

```JSON
{
 "value" : 200.00
}
```

> POST /donations/<ong_id> - FORMATO DE RESPOSTA - 201

```JSON
{
    "id": "88249fc1-e9e5-4ffe-b008-02afc7566996",
    "value": "100.00",
    "date": "2023-01-09T13:27:23.908339Z",
    "user": "45730532-62f5-4cf2-9168-698459d7e675",
    "ong": "26718f11-cbfb-49af-821c-1722da075a28"
}
```

### ⚠️ Possíveis Erros

> POST /donations/<ong_id> - FORMATO DA RESPOSTA - STATUS 400

Caso você esqueça de enviar o campo, a resposta de erro será assim:

```JSON
{
  "value": ["This field is required."]
}
```

> POST /donations/<ong_id> - FORMATO DE RESPOSTA - STATUS 404

Caso a ong não seja encontrada, a resposta de erro será assim::

```JSON
{
  "detail": "Not found."
}
```

> POST /donations/<ong_id> - FORMATO DA RESPOSTA - STATUS 400

Caso o token seja inválido, a resposta de erro será assim:

```JSON
{  "detail": "Given token not valid for any token type",
    "code": "token_not_valid",
    "messages": 
    [{
	"token_class": "AccessToken",
	"token_type": "access",
	"message": "Token is invalid or expired"
    }]
}
```

> POST /donations/<ong_id> - FORMATO DA RESPOSTA - STATUS 400

Caso o usuário esteja inativo, a resposta de erro será assim:

```JSON
{
  "detail": "User is inative"
}
```

> POST /donations/<ong_id> - FORMATO DA RESPOSTA - STATUS 400

Caso o valor enviado no corpo da requisição não seja do tipo number, a resposta de erro será assim:

```JSON
{
    "value": [ "A valid number is required." ]
}
```

## 🔹 **Rota de Login**

### ▪️ Realizar login na aplicação

Nesta rota o Usuário precisa não estar logado, e não precisa de autorização de admnistrador. Independente de o usuário estar ativo ou não, essa rota automaticamente seta a chave **is_active** para **true**.

> POST users/login/ - FORMATO DA REQUISIÇÃO

```JSON
{
    "email": "maria@gmail.com",
    "password": "123456"
}
```

Caso tudo dê certo, a resposta será dois tokens de autenticação. O token de acesso e um de atualização para caso o token expire:

> POST users/login/ - FORMATO DA RESPOSTA - STATUS 200

```JSON
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MzY1MzY5NCwiaWF0IjoxNjczMDQ4ODk0LCJqdGkiOiJjZjQ5YzQ1NjFjZDg0MTE2YjIxNzQ3YjZhMjQ0ZWJmOCIsInVzZXJfaWQiOiI2MmM3M2M4NS0xNGM2LTQ0YzctYTQ5ZC1kM2JkNGUxZGQ5MWQifQ.XPDhskxDvAWe7DRh1IJFH_-pv92ZMnOZctcUKF9lOCM",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjczMTAyODk0LCJpYXQiOjE2NzMwNDg4OTQsImp0aSI6IjY2MDdjZTk4YTY5NzRiNjJiNDI3NDgwMWIxZWU4MDY3IiwidXNlcl9pZCI6IjYyYzczYzg1LTE0YzYtNDRjNy1hNDlkLWQzYmQ0ZTFkZDkxZCJ9.91i7NzMUiEpEzjltBm4OX1YVWwHZ3zVElttqGoQJ7Z8"
    "user": {
    "id": "f1428619-6db1-4600-b4bd-2f1410bf56ab",
    "name": "Maria",
    "email": "maria@gmail.com",
    "birth_date": "1990-10-10",
    "create_at": "2023-01-06T18:00:22.095169Z",
    "update_at": "2023-01-06T18:00:22.095169Z",
    "is_superuser": false,
    "is_active": true
    }
}
```

### ⚠️ Possíveis Erros

> POST users/login/ - FORMATO DA RESPOSTA - STATUS 400

Caso alguma chave do corpo da requisição esteja errada ou não seja passada, a resposta de erro será assim:

```JSON
{
  "key": ["This field is required."]
}
```

> POST /login - FORMATO DA RESPOSTA - STATUS 401

Caso o usuário não seja dono da conta ou tenha passado alguma informação errada, a resposta de erro será assim::

```JSON
{
    "detail": "No active account found with the given credentials"
}
```

## 🔹 **Rota de Atualização de Token de Acesso**
Caso o access_token tenha sido expirado, o usuário pode solicitá-lo novamente sem a necessidade de realizar login, atráves do seu refresh_token. Por padrão, o tempo de expiração do access_token é de 15 horas e do refresh_token 7 dias.

>POST /users/refresh/ - FORMATO DA REQUISIÇÃO
~~~JSON
  {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MzY1MzY5NCwiaWF0IjoxNjczMDQ4ODk0LCJqdGkiOiJjZjQ5YzQ1NjFjZDg0MTE2YjIxNzQ3YjZhMjQ0ZWJmOCIsInVzZXJfaWQiOiI2MmM3M2M4NS0xNGM2LTQ0YzctYTQ5ZC1kM2JkNGUxZGQ5MWQifQ.XPDhskxDvAWe7DRh1IJFH_-pv92ZMnOZctcUKF9lOCM",
  }
~~~

Caso tudo dê certo a resposta deverá ser assim:

> POST /users/refresh/ - FORMATO DA RESPOSTA - STATUS 200

~~~JSON
  {
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MzY1MzY5NCwiaWF0IjoxNjczMDQ4ODk0LCJqdGkiOiJjZjQ5YzQ1NjFjZDg0MTE2YjIxNzQ3YjZhMjQ0ZWJmOCIsInVzZXJfaWQiOiI2MmM3M2M4NS0xNGM2LTQ0YzctYTQ5ZC1kM2JkNGUxZGQ5MWQifQ.XPDhskxDvAWe7DRh1IJFH_-pv92ZMnOZctcUKF9lOCM",
  }
~~~

### ⚠️ Possível Erro

> POST /users/refresh/ - FORMATO DA RESPOSTA - STATUS 401

Caso o refresh_token tenha expirado e/ou seja inválido, o erro será assim:

~~~JSON
{
    "detail": "Token is invalid or expired",
    "code": "token_not_valid"
}
~~~

## 🔹 **Rotas de Ongs**
### ▪️ Criação de Ong

Para criação de uma ong o usuário deve estar cadastrado e logado.

Devem ser passados os dados da Ong e uma categoria válida em formato de string dentro das opções: meio ambiente, animais, assistência social, cultura, saúde, desenvolvimento e defesa de direitos, habitação, educação, pesquisa, outro.

>POST /ongs/ - FORMATO DA REQUISIÇÃO

~~~JSON
  {
    "name": "nome da ong",
    "email": "ong@email.com",
    "tel": "9955996366",
    "description": "breve descrição da ong",
    "cnpj": "11222333344445",
    "category": "categoria válida"
  }
~~~

Caso tudo dê certo a resposta deverá ser assim:

> POST /ongs/ - FORMATO DA RESPOSTA - STATUS 201

~~~JSON
{
    "id": "cda1d093-4872-4742-a53a-5c207adcdcda",
    "name": "Nome da Ong",
    "email": "ong@email.com",
    "tel": "92988556443",
    "description": "Descrição do serviço prestado pela ong",
    "cnpj": "11222447878543",
    "createdAt": "2023-01-06T18:58:53.162097Z",
    "updatedAt": "2023-01-06T18:58:53.162097Z",
    "category": "outro",
    "user": "62c73c85-14c6-44c7-a49d-d3bd4e1dd91d"
}

~~~


### ⚠️ Possíveis Erros

> POST /ongs/ - FORMATO DA RESPOSTA - STATUS 400

Requisição enviada com campo obrigatório faltando: 
~~~JSON
{
    "nome_do_campo": [
        "This field is required."
    ]
}
~~~


> POST /ongs/ - FORMATO DA RESPOSTA - STATUS 400

Requisição enviada por usuário que já possui uma ONG: 
```JSON
{
    "detail": "This user already have a ONG created"
}
```

> POST /ongs/ - FORMATO DA RESPOSTA - STATUS 404

Requisição enviada com categoria inexistente: 
```JSON
{
    "category": [
        "\"categoria enviada\" is not a valid choice."
    ]
}
```

> POST /ongs/ - FORMATO DA RESPOSTA - STATUS 400

Requisição enviada com propriedades email ou cnpj já cadastradas no banco de dados: 
```JSON
{
    "email": [
        "ong with this email already exists."
	],
    "cnpj": [
        "ong with this cnpj already exists."
    ]
}
```

### ▪️ Editar Ong

Para editar uma ong o usuário deverá estar logado e ter permissão de adm para aquela ong.

Podem ser editados os campos: name, email, tel, description, cnpj.

>PATCH /ongs/<ong_id>/ - FORMATO DA REQUISIÇÃO

~~~JSON
  {

    "name": "Nome da Ong Updated",
    "email": "ongupdated@email.com",
    "tel": "21966356685",
    "description": "Descrição do serviço prestado pela ong - updated",
    "cnpj": "11222333444455"
  }
~~~

Em caso de sucesso a resposta deverá ser assim

>PATCH /ongs/<ong_id>/ - FORMATO DA RESPOSTA - STATUS 200

~~~JSON
{
    "id": "cda1d093-4872-4742-a53a-5c207adcdcda",
    "name": "Nome da Ong Updated",
    "email": "ongupdated@email.com",
    "tel": "21966356685",
    "description": "Descrição do serviço prestado pela ong - updated",
    "cnpj": "11222333444455",
    "createdAt": "2023-01-06T18:58:53.162097Z",
    "updatedAt": "2023-01-06T18:58:53.162097Z",
    "category": "outro",
    "user": "62c73c85-14c6-44c7-a49d-d3bd4e1dd91d"
}
~~~


### ⚠️ Possíveis Erros

> PATCH /ongs/<ong_id>/ - FORMATO DA RESPOSTA - STATUS 404

A ONG não foi encontrada: 
~~~JSON
{
    "detail": "Not found."
}
~~~

> PATCH /ongs/<ong_id>/ - FORMATO DA RESPOSTA - STATUS 403

User não possui permissão de Admin para aquela ong: 
~~~JSON
{
    "detail": "You do not have permission to perform this action."
}
~~~


### ▪️ Deleção de Ong (Soft Delete)

Para acessar essa rota o usuário deve estar logado e ter permissão de admin na ONG que irá ser deletada. 

**Atenção! Ao deletar a Ong todos os eventos realizados por ela são deletados do banco.**


>DELETE /ongs/<ong_id>/ - FORMATO DA REQUISIÇÃO`

~~~
Não é necessário um corpo da requisição.
~~~

Se tudo der certo a resposta deverá ser:

>DELETE /ongs/<ong_id>/ - FORMATO DA RESPOSTA - STATUS 204


~~~
A resposta não conterá nenhuma mensagem.
~~~

>DELETE /ongs/<ong_id>/ - FORMATO DA RESPOSTA - STATUS 403

User não possui permissão de Admin para aquela ong: 
~~~JSON
{
    "detail": "You do not have permission to perform this action."
}
~~~

> DELETE /ongs/<ong_id>/ - FORMATO DA RESPOSTA - STATUS 404

A ONG não foi encontrada: 
~~~JSON
{
    "detail": "Not found."
}
~~~


### ▪️ Listar todas as ONGS

Essa rota não precisa de autenticação. A rota retorna todas as ONGs que estão cadastradas na aplicação e conta com paginação conforme exemplo abaixo:

> GET /ongs/ - FORMATO DE RESPOSTA - STATUS 200

~~~JSON
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "cda1d093-4872-4742-a53a-5c207adcdcda",
            "name": "Nome da Ong Updated",
            "email": "ongupdated@email.com",
            "tel": "21966356685",
            "description": "Descrição do serviço prestado pela ong - updated",
            "cnpj": "11222333444455",
            "createdAt": "2023-01-06T18:58:53.162097Z",
            "updatedAt": "2023-01-06T18:58:53.162097Z",
            "category": "outro",
            "user": "62c73c85-14c6-44c7-a49d-d3bd4e1dd91d"
        }
    ],
}
~~~

### ▪️ Listar Ong Específica


> GET /ongs/<ong_id>/ - FORMATO DA REQUISIÇÃO


Há dois tipos de respostas para essa requisição.
Caso seja um usuário comum autenticado deverá retornar:

~~~JSON
{
    "id": "cda1d093-4872-4742-a53a-5c207adcdcda",
    "name": "Nome da Ong Updated",
    "email": "ongupdated@email.com",
    "tel": "21966356685",
    "description": "Descrição do serviço prestado pela ong - updated",
    "cnpj": "11222333444455",
    "createdAt": "2023-01-06T18:58:53.162097Z",
    "updatedAt": "2023-01-06T18:58:53.162097Z",
    "category": "outro",
    "user": "62c73c85-14c6-44c7-a49d-d3bd4e1dd91d"
}
~~~


Caso seja um usuário com permissão de Admin para aquela ong, a resposta esperada deverá contar com o campo balance da Ong:

~~~JSON
{
    "id": "cda1d093-4872-4742-a53a-5c207adcdcda",
    "name": "Nome da Ong Updated",
    "email": "ongupdated@email.com",
    "tel": "21966356685",
    "description": "Descrição do serviço prestado pela ong - updated",
    "cnpj": "11222333444455",
    "createdAt": "2023-01-06T18:58:53.162097Z",
    "updatedAt": "2023-01-06T18:58:53.162097Z",
    "balance": "0.00",
    "category": "outro",
    "user": "62c73c85-14c6-44c7-a49d-d3bd4e1dd91d"
}
~~~



###AINDA FALTA###
### ▪️ Listar usuários cadastrados no evento de uma ONG específica

Nesta rota o Usuário precisa estar logado, e é acessada apenas pelo administrador da ONG em questão.

> GET /ongs/<event_id>/users/ - FORMATO DE RESPOSTA - STATUS 200

~~~ JSON
{
	"id": "e6ba07cf-896e-4e76-8bc3-79dadcf46643",
	"name": "Plantação de Mudas Edited",
	"date": "2023-02-12T14:00:00Z",
	"description": "Plantar mudas de árvore na avenida Djalma Batista",
	"address": {
		"street": "Av. Djalma Batista",
		"number": "20",
		"cep": "69070340",
		"extra": "Avenida",
		"id": "ee1c0890-8458-4106-bbaf-0ae8b3718722"
	},
	"ong": "0114982c-2936-4d87-924b-b94b40ae8e56",
	"volunteers": [
		{
		"id": "244f7c54-a218-4c08-8b34-833d81f1514d",
		"name": "Common Edited",
		"email": "common@gmail.com",
		"birth_date": "1997-12-22",
		"create_at": "2023-01-10T12:33:20.572939Z",
		"update_at": "2023-01-10T12:39:57.289390Z",
		"is_superuser": false,
		"is_active": true
		}
	]
}
~~~

### ⚠️ Possíveis Erros

O id da ong não for encontrado: 

> GET /ongs/<event_id>/users/ - FORMATO DA RESPOSTA - STATUS 404
~~~JSON
{
  "detail": "Not found."
}
~~~
---

## 🔹 **Rotas de Saque**

### ▪️ Realização de Saque
Esta rota é acessada apenas pelo administrador da ONG em questão. Nela, caso tenha saldo suficiente, o responsável pela ONG pode realizar o saque de fundos referentes a doações recebidas pelos demais usuários.

>POST /withdraw/<ong_id> - FORMATO DA REQUISIÇÃO

~~~JSON
{
    "value": 100
}
~~~

Caso tudo dê certo, a resposta será assim:

>POST /withdraw/<ong_id> - FORMATO DA RESPOSTA - STATUS 201

~~~JSON
{
    "id": "b18d4da2-6b6d-4426-b9f4-d9f8d5d029fe",
    "value": "100.00",
    "date": "2023-01-09T05:52:35.508570Z",
    "user": "06b696b8-72de-45f1-8fd98be24e108bd9",
    "ong": "1af6898f-2fcf-4fad-a926-6a43c5f6c7f4"
}
~~~

### ⚠️ Possíveis Erros

Caso o campo contendo o valor não seja enviado:

>POST /withdraw/<ong_id> - FORMATO DA RESPOSTA - STATUS 400


~~~JSON
{
    "value": ["This field is required."]
}
~~~

Caso o saldo seja insuficiente para realizar o saque solicitado:

>POST /withdraw/<ong_id> - FORMATO DA RESPOSTA - STATUS 401


~~~JSON
{
    "detail": "Insufficient funds"
}
~~~

Caso a ONG não seja encontrada:

>POST /withdraw/<ong_id> - FORMATO DA RESPOSTA - STATUS 404


~~~JSON
{
    "detail": "Not found."
}
~~~

Caso o usuário não seja responsável pela ONG:

>POST /withdraw/<ong_id> - FORMATO DA RESPOSTA - STATUS 401


~~~JSON
{
    "detail": "Not authorizated."
}
~~~


### ▪️ Listagem dos Saques
Esta rota é acessada apenas pelo administrador da ONG em questão. Nela, é possível verificar o histórico dos saques realizados.

>GET /withdraw/<ong_id> - FORMATO DA RESPOSTA - 200

~~~JSON
[
    {
        "id": "7ff505bd-640a-4f60-bfbf-0d2d23086b87",
        "value": "100.00",
        "date": "2023-01-06T14:32:52.918648Z",
        "user": "06b696b8-72de-45f1-8fd9-8be24e108bd9",
        "ong": "1af6898f-2fcf-4fad-a926-6a43c5f6c7f4"
    },
    {
        "id": "63965a92-0227-4d72-b83f-969f523bf202",
        "value": "450.50",
        "date": "2023-01-06T14:36:00.778329Z",
        "user": "06b696b8-72de-45f1-8fd9-8be24e108bd9",
        "ong": "1af6898f-2fcf-4fad-a926-6a43c5f6c7f4"
	},
        ...
]
~~~

### ⚠️ Possíveis Erros


Caso o token seja inválido, a resposta de erro será assim:

>GET /withdraw/<ong_id> - FORMATO DA RESPOSTA - 401

```JSON
 {  "detail": "Given token not valid for any token type",
    "code": "token_not_valid",
    "messages": 
    [{
	"token_class": "AccessToken",
	"token_type": "access",
	"message": "Token is invalid or expired"
    }]
}
```

Caso a ONG não seja encontrada:

>GET /withdraw/<ong_id> - FORMATO DA RESPOSTA - STATUS 404


~~~JSON
{
    "detail": "Not found."
}
~~~

Caso o usuário não seja responsável pela ONG:

>GET /withdraw/<ong_id> - FORMATO DA RESPOSTA - STATUS 401


~~~JSON
{
    "detail": "Not authorizated."
}
~~~


## 🔹 **Rotas de Eventos**

### ▪️ Criação de Evento
Esta rota é acessada apenas pelo administrador da ONG em questão.
O horário do evento deverá subir em horário local, e entrará no banco de dados automaticamente em horário UTC(Padrão Global GMT+0)


> POST /ongs/events/ - FORMATO DA REQUISIÇÃO
~~~JSON
{
  "name": "Ação de Natal",
  "date": "2023-12-24 14:00",
  "description": "Entrega de alimentos a famílias necessitadas na véspera do Natal",
  "ong_id": "1940084e-163a-4594-99f5-239fdac540e5",
  "address": {
    "street": "Rua Carolia Fernandes",
    "number": "980",
    "cep": "69400797",
    "extra": "casa"
   }
}
~~~

Caso tudo dê certo, a resposta será assim:

> POST /ongs/events/ - FORMATO DA RESPOSTA - STATUS 201

~~~JSON
{
	"data": {
	    "name": "Ação de Natal",
	    "description": "Entrega de alimentos a famílias necessitadas na véspera do Natal",
	    "date": "2022-12-24T14:00:00.000Z",
	    "ong": {
		    "id": "5d186775-fb9e-4612-9149-4d8e7aa6fc2c",
		    "name": "Amigos da Natureza Pt.2",
		    "email": "ong@email.com"
		},
	    "address": {
		    "street": "Rua Carolia Fernandes",
		    "number": "980",
		    "cep": "69400797",
		    "extra": "casa",
		    "id": "8f647ab0-6b99-4a1c-b837-e9a7c95959a5"
		},
	    "id": "3bf04ab3-7d2b-498b-a989-1f83c9c778b0"
	}
}
~~~

### ⚠️ Possíveis Erros

A data do evento não pode ser uma data passada: 

>POST ongs/events/ - FORMATO DA RESPOSTA - STATUS 400
~~~JSON
{
  "detail": "The event date cannot be a past date"
}
~~~

O id da ong não for encontrado: 

>POST ongs/events/ - FORMATO DA RESPOSTA - STATUS 404
~~~JSON
{
  "detail": "Ong not found."
}
~~~

### ▪️ Editar um Evento

Esta rota é acessada apenas pelo administrador da ONG em questão.
O horário do evento deverá subir em horário local, e entrará no banco de dados automaticamente em horário UTC(Padrão Global GMT+0)

>PATCH ongs/events/<event_id>/ - FORMATO DA REQUISIÇÃO

~~~JSON
{
  "name": "Ação de Natal - 2022",
  "date": "December 24, 2022 14:00:00",
  "description": "Entrega de alimentos a famílias necessitadas na véspera do Natal",
  "address": {
    "street": "Rua Carolia Fernandes",
    "number": "720",
    "cep": "69400797",
    "extra": "igreja"
   }
}
~~~

>PATCH ongs/events/<event_id>/- FORMATO DA RESPOSTA - STATUS 200

~~~JSON
{
	"name": "Plantação de Mudas Edited 2",
	"description": "Plantar mudas de árvore na avenida Djalma Batista",
	"date": "2023-02-12T14:00:00Z",
	"address": {
		"street": "Av. Djalma Batista",
		"number": "20",
		"cep": "69070340",
		"extra": "Avenida",
		"id": "ee1c0890-8458-4106-bbaf-0ae8b3718722"
	},
	"ong": {
		"id": "0114982c-2936-4d87-924b-b94b40ae8e56",
		"name": "Amigos da Natureza Edited",
		"email": "naturezae@gmail.com"
	},
	"id": "e6ba07cf-896e-4e76-8bc3-79dadcf46643",
	"volunteers": 1
}
~~~

### ⚠️ Possíveis Erros

O id do evento não for encontrado: 

>PATCH ongs/events/<event_id>/ - FORMATO DA RESPOSTA - STATUS 404
~~~JSON
{
  "detail": "Event not found."
}
~~~

>PATCH ongs/events/<event_id>/- FORMATO DA RESPOSTA - STATUS 400

O id fornecido não é um UUID válido: 
~~~JSON
{
  "detail": "Id must have a valid UUID format"
}
~~~


### ▪️ Deletar um Evento

Esta rota é acessada apenas pelo administrador da ONG em questão.

>DELETE ongs/events/<event_id>/ - FORMATO DA REQUISIÇÃO

~~~
Não é necessário um corpo da requisição.
~~~

>DELETE ongs/events/<event_id>/- FORMATO DA RESPOSTA - STATUS 204


~~~
A resposta não conterá nenhuma mensagem.
~~~



### ⚠️ Possíveis Erros

O id do evento não for encontrado: 

>DELETE ongs/events/<event_id>/ - FORMATO DA RESPOSTA - STATUS 404
~~~JSON
{
  "detail": "Event not found"
}
~~~

>DELETE ongs/events/<event_id>/ - FORMATO DA RESPOSTA - STATUS 400

O id fornecido não é um UUID válido: 
~~~JSON
{
  "detail": "Id must have a valid UUID format"
}
~~~


### ▪️ Cadastrar usuário em um Evento

Esta rota precisa de autenticação.

>POST /events/<event_id>/ - FORMATO DA REQUISIÇÃO

~~~
Não é necessário um corpo da requisição.
~~~

>POST /events/<event_id>/ - FORMATO DA RESPOSTA - STATUS 201

~~~JSON
{
 "detail": "User successfully registered on event."
}
~~~

### ⚠️ Possíveis Erros

O id do evento não for encontrado: 

>POST /events/<event_id>/ - FORMATO DA RESPOSTA - STATUS 404
~~~JSON
{
    "detail": "Not found."
}
~~~

>POST /events/<event_id>/ - FORMATO DA RESPOSTA - STATUS 403

O Adm da Ong que criou o evento não pode se cadastrar como voluntário, caso tente recebrá o seguinte erro: 
~~~JSON
{
    "detail": "You do not have permission to perform this action."
}
~~~

>POST /events/<event_id>/ - FORMATO DA RESPOSTA - STATUS 400

Quando o usuário tenta se cadastrar em um evento com data ou horário conflitante com algum outro evento que já esteja cadastrado.
Obs: Esse erro irá ocorrer quando houver uma diferença menor que uma hora entre os horários.
~~~JSON
{
  "detail": "You are already registered for an event at the same time"
}
~~~


### ▪️ Excluir a participação de usuário em um Evento

Rota para o usuário cadastrado cancelar sua participação no evento.

>DELETE /events/<event_id>/ - FORMATO DA REQUISIÇÃO

~~~
Não é necessário um corpo da requisição.
~~~

>DELETE /events/<event_id>/ - FORMATO DA RESPOSTA - STATUS 204

~~~
Não há corpo de resposta.
~~~

### ⚠️ Possíveis Erros

O id do evento não for encontrado: 

>DELETE /events/<event_id>/ - FORMATO DA RESPOSTA - STATUS 404
~~~JSON
{
    "detail": "Not found."
}
~~~



### ▪️ Listar todos os Eventos

Esta rota não precisa de autenticação.
Serão listados todos os eventos cadastrados na plataforma. Rota conta com paginação.

>GET /events/ - FORMATO DA RESPOSTA - STATUS 200

~~~JSON
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "c8e76c9d-7a84-4020-888e-1b49d7fab5e9",
            "name": "Nome do evento",
            "date": "2023-01-10T14:00:00Z",
            "description": "Descrição da ação",
            "address": {
                "street": "Rua Carolia Fernandes",
                "number": "980",
                "cep": "69400797",
                "extra": "casa",
            "id": "c5618c16-e7ea-424e-a5e2-be2a0418381f"
            },
            "ong": "2e27f538-ed1b-4ef6-b330-f081890f2ef3"
        }
    ],
}
~~~

### ▪️ Listar todos os Eventos de uma ONG específica

Esta rota não precisa de autenticação.Retornará todos os eventos de uma ONG que foi passada pelo parâmetro de rota.

>GET /events/ongs/<ong_id>/ - FORMATO DA REQUISIÇÃO
~~~
Não é necessário um corpo da requisição.
~~~

>GET /events/ongs/<ong_id>/ - FORMATO DA RESPOSTA - STATUS 200

~~~JSON
    
[
    {
	    "id": "776e1831-4f14-47e1-b5a3-fec2845236e1",
	    "name": "Réveillon Solidário",
	    "date": "2022-12-31T00:00:00Z",
	    "description": "Festa de reveillon",
	    "address": {
		    "street": "Rua A",
		    "number": "001",
		    "cep": "69200990",
		    "extra": "na rua A",
		    "id": "0fb5c58a-889f-4479-a25c-6e589de828da"
	    },
	    "ong": "6373a090-b379-4d59-b0ce-ce2390856f06"
    },
]
~~~

### ⚠️ Possíveis Erros

O id da ONG não for encontrado: 

>GET /events/ongs/<ong_id>/  - FORMATO DA RESPOSTA - STATUS 404
~~~JSON
{
    "detail": "Not found."
}
~~~

### ▪️ Listar um Evento específico

Esta rota não precisa de autenticação.

>GET /events/<event_id>/ - FORMATO DA REQUISIÇÃO

Não é necessário um corpo da requisição.


>GET /events/<event_id>/ - FORMATO DA RESPOSTA - STATUS 200

~~~JSON
{
    "name": "Nome do evento",
    "description": "Descrição da ação",
    "date": "2023-01-10T14:00:00Z",
    "address": {
        "street": "Rua Carolia Fernandes",
        "number": "980",
        "cep": "69400797",
        "extra": "casa",
        "id": "c5618c16-e7ea-424e-a5e2-be2a0418381f"
    },
    "ong": {},
    "id": "c8e76c9d-7a84-4020-888e-1b49d7fab5e9",
    "volunteers": 1
}
~~~

### ⚠️ Possíveis Erros

O id do evento não for encontrado: 

>GET /events/<event_id>/ - FORMATO DA RESPOSTA - STATUS 404
~~~JSON
{
    "detail": "Not found."
}
~~~
---
