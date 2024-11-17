import google.generativeai as genai
from dotenv import load_dotenv
import os

import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

def configure_api_key():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    genai.configure(api_key=api_key)

def create_prompt():
    return (
        "Quero que você retorne um JSON válido sobre o código fornecido. "
        "O JSON deve conter as seguintes chaves: "
        "'codigo', 'descricao', explicação  "
        "Em 'codigo': Deve conter o código fornecido. "
        "Em 'descricao': Uma breve descrição do que o código faz. "
        "Em 'explicacao': Uma explicação detalhada do código. "      
    )
 
def create_documentation(language, codigo, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"\n\n {codigo} em {language}, {prompt} \n\n")
    return response.text

def select_language_user(resposta_input_language):
    match resposta_input_language:
        case 1:
            return 'Python'
        case 2:
            return 'Java'
        case 3:
            return 'JavaScript'
        case 4:
            return 'C#'
        case _:
            return 'Invalid selection'

def prompt_user_language_input():
    valid_language_select = False
    while not valid_language_select:
        try:
            input_language_code_user = int(input("Digite o número correspondente à linguagem de programação desejada:\n1. Python\n2. Java\n3. JavaScript\n4. C#\n"))
            language_select = select_language_user(input_language_code_user)
            
            if language_select == 'Invalid selection':
                print("Por favor, insira um número válido.")
            else:
                valid_language_select = True
                return language_select
        except ValueError:
            print("Por favor, insira um número válido.")
            
def prompt_user_code_input():
    # input_code_user = input("Digite o código que você deseja documentar: \n")
    input_code_user = 'soma_lista(numeros): total = 0 \n for num in numeros: \ntotal = add\n(total, num) \nreturn total'
    return input_code_user

def format_json_string(json_string):
    # Remove as marcações de código
    formatted_string = json_string.replace("```json", "").replace("```", "").strip()
    return formatted_string

def generate_pdf(documentation):
    # configurar onde o arquivo gerado será salvo e nome do arquivo
    pdf_dir = os.path.join(os.path.dirname(__file__), 'pdf')
    os.makedirs(pdf_dir, exist_ok=True)
    pdf_path = os.path.join(pdf_dir, 'documentation.pdf')


    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Título
    title = Paragraph("Documentação do Código", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Adiciona o conteúdo da documentação
    try:
        documentation_dict = json.loads(documentation)  # Converte a string JSON para umdicionário
    except json.JSONDecodeError:
        print("Erro ao decodificar o JSON")
        return None

    for key, value in documentation_dict.items():
        subtitle = Paragraph(key.capitalize(), styles['Heading2'])
        elements.append(subtitle)
        elements.append(Spacer(1, 6))
        content = Paragraph(value, styles['BodyText'])
        elements.append(content)
        elements.append(Spacer(1, 12))

    doc.build(elements)
    return pdf_path

def main():
    configure_api_key()
    prompt = create_prompt()
    user_language_select = prompt_user_language_input()
    user_code = prompt_user_code_input()
    documentation = create_documentation(user_language_select, user_code, prompt)
    docJSON = format_json_string(documentation)
    pdf_path = generate_pdf(docJSON)
    if pdf_path:
        print(f"PDF gerado em: {pdf_path}")
    else:
        print(docJSON)

if __name__ == "__main__":
    main()