from openai import OpenAI
import os
from dotenv import load_dotenv
from src.persona.persona_builder import PersonaBuilder
load_dotenv()


class GptApi():
    def __init__(self) -> None:
        self.OPENAI_TEMPERATURE       = int(os.getenv('OPENAI_TEMPERATURE'))
        self.OPENAI_MAX_TOKENS        = int(os.getenv('OPENAI_MAX_TOKENS'))
        self.OPENAI_FREQUENCY_PENALTY = int(os.getenv('OPENAI_FREQUENCY_PENALTY'))
        self.OPENAI_PRESENCE_PENALTY  = int(os.getenv('OPENAI_PRESENCE_PENALTY'))
        self.OPENAI_MODELO            = os.getenv('OPENAI_MODELO')
        self.CLIENT                   = OpenAI( api_key= os.getenv('OPENAI_API_KEY') )


    def m_conversa(self, persona: PersonaBuilder, pergunta: str):
        completion = self.CLIENT.chat.completions.create(
            model= self.OPENAI_MODELO,
            messages=[
                {"role": "system", "content": persona.m_get_contexto()},
                {"role": "user", "content": pergunta}
            ],
            temperature       = self.OPENAI_TEMPERATURE,
            max_tokens        = self.OPENAI_MAX_TOKENS,
            frequency_penalty = self.OPENAI_PRESENCE_PENALTY,
            presence_penalty  = self.OPENAI_PRESENCE_PENALTY
        )

        return completion.choices[0].message.content


    def m_criar_thread(self):
        thread =  self.CLIENT.beta.threads.create()
        print(thread)
        return thread
    

    def m_adicionar_msg_thread(self, thread, msg: str):
        message = self.CLIENT.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=msg
        )


    def m_run(self, thread, assistant_id):
        run = self.CLIENT.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=assistant_id,
            instructions=""
        )

        if run.status == 'completed': 
            messages = self.CLIENT.beta.threads.messages.list(
                thread_id=thread.id,

            )
            print(messages)
            return messages
        else:
            print(run.status)
            return "Falhou!!!"