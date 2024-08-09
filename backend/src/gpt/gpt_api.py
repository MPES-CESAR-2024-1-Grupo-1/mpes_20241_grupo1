from openai import OpenAI
import os
from dotenv import load_dotenv
from src.persona.persona_builder import PersonaBuilder
load_dotenv()


class GptApi():
    def __init__(self) -> None:
        self.OPENAI_TEMPERATURE       = 1
        self.OPENAI_MAX_TOKENS        = 4090
        self.OPENAI_FREQUENCY_PENALTY = 0
        self.OPENAI_PRESENCE_PENALTY  = 0
        self.OPENAI_MODELO            = "gpt-4o"
        self.CLIENT                   = OpenAI( api_key= "sk-proj-49cjrJazY5zqr0qmZ7V7T3BlbkFJ7w2Cr01MurzeyaOwHci3" )



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