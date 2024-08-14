import json


class ModelSerieEnsino():
    def __init__(self):
        self.id_serie_ensino  = None
        self.alias_str_numero = None


    def m_to_json(self):
        return json.dumps(
            {
                'id_serie_ensino' : self.id_serie_ensino,
                'alias_str_numero' : self.alias_str_numero 
            }
        ) 


    def __str__(self):
        txt = self.m_to_json()
        txt = txt.replace("{", "{\n")
        txt = txt.replace("}", "\n}")
        txt = txt.replace(",", ",\n")
        return txt

