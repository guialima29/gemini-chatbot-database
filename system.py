# EN-US | This file just centralize the process of the 2 AIs 
# PT-BR | Esse arquivo centraliza apenas o processo das 2 IAs

from ia.chat import aiResponse
from ia.pre_prompt import firstCheck

def returnInfo(prompt):
    data = firstCheck(prompt)
    final = aiResponse(prompt,data)

    return final
