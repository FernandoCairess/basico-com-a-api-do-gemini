import os 
import google.generativeai as g
from dotenv import load_dotenv

load_dotenv() #

CHAVE_API_KEY = os.getenv('GEMINI_API_KEY')

g.configure(api_key=CHAVE_API_KEY)
MODELO_ESCOLHIDO = 'gemini-1.5-flash'

prompt_sistema = 'Liste apenas os nomes dos produtos, e ofereca uma breve descricao de cada um.'

llm = g.GenerativeModel(
    model_name = MODELO_ESCOLHIDO,
    system_instruction= prompt_sistema,

)

pergunta = 'liste tres prdotudos de moda sustentavel para ir ao shopping'

resposta = llm.generate_content(pergunta)
print(resposta.text)