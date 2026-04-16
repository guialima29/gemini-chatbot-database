# AI Model Integrated with Database

<div align="center">

| <img height="120" width="120" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Google_Gemini_icon_2025.svg/250px-Google_Gemini_icon_2025.svg.png" /> | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | <img height="120" width="140" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg" /> | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | <img height="120" width="140" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" /> |
|:---:|:---:|:---:|:---:|:---:|

</div>

<br>

**PT-BR**

Este é um código de estudo para a integração do agente de inteligência artificial Gemini junto com um banco de dados estruturado. Modelo simples que consiste em analisar o prompt do usuário e responder ele buscando as informações necessárias na base de dados.

O projeto foi desenvolvido pensando em ser ampliado no futuro, isto é apenas uma base, e também foi projetado para rodar em um [Data Warehouse](https://aws.amazon.com/what-is/data-warehouse/) (DW).

Este é um código de estudo para usar modelos de IA para conectar bancos de dados e processar dados. Fiz o “frontend” e o “backend” no mesmo projeto e em Python, mas recomendo fazer esse backend em Python (usando Flask, Django, FastAPI ou qualquer outro) e usar o frontend com outra linguagem (como TypeScript, JavaScript, Ruby... ou outras linguagens). Porque, na minha opinião, os frameworks de front-end do Python não oferecem muita personalização. Mas você é livre para fazer o que quiser.

A aplicação foi desenvolvida em Python, utilizando:

- Streamlit como backend para criar uma interface interativa.
- psycopg2 para conexão e leitura do banco de dados.
- Gemini como agente de IA para interpretar perguntas e gerar insights a partir dos dados.

O banco de dados utilizado é o Pagila, um sample baseado no clássico Sakila, adaptado para PostgreSQL. O Pagila simula uma locadora de filmes, com tabelas de clientes, filmes, inventário, pagamentos, entre outros.
Este repositório é voltado para fins de estudo e demonstração de integração entre IA e banco de dados relacional.

<br>

**EN-US**

This is a study code for integrating the Gemini artificial intelligence agent with a structured database. The simple model consists of analyzing the user's prompt and answering it by searching for the necessary information in the database.

The project was developed with a view to being extended in the future, this is just a base, and it was also designed to run on a [Data Warehouse](https://aws.amazon.com/what-is/data-warehouse/) (DW).

This is a study code for using AI models to connect databases and process data. I made the "frontend" and "backend" on the same project and in Python, but I recommend making this backend in Python (using Flask, Django, FastAPI, or whatever) and using the frontend with another language (like TypeScript, JavaScript, Ruby... or other languages). Because, in my opinion, the Python frontend frameworks don't offer so much customization. But you're free to make what you want.

The application is developed in Python, using:
- Streamlit as the backend to build an interactive interface.
- psycopg2 for database connection and querying.
- Gemini as the AI agent to interpret user questions and generate insights from the data.

The database used is Pagila, a sample inspired by the classic Sakila database and adapted for PostgreSQL. Pagila simulates a video rental store, with tables for customers, films, inventory, payments, and more. This repository is intended for educational purposes and as a demonstration of how AI can be integrated with a relational database.

<div align="center">
<img src="https://raw.githubusercontent.com/guialima29/reading-database-with-ia/refs/heads/main/_diagrams/flow-diagram.png"/>
<img src="https://raw.githubusercontent.com/guialima29/reading-database-with-ia/refs/heads/main/_diagrams/process-diagram.png"/>
<img src="https://raw.githubusercontent.com/guialima29/reading-database-with-ia/refs/heads/main/_diagrams/execution-map-diagram.png"/>
</div>
