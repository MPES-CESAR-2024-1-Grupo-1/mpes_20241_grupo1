from openai import OpenAI
import os
from dotenv import load_dotenv
from src.persona.persona_builder import PersonaBuilder
import json
from flask import current_app

load_dotenv()

MENSAGEM_PARA_FORMATAR_EM_JSON_COM_METADADOS = '''Responda em formato json,
com todo o conteudo em um campo chamado resposta
e adicionando um outro campo chamado tema contendo o tema do conteudo solicitado'''

class GptApi():
    def __init__(self) -> None:
        self.OPENAI_TEMPERATURE       = 1
        self.OPENAI_MAX_TOKENS        = 4090
        self.OPENAI_FREQUENCY_PENALTY = 0
        self.OPENAI_PRESENCE_PENALTY  = 0
        self.OPENAI_MODELO            = "gpt-4o"
        self.CLIENT                   = OpenAI( api_key= "sk-proj-49cjrJazY5zqr0qmZ7V7T3BlbkFJ7w2Cr01MurzeyaOwHci3" )



    def m_conversa(self, persona: PersonaBuilder, pergunta: str, formato_json: bool=False):
        messages = [
            {"role": "system", "content": persona.m_get_contexto()},
            {"role": "user", "content": pergunta}
        ]
        if formato_json:
            messages.extend([
                { "role": "system", "content": MENSAGEM_PARA_FORMATAR_EM_JSON_COM_METADADOS}
            ])
        completion = self.CLIENT.chat.completions.create(
            model             = self.OPENAI_MODELO,
            messages          = messages,
            temperature       = self.OPENAI_TEMPERATURE,
            max_tokens        = self.OPENAI_MAX_TOKENS,
            frequency_penalty = self.OPENAI_PRESENCE_PENALTY,
            presence_penalty  = self.OPENAI_PRESENCE_PENALTY,
            response_format={"type": "json_object" if formato_json else "text"}
        )

        resposta = completion.choices[0].message.content
        current_app.logger.debug(f"Retorno openai: {resposta}")
        if formato_json:
            return json.loads(resposta)
        return resposta



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