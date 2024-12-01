from src.database.repositorios.base import RepositorioBase
from src.database import db, ThreadOpenAI
from sqlalchemy import select, text
from datetime import datetime
import os

TEMPO_VALIDADE_THREAD = os.environ.get('TEMPO_VALIDADE_THREAD_EM_MINUTOS', 5)

class RepositorioThreadOpenai(RepositorioBase):

    def thread_valida_do_professor(self, professor):
        return self.db.session.scalar(
            select(ThreadOpenAI)
            .from_statement(
                text(f'''
                    SELECT * FROM thread_openai
                     WHERE id_professor = :id_professor 
                        AND timestamp_ultima_interacao > :timestamp_atual - INTERVAL '{TEMPO_VALIDADE_THREAD} minutes'
                        AND finalizada = FALSE
                     ORDER BY timestamp_ultima_interacao DESC LIMIT 1
                 ''')
            ).params(id_professor=professor.id, timestamp_atual=datetime.now())
        )

    def crie_thread(self, professor, openai_thread_id):
        thread = ThreadOpenAI(id_professor=professor.id, id_openai=openai_thread_id)
        return self.salve(thread)

    def salve(self, thread):
        self.db.session.add(thread)
        return thread


repositorio_thread_openai = RepositorioThreadOpenai(db)
