import google.generativeai as genai
from dotenv import load_dotenv
import os

#Configuração da chave de API
load_dotenv()
api_key = os.getenv("API_KEY")
#TODO : REMOVER API KEY  
#genai.configure(api_key="AIzaSyAoQsPcH8Yc0YWnl4bPTie3IjN_G96SLq4")
genai.configure(api_key=api_key)
 
 

# terminar o video 
# ver documentação
# ver se tem outro video 
#ja criar seus comando nesse arquivo  

# o que fazer com o codigo acima
# - pedir pra usuário adicionar o linguagem de programação(selecionar dar opções de escolha com números )
# - criar o input da pergunta
# - pedir pra usuário adicionar o código
#- fazer mockado estas informações priemiros
# - dar exemplo de como eu quero o retono
#-como esconder chave de api
#- fazer um kanban para organizar as tarefas (metodologia no trabalho - tirar print )
#- criar um projeto no github
#- criar um readme.md
#- 2 etapa integrar com html

#new test

def selectLanguageUser(respostaInputLanguege):
    if respostaInputLanguege == 1:
        return 'Python'
    if respostaInputLanguege == 2:
        return 'Java'
    if respostaInputLanguege == 3:
        return 'JavaScript'
    if respostaInputLanguege == 4:
        return 'C#'
    

#Método para gerar a documentação
model = genai.GenerativeModel("gemini-1.5-flash")
def create_documentation(linguage, codigo):
    response = model.generate_content(f"Escreva detalhe este codigo em  {linguage} , quero que retorne em tópico 1-Código, 2- Descrição 3- Exemplo: \n\n {codigo}")
    return response.text
 
# Dados do usuário  
#linguage_code_user = selectLanguageUser(3)
languageSelect = None
while languageSelect is None:
    try:
        input_linguage_code_user = int(input("Digite o número correspondente à linguagem de programação desejada:\n1. Python\n2. Java\n3. JavaScript\n4. C#\n"))
        languageSelect = selectLanguageUser(input_linguage_code_user)
        
        if languageSelect is None:
            raise ValueError("Por favor, insira um número válido.")

        codigo_usuario = 'def add(a, b): \n return a + b'
        response = print(create_documentation(languageSelect, codigo_usuario))
    except ValueError:
        print("Por favor, insira um número válido.")
        





