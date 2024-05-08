# Crud Realizado em Python - Sprint 4 Salesforce

## Objetivo do Projeto

Este projeto tem como objetivo realizar um CRUD com o nosso banco de dados utilizando a matéria de python

Nosso projeto desenvolvimento em python vamos realizar o crud com a nossa tabela de suporte que representa um suporte que um usuário irá abrir pelo site

## Passo a Passo para rodar o projeto
Para rodar este projeto é necessário:

1. Instalar o Python: Verifique se você tem uma versão atualizada do Python instalada em seu sistema. Se não, você pode baixá-lo do site oficial do Python.

2. Clonar o repositório: Clone o repositório do projeto para o seu sistema local usando o comando `git clone`.
```bash
git clone https://github.com/yagoluucas/salesforce_sprint4_python.git
```

3. Instalar as dependências: Navegue até a pasta do projeto e instale as dependências necessárias usando o comando `pip install -r requirements.txt`.

4. Configurar o banco de dados: Configure o banco de dados para ter as tabelas necessárias para ser feito o CRUD. ao final do projeto, deixamos os comados SQL que serão responsáveis por criar a tabela no banco de dados.

5. Executar o arquivo main.py pela sua IDE de preferência ou via terminal

6. Ao Executar o arquivo é necessário inserir o usuário e senha do seu banco de dados oracle para poder realizar as operações do crud

## Funcionalidades

Neste CRUD será possível cadastrar, atualizar, deletar, listar todos os suportes, listar suporte pelo id do suporte, listar suporte pelo id do País

Além disso, será possível exportar a consulta gerando um arquivo JSON na qual o usuário poderá inserir o nome dele

No projeto a cada inserção de suporte será feito uma inserção na tabela de atividade do site que é uma tabela que representa toda atividade que temos no nosso site

## Script SQL para criação das tabelas

Para criar a tabela de **suporte** você pode usar o script abaixo
```sql
CREATE TABLE suporte (
    id_suporte        NUMBER GENERATED ALWAYS AS IDENTITY,
    nome_empresa      VARCHAR2(50),
    nome_pessoa       VARCHAR2(50),
    sobrenome_pessoa  VARCHAR2(100),
    descricao         VARCHAR2(500),
    id_pais           NUMBER(12) NOT NULL,
    CONSTRAINT suporte_pk PRIMARY KEY (id_suporte)
);
```

Para criar a tabela de **atividade do site** você pode usar o script abaixo
```sql
CREATE TABLE atividade_do_site (
    id_atividade    NUMBER GENERATED ALWAYS AS IDENTITY,
    oportunidade    CHAR(1),
    data            DATE,
    id_suporte      NUMBER(10),
    id_teste_gratis NUMBER(10),
    CONSTRAINT atividade_do_site_pk PRIMARY KEY (id_atividade)
);
```

Para criar a tabela de **pais** você pode usar o script abaixo
```sql
CREATE TABLE pais (
    id_pais   NUMBER GENERATED ALWAYS AS IDENTITY,
    descricao VARCHAR2(200),
    CONSTRAINT pais_pk PRIMARY KEY (id_pais)
);
```

Também temos nossa tabela de 'teste grátis', que é utilizada na tabela de atividades do site. No entanto, como ela não é obrigatória, não é necessário criá-la para que o sistema funcione.
