import os
from dotenv import load_dotenv
from .models import Base, Professor, LogDeSolicitacao, ThreadOpenAI
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

load_dotenv("development.env")

__PSQL_HOST = os.getenv('PSQL_HOST')
__PSQL_USER = os.getenv('PSQL_USER')
__PSQL_PASS = os.getenv('PSQL_PASS')
__PSQL_DB   = os.getenv('PSQL_DB')
__PSQL_PORT = os.getenv('PSQL_PORT')
__DB_URL = f'postgresql+psycopg2://{__PSQL_USER}:{__PSQL_PASS}@{__PSQL_HOST}:{__PSQL_PORT}/{__PSQL_DB}'

db = SQLAlchemy(model_class=Base)
migrate = Migrate()

def init_database(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = __DB_URL
    db.init_app(flask_app)
    migrate.init_app(app=flask_app, db=db)
    # with flask_app.app_context():
    #     db.drop_all()
