Galeria de fotos com Django e Tailwind CSS.
Este é um projeto de uma galeria de fotos de viagens simples, desenvolvido com Django para o back-end e Tailwind CSS para a estilização do front-end. O projeto permite a criação, visualização e gerenciamento de fotos de forma dinâmica, utilizando um painel de administração integrado.

Tecnologias Utilizadas
Django: Framework web Python de alto nível que incentiva o desenvolvimento rápido e um design limpo e pragmático.

Tailwind CSS: Framework CSS de utilitários que permite a criação de designs customizados de forma rápida. Neste projeto, a versão CDN do Tailwind é utilizada para simplicidade, sem a necessidade de um processo de build complexo.

Python: Linguagem de programação principal.

Pillow: Biblioteca Python para manipulação de imagens, necessária para fazer o upload de fotos.

Como Rodar o Projeto
Siga estes passos para configurar e executar o projeto em seu ambiente local.

1. Clonar o Repositório
Primeiro, clone este repositório para a sua máquina usando o Git.

Bash

git clone https://github.com/seu-usuario/seu-repositorio.git
cd galeria-django
2. Configurar o Ambiente Virtual (VENV)
É altamente recomendado usar um ambiente virtual para isolar as dependências do projeto.

Bash

# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# No Windows
venv\Scripts\activate

# No macOS/Linux
source venv/bin/activate
3. Instalar as Dependências
Com o ambiente virtual ativado, instale as bibliotecas Django e Pillow listadas no arquivo requirements.txt (caso você já o tenha criado) ou diretamente:

Bash

pip install Django Pillow
4. Rodar as Migrações do Banco de Dados
Aplique as migrações para criar a estrutura do banco de dados necessária para o projeto.

Bash

python manage.py makemigrations fotos
python manage.py migrate
5. Criar um Superusuário
Para acessar o painel de administração e adicionar fotos, crie um superusuário.

Bash

python manage.py createsuperuser
Siga as instruções para definir seu nome de usuário, e-mail e senha.

6. Iniciar o Servidor de Desenvolvimento
Agora, você pode iniciar o servidor local.

Bash

python manage.py runserver
O projeto estará acessível em http://127.0.0.1:8000/.

Uso da Aplicação
Galeria de Fotos: Acesse http://127.0.0.1:8000/ para ver a galeria.

Painel de Administração: Acesse http://127.0.0.1:8000/admin/ para fazer login com o superusuário e adicionar novas fotos.

Contribuições
Sinta-se à vontade para abrir issues ou pull requests se tiver alguma sugestão de melhoria para o projeto.