import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
#TODO : REMOVER API KEY  
#genai.configure(api_key="AIzaSyAoQsPcH8Yc0YWnl4bPTie3IjN_G96SLq4")
genai.configure(api_key=api_key)
 
# work
# genai.configure(api_key="AIzaSyAoQsPcH8Yc0YWnl4bPTie3IjN_G96SLq4")

# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Escreva detalhe este codigo em  Python , quero que retorne em tópico 1-código, 2- descrição 3- exemplo: \n\n def add(a,b): \n return a+b")
# print(response.text)

# terminar o video 
# ver documentação
# ver se tem outro video 
#ja criar seus comando nesse arquivo 
# tentar passar para um pasta novo (ver como criar um projeto pythom )

# o que fazer com o codigo acima
# - pedir pra usuário adicionar o linguagem de programação
# - pedir pra usuário adicionar o código
#- fazer mockado estas informações priemiros
# - dar exemplo de como eu quero o retono
#-como esconder chave de api
#- fazer um kanban para organizar as tarefas (metodologia no trabalho - tirar print )
#- criar um projeto no github
#- criar um readme.md
#- 2 etapa integrar com html

#new test



model = genai.GenerativeModel("gemini-1.5-flash")
def create_documentation(linguage, codigo):
    response = model.generate_content(f"Escreva detalhe este codigo em  {linguage} , quero que retorne em tópico 1-Código, 2- Descrição 3- Exemplo: \n\n {codigo}")
    return response.text
 

linguage_code_user = 'Python'
codigo_usuario =  'def add(a,b): \n return a+b'
response = print(create_documentation(linguage_code_user, codigo_usuario))