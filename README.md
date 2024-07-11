# My Project

## Descrição

Este projeto é um sistema de gerenciamento de cardápio e produtos para um café.

## Funcionalidades

- Visualização do cardápio na página inicial
- Adição, edição e exclusão de produtos na área administrativa
- Geração de relatórios de produtos

## Como rodar o projeto

1. Clone o repositório:
    ```sh
    git clone https://github.com/Yuriwinchest/my_project.git
    cd my_project
    ```

2. Crie um ambiente virtual e instale as dependências:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
    pip install -r requirements.txt
    ```

3. Execute a aplicação:
    ```sh
    python app.py
    ```

4. Acesse o aplicativo no navegador:
    ```
    http://127.0.0.1:5000
    ```

## Estrutura do projeto

- `app.py`: Arquivo principal da aplicação Flask.
- `templates/`: Contém os arquivos HTML.
- `static/`: Contém arquivos CSS e imagens.
- `models.py`: Define os modelos de dados.
- `database.py`: Configuração do banco de dados.

## Contribuição

Sinta-se à vontade para contribuir com o projeto. Abra uma issue ou faça um pull request.
