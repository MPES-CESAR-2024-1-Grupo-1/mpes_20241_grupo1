import requests
from flask import current_app
import os

class WhatsApp:

    def __init__(self,  mensagem_recebida):
        self.token = os.environ['WHATSAPP_AUTH_TOKEN']
        evento = (
            mensagem_recebida.get("entry", [{}])[0]
            .get("changes", [{}])[0]
            .get("value", {})
        )
        self.mensagem_recebida = evento.get('messages', [{}])[0]
        self.numero_de_telefone_do_assistente = evento.get('metadata', {}).get('phone_number_id', '')
        self.numero_de_telefone_do_professor = self.mensagem_recebida.get('from', '')
        self.api_url = f"https://graph.facebook.com/v18.0/{self.numero_de_telefone_do_assistente}/messages"


    def texto_da_mensagem_recebida(self):
        return self.mensagem_recebida.get('text', {}).get('body', '')

    def __id_da_mensagem_recebida(self):
        return self.mensagem_recebida.get('id', '')

    def __enviar_mensagem_ao_whatsapp(self, objeto_mensagem):
        current_app.logger.debug(f"[whatsapp] enviando {objeto_mensagem} para:{self.numero_de_telefone_do_professor} usando {self.api_url}")
        resposta = requests.post(
            self.api_url,
            headers={'Authorization': f'Bearer {self.token}'},
            json=objeto_mensagem
        )
        current_app.logger.debug(f"[whatsapp] resposta: [{resposta.status_code}] {resposta.json()}")
        return resposta

    def marcar_como_lida(self):
        self.__enviar_mensagem_ao_whatsapp({
            'messaging_product': 'whatsapp',
            'status': 'read',
            'message_id': self.__id_da_mensagem_recebida(),
        })

    def responder_mensagem(self, texto_da_mensagem):
        self.__enviar_mensagem_ao_whatsapp({
            'messaging_product': 'whatsapp',
            'to': self.numero_de_telefone_do_professor,
            'text': {'body': texto_da_mensagem}
        })
