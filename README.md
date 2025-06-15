# 🏋️‍♂️ API de Exercícios para Academia

Esta API foi desenvolvida com o objetivo de gerenciar uma lista de exercícios físicos, permitindo o cadastro de nome, descrição e URL de vídeo demonstrativo. Ideal para academias, personal trainers e plataformas fitness que desejam oferecer instruções claras e acessíveis.

---

## 🚀 Tecnologias Utilizadas

- **Linguagem**: Python
- **Framework Web**: FastAPI
- **Banco de Dados**: SQL (via SQLAlchemy)
- **Autenticação**: OAuth2 com JWT
- **Middleware**: CORS

#  Como Rodar Localmente

# Clone o repositório
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
uvicorn main:app --reload
