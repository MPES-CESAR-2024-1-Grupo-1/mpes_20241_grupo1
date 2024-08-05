
class PersonaBuilder():
    def __init__(self) -> None:
        self.context = []

    def m_add_contexto_profissao(self, txt_profissao: str):
        self.context.append(txt_profissao)
        return self


    def m_add_contexto_ambiente_or_tecnologias(self, txt_ambiente_or_tecnologias: str):
        self.context.append(txt_ambiente_or_tecnologias)
        return self


    def m_get_contexto(self):
        '''Retorna o contesto criado.'''
        txt_contexto = ""
        for i, value in enumerate(self.context):
            # print(i)
            # print(value)

            if i == 0:
                txt_contexto = value
                continue 
            
            if i == self.context.__len__() -1:
                txt_contexto += " " + value + "."
                continue
            txt_contexto += " " + value

        # print(txt_contexto)
        return txt_contexto
                    
            



#  messages=[
#     {"role": "system", "content": "Você é um programador que trabalha com Springboot3 com java."},
#     {"role": "user", "content": "como configurar um banco de dados postgres que tem um schema."}
#   ],