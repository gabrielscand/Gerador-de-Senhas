# 🔐 Gerador de Senhas Seguras — Flask + HTML/CSS/JS

Uma aplicação **full stack** simples e bonita para gerar senhas fortes.  
Back-end em **Python + Flask** expondo uma API `/generate`, e front-end em **HTML/CSS/JS** consumindo essa API.

## ✨ Funcionalidades
- Geração de senhas com:
  - Tamanho configurável
  - Letras maiúsculas/minúsculas
  - Números
  - Símbolos
- Interface web limpa e responsiva
- Botão **“Copiar senha”** (clipboard)
- API REST JSON (`/generate`) para integrar com outras apps

---

## 🧰 Tecnologias
- **Back-end:** Python 3.9+ · Flask · Flask-CORS · python-dotenv
- **Front-end:** HTML · CSS · JavaScript (Fetch API)
- **Ambiente recomendado:** VS Code (extensão **Live Server**)

---

## 🗂️ Estrutura de Pastas
```
gerador-senhas/
├── backend/
│   ├── app.py
│   ├── utils/
│   │   └── password_generator.py
│   └── .env           (opcional)
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
└── requirements.txt
```

---

## 🚀 Como rodar (primeira vez)

1) **Criar e ativar o ambiente virtual**
```bash
cd gerador-senhas
python3 -m venv venv
source venv/bin/activate
```

2) **Instalar as dependências**
```bash
pip install --upgrade pip
pip install flask flask-cors python-dotenv
pip freeze > requirements.txt
```

3) **Subir o back-end (Flask)**
```bash
cd backend
python3 -m flask --app app:app run --debug
# ou:
# python3 app.py
```
O servidor sobe em: **http://127.0.0.1:5000**

4) **Abrir o front-end**
- Opção recomendada: abrir `frontend/index.html` com **Live Server**  
  (no VS Code: clique direito no `index.html` → *Open with Live Server*).  
  A página abrirá em algo como: `http://127.0.0.1:5500/frontend/index.html`

> Dica: abrir o `index.html` com duplo clique (URL `file://`) pode bloquear requisições por segurança em alguns navegadores. O **Live Server** evita isso.

---

## 🔁 Como rodar **de novo** (sempre que reabrir o projeto)

1) Abrir a pasta do projeto no VS Code  
2) Ativar o ambiente virtual e subir o Flask:
```bash
cd gerador-senhas/backend
source ../venv/bin/activate
python3 app.py   # ou: python3 -m flask --app app:app run --debug
```
3) Abrir o `frontend/index.html` (via **Live Server** é o ideal)  
4) Clicar em **“Gerar Senha”** e pronto ✅

> **Você NÃO precisa reinstalar as libs** toda vez. Só reinstale se apagar/recriar o `venv`:
> ```bash
> python3 -m venv venv
> source venv/bin/activate
> pip install -r requirements.txt
> ```

---

## 📡 Documentação da API

### `GET /generate`
Gera uma senha com base nos parâmetros.

**Exemplo**
```
GET http://127.0.0.1:5000/generate?length=16&upper=true&lower=true&digits=true&symbols=true
```

**Parâmetros (query)**
| Parâmetro | Tipo   | Default | Descrição                         |
|----------:|:------:|:-------:|-----------------------------------|
| `length`  | number |   12    | Tamanho da senha                  |
| `upper`   | bool   |  true   | Incluir letras maiúsculas         |
| `lower`   | bool   |  true   | Incluir letras minúsculas         |
| `digits`  | bool   |  true   | Incluir números                   |
| `symbols` | bool   |  true   | Incluir símbolos                  |

**Resposta (200)**
```json
{ "password": "A9!fP2#tG5@l" }
```

**cURL**
```bash
curl "http://127.0.0.1:5000/generate?length=20&upper=true&lower=true&digits=true&symbols=true"
```

---

## 🧩 Configuração (opcional)
Arquivo `backend/.env` (opcional):
```
FLASK_ENV=development
PORT=5000
```
No `app.py`, você pode ler essas variáveis com `python-dotenv` se quiser.

---

## 🧷 Troubleshooting

### 🔴 “Port 5000 is in use”
Outra aplicação está usando a porta.
```bash
lsof -i :5000
kill -9 <PID_que_aparecer>
# depois rode o Flask novamente
```
Ou troque a porta:
```bash
flask --app app:app run --port=5001 --debug
```

### 🔴 “No module named flask”
O `venv` não está ativo ou está vazio.  
Ative e reinstale:
```bash
source venv/bin/activate   # (ou source ../venv/bin/activate se estiver em /backend)
pip install -r requirements.txt
```

### 🔴 Front não gera a senha ao clicar
- Confirme se o back-end está rodando (**http://127.0.0.1:5000**).
- Prefira abrir o front com **Live Server** (evita bloqueio do `file://`).
- Veja o Console do navegador (F12) para erros de rede (CORS/Fetch).

---

## 🗺️ Próximos passos (Roadmap)
- Adicionar seletor de “força” da senha
- Botão para mostrar/ocultar senha
- Testes automatizados
- Dockerfile
- Deploy (Render/Railway) e página pública

---

## 👤 Autor
**Gabriel** — Estudante de Eng. de Software (PUC Campinas)  
Apaixonado por tecnologia, curioso e em busca do primeiro estágio 🚀
