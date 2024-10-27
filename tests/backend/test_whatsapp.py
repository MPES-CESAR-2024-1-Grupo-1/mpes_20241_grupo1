import unittest
from unittest.mock import patch
from backend.src.whatsapp import WhatsApp
import os
class TestWhatsApp(unittest.TestCase):

    @patch('logging.Logger')
    def setUp(self, mock_logger):
        self.environ_patch = patch.dict(os.environ, {
            'WHATSAPP_AUTH_TOKEN': 'token'
        })
        self.environ_patch.start()
        self.logger = mock_logger
        self.msg = msg = {
            "object": "whatsapp_business_account",
            "entry": [
                {
                    "id": "0",
                    "changes": [
                        {
                            "field": "messages",
                            "value": {
                                "messaging_product": "whatsapp",
                                 "metadata": {
                                    "display_phone_number": "16505551111",
                                    "phone_number_id": "123456123"
                                },
                                "messages": [
                                    {
                                        "from": "16315551181",
                                        "id": "ABGGFlA5Fpa",
                                        "timestamp": "1504902988",
                                        "type": "text",
                                        "text": {
                                            "body": "this is a text message"
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }

    def tearDown(self):
        self.environ_patch.stop()

    def test_whatsapp_funciona_com_mensagem_recebida_do_webhook(self):
        whatsApp = WhatsApp(self.msg, self.logger)
        self.assertEqual(whatsApp.texto_da_mensagem_recebida(), "this is a text message")
        self.assertEqual(whatsApp.mensagem_recebida_eh_valida(), True)
        self.assertEqual(whatsApp.numero_de_telefone_do_professor, '16315551181')
        self.assertEqual(whatsApp.numero_de_telefone_do_assistente, '123456123')

    @patch('requests.post')
    def test_whatsapp_marque_mensagem_como_lida_funciona(self, mock_post):
        whatsApp = WhatsApp(self.msg, self.logger)
        whatsApp.marque_mensagem_como_lida()
        mock_post.assert_called_once_with(
            whatsApp.api_url,
            headers={'Authorization': f'Bearer {whatsApp.token}'},
            json={
                'messaging_product': 'whatsapp',
                'status': 'read',
                'message_id': 'ABGGFlA5Fpa',
            }
        )

    @patch('requests.post')
    def test_whatsapp_responda_mensagem_funciona(self, mock_post):
        whatsApp = WhatsApp(self.msg, self.logger)
        msg_enviada = 'olá, Professor'
        whatsApp.responda_mensagem(msg_enviada)
        mock_post.assert_called_once_with(
            whatsApp.api_url,
            headers={'Authorization': f'Bearer {whatsApp.token}'},
            json={
                'messaging_product': 'whatsapp',
                'to': whatsApp.numero_de_telefone_do_professor,
                'text': {'body': msg_enviada}
            }
        )








