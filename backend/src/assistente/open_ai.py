from openai import OpenAI
import os

class Assistente:
    """
    Classe que representa um assistente de IA da OpenAI
    - Inicializa o assistente com as credenciais da OpenAI (OPEN_AI_API_KEY)
    - Necessita de um assistente_id para funcionar (OPEN_AI_ASSISTANT_ID)


    """
    def __init__(self):
        id_assistente = os.environ.get('OPENAI_ASSISTANT_ID')
        openai = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
        self.__assistente = openai.beta.assistants.retrieve(assistant_id=id_assistente)

    def responder(self, mensagem, contexto):
        return self.openai.responder(mensagem)
