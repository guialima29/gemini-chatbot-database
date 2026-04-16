"""
Portuguese-BR:
database.py - Conexão e acesso ao banco de dados

Essa parte do código é responsável por fazer uma consulta que foi feita pelo primeiro AI e retornar os valores do banco de dados.
Estou usando um banco de dados Postgres com Pagila Sample

English-US:
database.py - Connection and access to database

This part of code is responsible to make a query that was made by the first AI and return the values of database.
I'm using a Postgres database with Pagila Sample
"""

import psycopg2
from dotenv import load_dotenv 
import os 

load_dotenv() 

# setup environment variables
DBUSER = os.getenv("DB_USER")
DBPASS = os.getenv("DB_PASS")
DBHOST = os.getenv("DB_HOST")
DBPORT = os.getenv("DB_PORT")
DBNAME = os.getenv("DB_NAME")

# function that connect to database and make querys
def dbConnection(query):
    try:
        conn = psycopg2.connect(
            host=DBHOST,
            database=DBNAME,
            user=DBUSER,
            password=DBPASS
        )

        cur = conn.cursor() # open cursor
        cur.execute(query) # execute query
        query_return = cur.fetchall() # get all data

        cur.close() # close cursor
        conn.close() # close connection

        return query_return

    except psycopg2.Error as e:
        print(f"Erro: {e}")