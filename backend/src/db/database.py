# import pandas as pd
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv
from .models import Base, Professor, LogDeSolicitacao

load_dotenv()
class Database:
    def __init__(self):
        self.PSQL_HOST = os.getenv('PSQL_HOST')
        self.PSQL_USER = os.getenv('PSQL_USER')
        self.PSQL_PASS = os.getenv('PSQL_PASS')
        self.PSQL_DB   = os.getenv('PSQL_DB')
        self.PSQL_PORT = os.getenv('PSQL_PORT')
        self.engine = create_engine(f'postgresql+psycopg2://{self.PSQL_USER}:{self.PSQL_PASS}@{self.PSQL_HOST}:{self.PSQL_PORT}/{self.PSQL_DB}')
        Base.metadata.create_all(self.engine)


    def create_conexao_bd_postgresql(self):
        '''Cria a conexão para o postgresql do projeto'''
        return self.engine

    def salve(self, objeto: Base):
        self.sessao.add(objeto)

    def carrega_ou_cria_professor(self, numero_de_telefone) -> Professor:
        query = select(Professor).where(Professor.numero_de_telefone == numero_de_telefone)
        professor_do_banco = self.sessao.scalar(query)
        if professor_do_banco:
            return professor_do_banco
        novo_professor = Professor(
            nome=f"Professor Teste {numero_de_telefone}",
            numero_de_telefone=numero_de_telefone,
            disciplina="História",
            serie="Quarta Série"
        )
        self.salve(novo_professor)
        return novo_professor

    def salva_log_de_solicitacao(self, professor: Professor, dados):
        tema = dados.get('tema')
        if tema:
            professor.logs_de_solicitacao.append(LogDeSolicitacao(tema=tema))
            self.salve(professor)

    '''Funções para permitir uso com with:
        with Database() as db:
    '''
    def __enter__(self):
        self.sessao = Session(self.engine)
        self.sessao.begin()
        return self

    def __exit__(self, *args):
        self.sessao.commit()
        self.sessao.close()


def init_db():
    Database()