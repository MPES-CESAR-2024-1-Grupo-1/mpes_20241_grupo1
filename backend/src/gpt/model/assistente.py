import json


class ModelAssistente():
    def __init__(self):
        self.id_assistente    = None
        self.gpt_codigo       = None
        self.alias_str_numero = None
        self.descricao        = None


    def m_to_json(self):
        return json.dumps(
            {
            'id_assistente' : self.id_assistente,
            'gpt_codigo'         : self.gpt_codigo,
            'alias_str_numero'   : self.alias_str_numero,
            'descricao'          : self.descricao
            }
        ) 


    def __str__(self):
        txt = self.m_to_json()
        txt = txt.replace("{", "{\n")
        txt = txt.replace("}", "\n}")
        txt = txt.replace(",", ",\n")
        return txt

