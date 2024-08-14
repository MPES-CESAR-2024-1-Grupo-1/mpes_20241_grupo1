import json


class ModelProfessor():
    def __init__(self):
        self.id_professor    = None
        self.numero_telefone = None
        self.email           = None
        self.descricao       = None


    def m_to_json(self):
        return json.dumps(
            {
                "id_professor"    : self.id_professor,
                "numero_telefone" : self.numero_telefone,
                "email"           : self.email,
                "descricao"       : self.descricao
            }
        ) 


    def __str__(self):
        txt = self.m_to_json()
        txt = txt.replace("{", "{\n")
        txt = txt.replace("}", "\n}")
        txt = txt.replace(",", ",\n")
        return txt


