from src.database.models import Professor
from src.database import db
from sqlalchemy import select
from src.database.repositorios.base import RepositorioBase


class RepositorioProfessor(RepositorioBase):

    def carrega_ou_cria(self, numero_de_telefone) -> Professor:
        professor_do_banco = self.carrega_professor(numero_de_telefone)
        if professor_do_banco:
            return professor_do_banco
        novo_professor = Professor(
            numero_de_telefone=numero_de_telefone,
        )
        self.db.session.add(novo_professor)
        return novo_professor

    def carrega_professor(self, numero_de_telefone) -> Professor:
        query = select(Professor).where(Professor.numero_de_telefone == numero_de_telefone)
        return self.db.session.scalar(query)

    def salva_professor(self, professor: Professor):
        self.db.session.add(professor)
        return professor


repositorio_professor = RepositorioProfessor(db)
