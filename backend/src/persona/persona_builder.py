
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
        '''Retorna o contexto criado.'''
        txt_contexto = ""
        ultimo_indice = self.context.__len__() -1
        for i, item_contexto in enumerate(self.context):
            txt_contexto += item_contexto
            if i < ultimo_indice:
                txt_contexto += ', '
            elif i == ultimo_indice:
                txt_contexto += '.'
        return txt_contexto
