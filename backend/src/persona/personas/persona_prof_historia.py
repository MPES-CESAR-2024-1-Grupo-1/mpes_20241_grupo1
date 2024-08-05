from src.persona.persona_abstrata import PersonaAbstrata
from src.persona.persona_builder import PersonaBuilder


class PersonaProfHistoria(PersonaAbstrata):
    def __init__(self) -> None:
        super().__init__()
        self.builder = PersonaBuilder()

    


