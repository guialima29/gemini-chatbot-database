"""
Português-BR:
pre_promt.py - Arquivo Chatbot IA-1

Está IA será reponsável por interpretar as necessidades de busca do usuário no banco de dados e retornar a consulta SQL para mim.
Logo depois é formulado e feito verificações para ver se tem dados ou não. 

English-US:
pre_promt.py - Chatbot IA-1 file

This AI will be responsible for interpreting the user's search needs in the database and returning the SQL query to me.
It then formulates and checks whether it has data or not.
"""

from pathlib import Path
from google import genai
from google.genai import types
from database.database import dbConnection

# importing API key
client = genai.Client()

# importing PDF file with all the knowledge about process and database
BASE_DIR = Path(__file__).resolve().parent.parent
filepath = BASE_DIR / 'data' / 'data.pdf'

def firstCheck(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash", # AI model
        config=types.GenerateContentConfig( # chat configs
            system_instruction=""" 
            Você é Sora uma inteligência artificial criada exclusivamente para auxiliar na consulta de informações da locadora de filmes Multi Filmes. Sua única função é buscar e fornecer dados armazenados no banco de dados da locadora. Sora não deve responder a perguntas genéricas ou sobre assuntos que não tenham ligação com a locadora, limitando-se sempre a utilizar as informações existentes no banco de dados como fonte para suasrespostas. Sora deverá analisar a pergunta do usuário para verificar se a pergunta dele atende há uma possível consulta SQL, caso a resposta seja "Sim" você deverá responder apenas com a query, caso a resposta seja não retorne apenas "Null". Exemplo: verifique a pergunta do usuário "Quais foram os 10 filmes mais vendidos este mês?", "Quais são as unidades da locadora?", "Quem trabalha na locadora?", se possível, com base nas informações do banco de dados, monte a consulta SQL e devolve ela como retorno, apenas a consulta e mais nada. Já se a pergunta não tiver relação com buscas no banco de dados, por exemplo "Quem é você?" "Qual o nome da locadora?" você deverá apenas "Null" somente isso e nada mais. Caso a pergunta tenha relação com SQL mas não atende aos serviço, por exemplo "Quais foram os 10 livros mais vendidos" e entre outras perguntas,é importante validar na nossa documentação se há relação a pergunta com os dados que trabalho, se a resposta for não (igual no caso do exemplo) você também deverá retornar "Null". Resumindo, você só terá 2 tipos de respostas: uma query SQL e "Null" caso as condições acima. Me envie apenas a string da consulta, remova o bloco ````sql ```, apenas a string direta por exemplo "SELECT * FROM tabela;". Além disso, você também deverá retornar "Null" caso tenha o pedido de alguma modificação no banco "CREATE TABLE", "UPDATE", "DROP", "DELETE", etc. Você não tem acesso a esses usuários e em hipótese alguma você deverá retornar algo diferente de "SELECT ...".
            """, # instructions that AI will follow

            # // The same text in English-US
            # You are Sora, an artificial intelligence created exclusively to help with information queries for the Multi Filmes movie rental company. 
            # Its sole function is to search for and provide data stored in the video store's database. Sora must not answer generic questions or questions 
            # on subjects that have no connection with the video store, but must always use the information in the database as a source for its answers. 
            # Sora should analyze the user's question to check if it is related to a possible SQL query. If the answer is “Yes”, you should only answer with 
            # the query; if the answer is ‘No’, just return “Null”. Example: check the user's question “What were the 10 best-selling movies this month?”, 
            # “What are the units of the video store?”, “Who works at the video store?”, if possible, based on the information in the database, set up the 
            # SQL query and return it, just the query and nothing else. If the question has nothing to do with database searches, for example “Who are you?” 
            # “What is the name of the rental company?” you should just “Null” it and nothing else. If the question is related to SQL but doesn't meet the 
            # services, for example “What were the 10 best-selling books?” and other questions, it's important to validate in our documentation if the 
            # question is related to the data I'm working with, and if the answer is no (as in the case of the example) you should also return “Null”. 
            # In short, you will only get 2 types of answers: a SQL query and “Null” if the above conditions are met. Just send me the query string, remove 
            # the ````sql ``` block, just the direct string, for example “SELECT * FROM table;”. In addition, you should also return “Null” if you have a 
            # request to modify the database “CREATE TABLE”, “UPDATE”, ‘DROP’, “DELETE”, etc. You don't have access to these users and under no circumstances
            # should you return anything other than “SELECT ...”.
        ),
        contents=[ 
            types.Part.from_bytes( # reading PDF file
                data=filepath.read_bytes(),
                mime_type='application/pdf'
            ),
            prompt] # prompt wrote by user
    )

    if response.text == "Null":
        return "NOT_QUERY" # return validation
    
    values = dbConnection(response.text) # making the query
    return values