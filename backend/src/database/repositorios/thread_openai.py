from src.database.repositorios.base import RepositorioBase
from src.database import db, ThreadOpenAI
from sqlalchemy import select, text
from datetime import datetime

class RepositorioThreadOpenai(RepositorioBase):

    def thread_valida_do_professor(self, professor):
        return self.db.session.scalar(
            select(ThreadOpenAI)
            .from_statement(
                text('''
                    SELECT * FROM thread_openai
                     WHERE id_professor = :id_professor AND timestamp_ultima_interacao > :timestamp_atual - INTERVAL '5 minutes'
                     ORDER BY timestamp_ultima_interacao DESC LIMIT 1
                 ''')
            ).params(id_professor=professor.id, timestamp_atual=datetime.now())
        )


    def crie_thread(self, professor, openai_thread_id):
        thread = ThreadOpenAI(id_professor=professor.id, id_openai=openai_thread_id)
        self.db.session.add(thread)
        return thread


repositorio_thread_openai = RepositorioThreadOpenai(db)
