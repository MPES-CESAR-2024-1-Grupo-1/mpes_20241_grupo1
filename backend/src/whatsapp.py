import requests
import os
from logging import Logger

class WhatsApp:

    def __init__(self,  mensagem_recebida, logger: Logger):
        self.token = os.environ['WHATSAPP_AUTH_TOKEN']
        self.logger = logger
        evento = (
            mensagem_recebida.get("entry", [{}])[0]
            .get("changes", [{}])[0]
            .get("value", {})
        )
        self.mensagem_recebida = evento.get('messages', [{}])[0]
        self.numero_de_telefone_do_assistente = evento.get('metadata', {}).get('phone_number_id', '')
        self.numero_de_telefone_do_professor = self.mensagem_recebida.get('from', '')
        self.api_url = f"https://graph.facebook.com/v18.0/{self.numero_de_telefone_do_assistente}/messages"
        self.logger.debug(f"[whatsapp] Mensagem recebida de {self.numero_de_telefone_do_professor}: {mensagem_recebida}")


    def texto_da_mensagem_recebida(self):
        return self.mensagem_recebida.get('text', {}).get('body', '')

    def mensagem_recebida_eh_valida(self):
        return self.texto_da_mensagem_recebida() != ''

    def __id_da_mensagem_recebida(self):
        return self.mensagem_recebida.get('id', '')

    def __envie_mensagem(self, objeto_mensagem):
        self.logger.debug(f"[whatsapp] enviando {objeto_mensagem} para:{self.numero_de_telefone_do_professor} usando {self.api_url}")
        resposta = requests.post(
            self.api_url,
            headers={'Authorization': f'Bearer {self.token}'},
            json=objeto_mensagem
        )
        self.logger.debug(f"[whatsapp] resposta: [{resposta.status_code}] {resposta.json()}")
        return resposta

    def marque_mensagem_como_lida(self):
        self.__envie_mensagem({
            'messaging_product': 'whatsapp',
            'status': 'read',
            'message_id': self.__id_da_mensagem_recebida(),
        })

    def responda_mensagem(self, texto_da_mensagem):
        self.__envie_mensagem({
            'messaging_product': 'whatsapp',
            'to': self.numero_de_telefone_do_professor,
            'text': {'body': texto_da_mensagem}
        })
