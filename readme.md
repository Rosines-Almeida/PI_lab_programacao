# Projeto de Geração de Documentação de Código

Este projeto utiliza a API do Google Generative AI para gerar documentação detalhada de código em várias linguagens de programação.

## Configuração do Ambiente

### 1. Clonar o Repositório

```bash
git clone https://github.com/Rosines-Almeida/PI_lab_programacao.git
cd seu-repositorio
```

### 2.Criar e Ativar um Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows use [activate](http://_vscodecontentref_/1) 
```
### 3. Instalar as Dependências

```bash
pip install -r [requirements.txt]
```

## Configuração da API Key do Google Generative AI

### 1. Obter a API Key
- Acesse o [Google Cloud Console](https://aistudio.google.com/app/apikey).
- Crie um novo projeto ou selecione um projeto existente.
- Ative a API do Google Generative AI.
- Navegue até a seção de credenciais e crie uma nova chave de API.
- Copie a chave de API gerada.

### 2. Configurar a API Key no Projeto
- Crie um arquivo `.env` na raiz do projeto e adicione a sua chave de API:

```bash
API_KEY=sua_chave_de_api_aqui
```

### 3. Executar o Script
- Para executar o script principal (`create.py`), use o seguinte comando:

```bash
python create.py
```

### 4. Inserir os Prompts
- O script solicitará que você insira a linguagem de programação e o código para o qual deseja gerar a documentação.
- Siga as instruções no terminal para fornecer as informações necessárias.

### Exemplo de Prompt
```bash
Digite o número correspondente à linguagem de programação desejada:
1. Python
2. Java
3. JavaScript
4. C#
```
Exemplo de código para inserir
```bash
Digite o código que você deseja documentar:
def add(a, b):\ return a + b
```
### Exemplo do retorno 

```json
{
  "codigo": "public class Main {\n  public static int add(int a, int b) {\n  return a + b;\n  }\n  public static void main(String[] args) {\n  int sum = add(5, 3);\n  System.out.println(\"A soma de 5 e 3 é: \" + sum);\n  }\n}",
  "descricao": "Esta função recebe dois inteiros como entrada e retorna a sua soma.",
  "explicacao": "A função `add(int a, int b)` recebe dois parâmetros inteiros, `a` e `b`. Ela então retorna a soma desses dois números usando o operador `+`. No exemplo do método `main`, a função `add` é chamada com os argumentos 5 e 3. A função retorna o valor 8, que é armazenado na variável `sum`. Em seguida, a variável `sum` é impressa no console.",
  "exemplo": "A função `add` pode ser usada para somar quaisquer dois números inteiros. Por exemplo, para adicionar 10 e 20, você chamaria a função da seguinte forma: `add(10, 20)`. Isso retornaria o valor 30." 
}
