
 
# ver documentação
# ver se tem outro video 
#ja criar seus comando nesse arquivo  

# o que fazer com o codigo acima
 
 
# - dar exemplo de como eu quero o retono do codigo
#- fazer um kanban para organizar as tarefas (metodologia no trabalho - tirar print )

#- criar um readme.md
#- 2 etapa integrar com html

#new test

import google.generativeai as genai
from dotenv import load_dotenv
import os

def configure_api_key():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    genai.configure(api_key=api_key)

def select_language_user(resposta_input_language):
    languages = {
        1: 'Python',
        2: 'Java',
        3: 'JavaScript',
        4: 'C#'
    }
    return languages.get(resposta_input_language, 'Invalid selection')

def create_documentation(language, codigo, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"\n\n {codigo} em {language}, {prompt} \n\n {codigo}")
    # response = model.generate_content(f"Quero um retorne soment Json  sobre este códigoo em {language}, quero que retorne em JSON com key codigo, descricao, explicacao e  exemplo: \n\n {codigo}")
    return response.text

def create_prompt():
    return "Quero que você retorne somente JSON sobre o código, as keys serão codigo', 'descricao', 'explicacao' e'exemplo'. Em codigo': Deve conter o código fornecido descricao  Uma breve descrição do que o código faz. explicacao: Uma explicação detalhada do código. exemplo': Um exemplo prático de como o código pode ser utilizado, incluindo exemplos de uso e o retorno esperado."

def prompt_user_language_input():
    while True:
        try:
            input_language_code_user = 1
            # input_language_code_user = int(input("Digite o número correspondente à linguagem de programação desejada:\n1. Python\n2. Java\n3. JavaScript\n4. C#\n"))
            language_select = select_language_user(input_language_code_user)
            
            if language_select == 'Invalid selection':
                raise ValueError("Por favor, insira um número válido.")
            
            return language_select
        except ValueError:
            print("Por favor, insira um número válido.")

def prompt_user_code_input():
    input_code_user = 'def add(a, b): \n return a + b'
    #input_code_user = input("Digite o código que você deseja documentar: \n")
    return input_code_user


def main():
    configure_api_key()
    prompt = create_prompt()
    user_language_select = prompt_user_language_input()
    user_code = prompt_user_code_input()
    documentation = create_documentation(user_language_select, user_code,prompt )
    print(documentation)

if __name__ == "__main__":
    main()