from src.database import LogDeSolicitacao, Professor, db
from src.database.repositorios.base import RepositorioBase


class RepositorioLogDeSolicitacao(RepositorioBase):

    def salva(self, professor: Professor, resposta):
        tema = resposta.get('tema')
        if tema:
            professor.logs_de_solicitacao.append(LogDeSolicitacao(tema=tema))
            self.db.session.add(professor)


repositorio_log_de_solicitacao = RepositorioLogDeSolicitacao(db)
