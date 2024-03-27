# Manipulação de Banco de Dados SQLite

Como desenvolvedor em uma empresa de consultoria de software, fui alocado para construir uma solução parametrizável capaz de interagir com bancos de dados SQLite. A solução deve oferecer as seguintes funcionalidades:

1. **Criação de Banco de Dados**: É possível criar um novo banco de dados informando apenas o nome desejado.
    
2. **Criação e Exclusão de Tabelas**: A solução permite criar e excluir tabelas em um banco de dados SQLite. Para criar uma nova tabela, é necessário informar o nome do banco que receberá a tabela e a DDL de criação. Para excluir uma tabela, basta fornecer o nome do banco e o nome da tabela.
    
3. **CRUD (Create, Read, Update, Delete)**: A solução é capaz de realizar as operações CRUD em um banco SQLite, sendo todas parametrizáveis. As operações disponíveis são:
    
    - **Inserir Registro**: Para inserir um novo registro em uma tabela, é necessário informar o nome do banco e da tabela, além de um dicionário contendo os campos e valores a serem inseridos.
    - **Recuperar Dados**: É possível recuperar os dados de uma tabela fornecendo o nome do banco e da tabela.
    - **Atualizar Registro**: Para atualizar um registro em uma tabela, é necessário informar o nome do banco e da tabela, além de dois dicionários: um contendo os campos e valores a serem atualizados e outro contendo os campos e valores da condição de busca.
    - **Excluir Registro**: Para excluir um registro em uma tabela, é necessário informar o nome do banco e da tabela, além de um dicionário contendo os campos e valores da condição de busca.

Com essa solução, é possível realizar operações de manipulação de banco de dados SQLite de forma flexível e parametrizável, atendendo às necessidades de diferentes contextos de uso.

##

## Estrutura do Projeto

- `main.py`
- `README.md`
- `src/`
    - `ddl/`
        - `ddl_sqlite.py`
    - `crud/`
        - `crud_sqlite.py`


Na estrutura acima:

- `main.py`: É o arquivo principal do projeto onde são realizadas as operações de manipulação do banco de dados.
- `README.md`: Documentação do projeto que descreve sua funcionalidade e estrutura.
- `src/`: Diretório que contém o código-fonte do projeto.
    - `ddl/`: Diretório que contém o módulo para manipulação de DDL (Data Definition Language).
        - `ddl_sqlite.py`: Módulo contendo a classe `DDLSQLite` para criação e exclusão de bancos e tabelas.
    - `crud/`: Diretório que contém o módulo para manipulação de CRUD (Create, Read, Update, Delete).
        - `crud_sqlite.py`: Módulo contendo a classe `CrudSQLite` para operações de inserção, leitura, atualização e exclusão de registros.

##

### Passos do Desenvolvimento

1. **Análise de Requisitos**: Iniciando o processo entendendo as necessidades do cliente e os requisitos do projeto. Identificando a necessidade de uma solução que pudesse criar bancos de dados, gerenciar tabelas e realizar operações de CRUD de forma parametrizável.
    
2. **Estruturação do Projeto**: Para garantir uma organização adequada do código-fonte, sendo dividido o projeto em módulos distintos. Criando os diretórios `ddl` e `crud` dentro da pasta `src`, onde cada um é responsável por lidar com as operações relacionadas à definição de dados e à manipulação de registros, respectivamente.
    
3. **Implementação da Funcionalidade DDL**: No módulo `ddl_sqlite.py`, foi desenvolvida a classe `DDLSQLite`, que oferece métodos para criar e excluir bancos de dados e tabelas. 
    
4. **Implementação da Funcionalidade CRUD**: No módulo `crud_sqlite.py`, foi criada a classe `CrudSQLite`, que possibilita as operações de inserção, leitura, atualização e exclusão de registros em tabelas do banco de dados. 
    
5. **Integração com o Código Principal**: No arquivo `main.py`, foi integrada a classe `CrudSQLite` para demonstrar o uso da solução em um contexto prático. 
