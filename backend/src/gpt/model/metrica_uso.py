import json


class ModelMetricaUso():
    def __init__(self):
        self.id_metrica_uso  = None
        self.professor_id    = None
        self.serie_ensino_id = None
        self.dt_uso          = None


    def m_to_json(self):
        return json.dumps(
            {
                'id_metrica_uso' : self.id_metrica_uso,
                'professor_id' : self.professor_id,
                'serie_ensino_id' : self.serie_ensino_id,
                'dt_uso' : self.dt_uso
            }
        ) 


    def __str__(self):
        txt = self.m_to_json()
        txt = txt.replace("{", "{\n")
        txt = txt.replace("}", "\n}")
        txt = txt.replace(",", ",\n")
        return txt


