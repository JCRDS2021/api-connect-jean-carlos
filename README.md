# 🔗 API Connect — Gerenciamento de Usuários

> MVP de API REST para gerenciamento de usuários, desenvolvido como projeto acadêmico.

---

## 📌 Objetivo

A API Connect tem como objetivo fornecer uma interface RESTful para as operações de
criação, listagem, busca, atualização e remoção de usuários (CRUD completo), seguindo
os padrões da arquitetura REST e as boas práticas de desenvolvimento back-end moderno.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Função |
|---|---|---|
| Python | 3.x | Linguagem principal |
| Flask | 3.x | Framework web / servidor HTTP |
| python-dotenv | 1.x | Gerenciamento de variáveis de ambiente |
| Git | — | Controle de versão |
| GitHub | — | Hospedagem do repositório |

---

## 🗂️ Estrutura do Projeto

api-usuarios/
│
├── app.py # Ponto de entrada da aplicação
├── requirements.txt # Dependências do projeto
├── .gitignore # Arquivos ignorados pelo Git
│
├── routes/
│ ├── init.py
│ └── usuarios.py # Definição das rotas HTTP
│
├── controllers/
│ ├── init.py
│ └── usuario_controller.py # Lógica de negócio e validações
│
└── data/
├── init.py
└── banco.py # Persistência simulada em memória


---

## ⚙️ Como executar localmente

### Pré-requisitos
- Python 3.x instalado
- Git instalado

### Passo a passo

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/api-connect-seu-nome-sobrenome.git
cd api-connect-seu-nome-sobrenome
```

**2. Crie e ative o ambiente virtual**
```bash
# Criar
python -m venv venv

# Ativar — Windows
venv\Scripts\activate

# Ativar — Mac/Linux
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Inicie o servidor**
```bash
python app.py
```

**5. Acesse a API**
http://localhost:5000/


---

## 🔌 Endpoints Disponíveis

Base URL: `http://localhost:5000`

### Verificação do servidor

| Método | Rota | Descrição | Status |
|---|---|---|---|
| GET | `/` | Verifica se o servidor está online | 200 |

---

### Usuários

| Método | Rota | Descrição | Status de sucesso |
|---|---|---|---|
| GET | `/usuarios/` | Lista todos os usuários | 200 OK |
| GET | `/usuarios/<id>` | Busca um usuário pelo ID | 200 OK |
| POST | `/usuarios/` | Cadastra um novo usuário | 201 Created |
| PUT | `/usuarios/<id>` | Atualiza um usuário pelo ID | 200 OK |
| DELETE | `/usuarios/<id>` | Remove um usuário pelo ID | 200 OK |

---

### Exemplos de requisição e resposta

#### ✅ GET /usuarios/
**Resposta 200 OK:**
```json
[
  {"id": 1, "nome": "Ana Lima",    "email": "ana.lima@email.com"},
  {"id": 2, "nome": "Bruno Costa", "email": "bruno.costa@email.com"},
  {"id": 3, "nome": "Carla Souza", "email": "carla.souza@email.com"}
]
```

---

#### ✅ GET /usuarios/1
**Resposta 200 OK:**
```json
{"id": 1, "nome": "Ana Lima", "email": "ana.lima@email.com"}
```

**Resposta 404 Not Found:**
```json
{"erro": "Usuário com ID 99 não encontrado."}
```

---

#### ✅ POST /usuarios/
**Body da requisição:**
```json
{"nome": "Diego Mendes", "email": "diego@email.com"}
```
**Resposta 201 Created:**
```json
{"id": 4, "nome": "Diego Mendes", "email": "diego@email.com"}
```

**Resposta 400 Bad Request:**
```json
{"erro": "Os campos 'nome' e 'email' são obrigatórios."}
```

---

#### ✅ PUT /usuarios/1
**Body da requisição:**
```json
{"nome": "Ana Lima Silva"}
```
**Resposta 200 OK:**
```json
{"id": 1, "nome": "Ana Lima Silva", "email": "ana.lima@email.com"}
```

---

#### ✅ DELETE /usuarios/2
**Resposta 200 OK:**
```json
{
  "mensagem": "Usuário 'Bruno Costa' removido com sucesso.",
  "usuario": {"id": 2, "nome": "Bruno Costa", "email": "bruno.costa@email.com"}
}
```

---

## 📋 Códigos de Status HTTP Utilizados

| Código | Status | Quando ocorre |
|---|---|---|
| 200 | OK | Requisição bem-sucedida |
| 201 | Created | Recurso criado com sucesso |
| 400 | Bad Request | Dados ausentes ou inválidos |
| 404 | Not Found | Recurso não encontrado |

---

## 👨‍💻 Autor

**Seu Nome Completo**
Estudante de Análise e Desenvolvimento de Sistemas

[![GitHub](https://img.shields.io/badge/GitHub-seu--usuario-181717?logo=github)](https://github.com/seu-usuario)
