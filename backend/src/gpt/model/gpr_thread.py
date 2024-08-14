import json


class ModelGptThread():
    def __init__(self):
        self.id_thread  = None
        self.professor_id = None
        self.thread_codigo = None


    def m_to_json(self):
        return json.dumps(
            {
                'self.id_thread'     : self.id_thread,
                'self.professor_id'  : self.professor_id,
                'self.thread_codigo' : self.thread_codigo
            }
        ) 


    def __str__(self):
        txt = self.m_to_json()
        txt = txt.replace("{", "{\n")
        txt = txt.replace("}", "\n}")
        txt = txt.replace(",", ",\n")
        return txt

