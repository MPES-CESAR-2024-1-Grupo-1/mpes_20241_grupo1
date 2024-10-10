from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv
from .models import Base, Professor, LogDeSolicitacao
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

__PSQL_HOST = os.getenv('PSQL_HOST')
__PSQL_USER = os.getenv('PSQL_USER')
__PSQL_PASS = os.getenv('PSQL_PASS')
__PSQL_DB   = os.getenv('PSQL_DB')
__PSQL_PORT = os.getenv('PSQL_PORT')
__DB_URL = f'postgresql+psycopg2://{__PSQL_USER}:{__PSQL_PASS}@{__PSQL_HOST}:{__PSQL_PORT}/{__PSQL_DB}'

db = SQLAlchemy(model_class=Base)

def carrega_ou_cria_professor(numero_de_telefone) -> Professor:
    query = select(Professor).where(Professor.numero_de_telefone == numero_de_telefone)
    professor_do_banco = db.session.scalar(query)
    if professor_do_banco:
        return professor_do_banco
    novo_professor = Professor(
        nome=f"Professor Teste {numero_de_telefone}",
        numero_de_telefone=numero_de_telefone,
        disciplina="História",
        serie="Quarta Série"
    )
    db.session.add(novo_professor)
    return novo_professor

def salva_log_de_solicitacao(professor: Professor, resposta):
    tema = resposta.get('tema')
    if tema:
        professor.logs_de_solicitacao.append(LogDeSolicitacao(tema=tema))
        db.session.add(professor)


def init_database(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = __DB_URL
    db.init_app(flask_app)
    with flask_app.app_context():
        db.create_all()