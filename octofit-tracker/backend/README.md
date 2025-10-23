# OctoFit Tracker — Backend

Este diretório contém o backend Django do OctoFit Tracker.

Pré-requisitos
- Python 3.10+
- Git
- MongoDB (mongodb-org) em execução localmente ou em um host acessível

Passos rápidos

1. Criar e ativar o virtualenv (já incluso nesta workspace):

```bash
python3 -m venv octofit-tracker/backend/venv
source octofit-tracker/backend/venv/bin/activate
```

2. Instalar dependências:

```bash
pip install -r octofit-tracker/backend/requirements.txt
```

3. Configurar variáveis de ambiente para usar MongoDB (opções):

```bash
# Exemplo para MongoDB local
export MONGO_URI='mongodb://localhost:27017'
export MONGO_DB_NAME='octofit_db'

# Variáveis opcionais do Django
export DJANGO_SECRET_KEY='alguma-chave-secreta'
export DJANGO_DEBUG=1
```

4. Executar migrações e iniciar o servidor:

```bash
source octofit-tracker/backend/venv/bin/activate
python octofit-tracker/backend/manage.py migrate
python octofit-tracker/backend/manage.py runserver 0.0.0.0:8000
```

Notas sobre MongoDB e djongo
- O `djongo` permite usar o MongoDB como backend para o ORM do Django. É necessário ter o serviço MongoDB em execução (mongodb-org) e que a URI esteja correta.
- Em ambientes de produção, prefira um banco relacional suportado oficialmente pelo Django (PostgreSQL/MySQL) ou uma camada de persistência projetada para documentos.

Onde ir a partir daqui
- Implementar apps Django (users, activities, teams)
- Configurar autenticação (django-allauth / dj-rest-auth)
- Adicionar testes e CI
