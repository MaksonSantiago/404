# AssociOn 

Plataforma digital ágil para gestão de eventos solidários e captação de recursos. Desenvolvido para o curso de Análise e Desenvolvimento de Sistemas (Anhanguera).

##  Tecnologias
* **Backend:** Python + Django
* **Frontend:** Tailwind CSS + HTMX
* **Banco de Dados:** SQLite (Local)

---

##  Como configurar o ambiente de desenvolvimento local

Siga os passos abaixo estritamente nesta ordem para garantir que o seu ambiente fique isolado e não gere conflitos de versão com o restante da equipe.

### 1. Clonar o repositório
Abra o terminal na pasta onde deseja salvar o projeto e execute:
```bash
git clone <COLE_AQUI_O_LINK_DO_GITHUB>
cd associ_on


### 2. Criar e ativar o Ambiente Virtual (.venv)
Isso evita misturar as bibliotecas do projeto com as do seu computador.
```bash
# Cria o ambiente virtual
python -m venv .venv

# Ativa o ambiente no Windows:
.venv\Scripts\activate

# Ativa o ambiente no Mac/Linux:
source .venv/bin/activate

#Instalar as dependências do projeto
pip install -r requirements.txt

#Configurar o Banco de Dados local
python manage.py makemigrations
python manage.py migrate

#Rodar o servidor de testes
python manage.py runserver