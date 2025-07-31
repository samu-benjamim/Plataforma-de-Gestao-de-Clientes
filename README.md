![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

# 📌 Sistema de Gerenciamento de Clientes

API REST construída com **Python + Flask + SQLite** para **cadastro, listagem, atualização e remoção** de clientes.

---

## 🚀 Tecnologias usadas

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Marshmallow (validação de dados)
- SQLite
- Postman/cURL (para testes de API)

---

## 📂 Estrutura do Projeto

```
/cliente_api
│── app.py           # Arquivo principal Flask
│── route.py         # Rotas da API com Blueprint
│── models.py        # Modelos e configuração do banco de dados
│── schemas.py       # Schemas do Marshmallow para validação
│── config.py        # Configurações da aplicação
│── seed.py          # Script para popular o banco de dados
│── database.db      # Banco de dados SQLite
│── requirements.txt # Dependências do projeto
```

---

## ✅ Requisitos

- Python **3.10+**
- pip **22+**

---

## 📦 Instalação e Configuração

### 1️⃣ Clonar o repositório:

```bash
git clone https://github.com/samu-benjamim/Plataforma-de-Gestao-de-Clientes.git
cd Plataforma-de-Gestao-de-Clientes
```

### 2️⃣ Criar e ativar o ambiente virtual:

```bash
python -m venv venv
```

#### Windows

```
venv\Scripts\activate
```

#### Linux/Mac

```
source venv/bin/activate
```

### 3️⃣ Instalar dependências:

```bash
pip install -r requirements.txt
```

### 4️⃣ Rodar o servidor:

```bash
python app.py
```

A API estará disponível em: `http://127.0.0.1:5000`

---

## 📌 Endpoints da API

### 🔹 Listar todos os clientes

```http
GET /clientes
```

### 🔹 Obter cliente específico

```http
GET /clientes/<id>
```

### 🔹 Criar novo cliente

```http
POST /clientes
```

📥 **Exemplo de JSON**

```json
{
  "nome": "João Silva",
  "email": "joao@email.com",
  "telefone": "11999999999"
}
```

### 🔹 Atualizar cliente

```http
PUT /clientes/<id>
```

📥 **Exemplo de JSON**

```json
{
  "nome": "Maria Oliveira",
  "email": "maria@email.com",
  "telefone": "11988887777"
}
```

### 🔹 Deletar cliente

```http
DELETE /clientes/<id>
```

---

## 🔄 Fluxo da Aplicação

```text
+-----------+       HTTP        +-----------+       SQL        +--------------+
|  Cliente  |  <------------>   |  Flask    |  <----------->   |   SQLite DB  |
| (Postman, |  GET / POST / PUT |  API      |  CRUD Operações  |  database.db |
| Frontend) |  DELETE / PATCH   |  (route)  |                  |              |
+-----------+                   +-----------+                  +--------------+
```

---

## 🧪 Testando a API com Postman ou cURL

### ➤ Criar cliente (POST)

```bash
curl -X POST http://127.0.0.1:5000/clientes -H "Content-Type: application/json" -d '{"nome": "João Silva", "email": "joao@email.com", "telefone": "11999999999"}'
```

### ➤ Listar clientes (GET)

```bash
curl http://127.0.0.1:5000/clientes
```

### ➤ Atualizar cliente (PUT)

```bash
curl -X PUT http://127.0.0.1:5000/clientes/1 -H "Content-Type: application/json" -d '{"nome": "Maria Oliveira"}'
```

### ➤ Deletar cliente (DELETE)

```bash
curl -X DELETE http://127.0.0.1:5000/clientes/1
```

---

## 🧩 Estrutura do Modelo Cliente

- `id`: Inteiro, chave primária
- `nome`: String (obrigatório)
- `email`: String (obrigatório)
- `telefone`: String (obrigatório)

---

## 📜 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

🔗 **Repositório:** [github.com/samu-benjamim/Plataforma-de-Gestao-de-Clientes](https://github.com/samu-benjamim/Plataforma-de-Gestao-de-Clientes)
