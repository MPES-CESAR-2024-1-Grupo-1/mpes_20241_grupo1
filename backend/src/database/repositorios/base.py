from flask_sqlalchemy import SQLAlchemy


class RepositorioBase:
    def __init__(self, database: SQLAlchemy):
        self.db = database
