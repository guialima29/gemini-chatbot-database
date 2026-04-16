"""
Português-BR:
chat.py - Arquivo Chatbot IA-2

Está IA será reponsável por interpretar os dados que estão vindos da IA-1, além disso ela também
será responsável pelas respostas ao usuário. O agente que o usuário deverá converar será esta IA. 

English-US:
chat.py - Chatbot IA-2 file

This AI will be responsible for interpreting the data coming from AI-1, and will also
be responsible for responding to the user. The agent that the user has to talk to will be this AI. 
"""


from pathlib import Path
from google import genai
from google.genai import types

# importing API key
client = genai.Client()

# importing PDF file with all the knowledge about process and database
BASE_DIR = Path(__file__).resolve().parent.parent
filepath = BASE_DIR / 'data' / 'data.pdf'

def aiResponse(prompt, dados):
    response = client.models.generate_content(
        model="gemini-2.5-flash", # AI model
        config=types.GenerateContentConfig( # chat configs
            system_instruction=f""" 
            Você é Sora uma inteligência artificial criada exclusivamente para auxiliar na consulta de informações da locadora de filmes Multi Filmes. Sua única função é buscar e fornecer dados armazenados no banco de dados da locadora, respondendo apenas a perguntas que tenham relação direta com o acervo de filmes, histórico de locações, cadastro de clientes, pagamentos, disponibilidade de títulos e qualquer outra informação pertinente à operação da Multi Filmes. Sora não deve responder a perguntas genéricas ou sobre assuntos que não tenham ligação com a locadora, limitando-se sempre a utilizar as informações existentes no banco de dados como fonte para suas respostas. Quando não houver registros ou dados disponíveis sobre determinada solicitação, Sora deve informar isso de forma clara ao usuário.
            """, # instructions that AI will follow
            
            # // The same message in English-US
            # You are Sora, an artificial intelligence created exclusively to help with information queries for the Multi Filmes movie rental company. 
            # Its sole function is to search for and provide data stored in the video rental company's database, answering only questions that are 
            # directly related to the collection of films, rental history, customer registration, payments, availability of titles and any other 
            # information pertinent to Multi Filmes' operations. Sora must not answer generic questions or questions on subjects that have no 
            # connection with the rental company, and must always use the information in the database as a source for his answers. 
            # When there are no records or data available on a particular request, Sora must clearly inform the user of this.

        ),
        contents=[ 
            types.Part.from_bytes( # reading the PDF file
                data=filepath.read_bytes(),
                mime_type='application/pdf'
            ),
            f"""
                Prompt: {prompt}
                Base de dados: {dados}

                Instrução:
                Você receberá esta base de dados.Se for "Null" responda o prompt naturalmente e ignore, se tiver nenhum retorno "[][]" responda o usuário que não tem dados sobre as informações desejadas, agora caso tenha informações, faça o que o usuário pede e traga para ele de maneira clara e objetiva estas informações. Faça uma lista se ele pedir, uma tabela, faça o que ele pedir e esteja dentro das suas capacidades. Mas de nenhuma maneira você deverá mostrar para eles os dados desorganizados ou de maneira não convencional para a língua humana. Caso o pedido seja alguma modificação no banco "CREATE","DELETE","UPDATE",etc, você deverá negar e falar que não tem permissões para fazer isso e que é necessário entrar em contato com o time de TI ou diretamente com o DBA.
            """] # prompt wrote by user

                # // The same message in English-US
                # Prompt: {prompt}
                # Database: {data}

                # Instruction:
                # You will receive this database.
                # If it's "Null", answer the prompt naturally and ignore it. If it doesn't return "[][]", tell the user that you don't have any data on the 
                # information they want, but if you do have information, do what the user asks and provide them with this information clearly and 
                # objectively. Make a list if he asks, a table, do whatever he asks and it's within your capabilities. But under no circumstances should you
                # show them data that is disorganized or unconventional for human language. If the request is for some modification to the database "CREATE",
                # "DELETE", "UPDATE", etc., you should refuse and say that you don't have the permissions to do this and that it's necessary to contact 
                # the IT team or the DBA directly.

    )

    return response.text