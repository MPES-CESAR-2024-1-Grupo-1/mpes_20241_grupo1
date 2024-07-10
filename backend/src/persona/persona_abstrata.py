from abc import ABC, abstractmethod



class PersonaAbstrata(ABC):
    def __init__(self) -> None:
        pass


    @abstractmethod
    def m_add_contexto_profissao(self, txt_profissao: str):
        pass


    @abstractmethod
    def m_add_contexto_ambiente_or_tecnologias(self, txt_ambiente_or_tecnologias: str):
        pass


    @abstractmethod
    def m_get_contexto(self):
        '''Retorna o contesto criado.'''
        pass
            
