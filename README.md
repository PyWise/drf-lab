# 🧠 Django DRF Learning Repo

Este é meu repositório de aprendizado pessoal, construído com **Django** e **Django REST Framework (DRF)**.  
Aqui eu aplico tudo o que estou aprendendo sobre construção de APIs RESTful com Python e Django.

---

## 🔧 O que aprendi e pratiquei

- ✅ **Function-Based Views (FBV)**
- ✅ **Class-Based Views (CBV)**
- ✅ **Mixins**
- ✅ **Generic Views**
- ✅ **ViewSets e Routers**
- ✅ **Nested Serializers**
- ✅ **Paginação**
- ✅ **Filtragem e Ordenação**
- ✅ **CRUD completo via API REST**

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/your-username/drf-lab.git
cd drf-lab
````

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate   # No Windows: venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Rode as migrações e inicie o servidor

```bash
python manage.py migrate
python manage.py runserver
```

### 5. Acesse o projeto

* API Root: [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)
* Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📁 Estrutura do Projeto

```
drf_lab/
├── api/             # App principal com views, serializers, urls
├── drf_lab/         # Configurações do projeto
├── manage.py
└── requirements.txt
```

---

## 🧪 Próximos Passos

* 🔒 Adicionar autenticação com JWT
* 📄 Adicionar documentação (Swagger ou drf-spectacular)
* ✅ Escrever testes automatizados
* 🐳 Adicionar suporte a Docker
* 🚀 Fazer deploy para uma plataforma (ex: Railway, Render)

---
