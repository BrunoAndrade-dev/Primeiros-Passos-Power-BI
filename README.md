# Analise de Dados de Vendas de Videogames

Este projeto consiste em uma esteira de dados completa para o processamento e visualizacao de informacoes sobre o mercado de videogames. O fluxo abrange desde a limpeza de dados brutos com Python ate a criacao de um painel interativo no Power BI, utilizando SQL como camada intermediaria de armazenamento.

### Objetivo

O sistema foi desenvolvido para responder perguntas de negocio fundamentais, como a identificacao das plataformas com maior volume de vendas, os generos de jogos dominantes e a evolucao temporal do mercado global de games.

### Estrutura do Projeto

A organizacao do repositorio reflete as etapas do processo de BI:

Data: Contem o arquivo vgsales.csv original com dados de vendas globais.
Notebooks: Documentacao de testes, exploracao inicial de dados e validacao de consultas SQL.
src: Scripts Python responsaveis pela limpeza de dados (data_cleaning.py) e gerenciamento do banco de dados (database_manager.py).
vendas_games.db: Arquivo de banco de dados SQLite gerado pelo processamento do Python.
Relatorio: Arquivo de extensao .pbix contendo o dashboard interativo.

### Requisitos do Sistema

Para reproduzir este ambiente, sao necessarias as seguintes ferramentas:

Python 3.12 ou superior.
Bibliotecas Pandas e Sqlite3.
Power BI Desktop.
Ambiente Virtual (venv) configurado para isolamento de dependencias.

### Como Executar o Projeto

.Em breve passo a passo e adição do arquivo .pbx para abrir no BI

### Tecnologias Utilizadas

Python: Manipulacao, limpeza e automacao do fluxo de dados.
SQL (SQLite): Armazenamento estruturado e execucao de queries de negocio.
Power BI: Visualizacao de dados e criacao de dashboards interativos.
