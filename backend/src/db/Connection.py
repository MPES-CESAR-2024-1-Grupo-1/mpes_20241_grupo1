# import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()


class Connection:
    def __init__(self):
        self.PSQL_HOST = os.getenv('PSQL_HOST')
        self.PSQL_USER = os.getenv('PSQL_USER')
        self.PSQL_PASS = os.getenv('PSQL_PASS')
        self.PSQL_DB   = os.getenv('PSQL_DB')
        self.PSQL_PORT = os.getenv('PSQL_PORT')


    # def create_conexao_bd_sqlite(self):
    #     '''Cria a conexão para sqlite local no projeto'''
    #     # engine = create_engine('sqlite:///banco_projeto.db')
    #     engine = create_engine('sqlite:///src/db/banco_projeto.db')
    #     return engine


    def create_conexao_bd_postgresql(self):
        '''Cria a conexão para o postgresql do projeto'''
        engine = create_engine(f'postgresql+psycopg2://{self.PSQL_USER}:{self.PSQL_PASS}@{self.PSQL_HOST}:{self.PSQL_PORT}/{self.PSQL_DB}')
        return engine
