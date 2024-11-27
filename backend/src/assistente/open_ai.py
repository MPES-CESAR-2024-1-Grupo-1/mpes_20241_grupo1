from openai import OpenAI
import os
from logging import Logger

from src.database import Professor
from src.database.repositorios import RepositorioThreadOpenai


class Assistente:
    """
    Classe que representa um assistente de IA da OpenAI
    - Inicializa o assistente com as credenciais da OpenAI (OPEN_AI_API_KEY)
    - Necessita de um assistente_id para funcionar (OPEN_AI_ASSISTANT_ID)


    """
    def __init__(self, repositorio_thread_openai: RepositorioThreadOpenai, logger: Logger):
        self.id_assistente = os.environ.get('OPENAI_ASSISTANT_ID')
        self.openai = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
        self.logger = logger
        self.repo_thread_openai = repositorio_thread_openai


    def responda(self, mensagem: str, professor: Professor):
        """
        Responde a mensagem do professor

        :param mensagem: Mensagem do professor
        :param professor: Professor que está fazendo a pergunta
        :return: Resposta do assistente
        """
        thread = self.repo_thread_openai.thread_valida_do_professor(professor)
        if not thread:
            self.logger.debug(f"[assistente] Criando nova thread para o professor {professor.id}")
            thread = self.repo_thread_openai.crie_thread(
                professor=professor, openai_thread_id=self.openai.beta.threads.create().id
            )
            self.logger.debug(f"[assistente] Nova thread criada {thread}")

        self.openai.beta.threads.messages.create(
            thread_id=thread.id_openai, content=mensagem, role="user"
        )
        run = self.openai.beta.threads.runs.create_and_poll(
            thread_id=thread.id_openai,
            assistant_id=self.id_assistente,
            instructions=self.__instrucoes_professor(professor),
        )
        if run.status == "completed":
            respostas = self.openai.beta.threads.messages.list(
                thread_id=thread.id_openai,
                extra_query={"run_id": run.id}
            )
            self.logger.debug(f"[assistente] Respostas: {respostas}")

    def __instrucoes_professor(self, professor: Professor):
        instrucoes = ""
        if professor.nome:
            instrucoes += f"Professor se chama {professor.nome}."
        if professor.disciplina:
            instrucoes += f"Professor leciona {professor.disciplina}."
        if professor.serie:
            instrucoes += f"Professor leciona na {professor.serie}."
        return instrucoes

