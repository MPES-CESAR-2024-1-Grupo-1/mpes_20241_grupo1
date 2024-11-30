from openai import OpenAI
import os, json
from logging import Logger
from datetime import datetime
from src.database import Professor, ThreadOpenAI
from src.database.repositorios import RepositorioThreadOpenai


class ResultadoAssistente:
    """
    Classe que representa o resultado de uma interação com o assistente
    """
    def __init__(self, resposta):
        self.nome_professor = resposta.get('nome')
        self.disciplina_professor = resposta.get('disciplina')
        self.serie_professor = resposta.get('ano_letivo')
        self.tipo_pedido = resposta.get('tipo')
        self.tema_pedido = resposta.get('tema')
        self.avaliacao_nota = resposta.get('avaliacao', {}).get('nota')
        self.avaliacao_comentario = resposta.get('avaliacao', {}).get('mensagem')
        self.textos = [r.get('texto') for r in resposta.get('respostas', [{}]) if r.get('texto') is not None]

class Assistente:
    """
    Classe que representa um assistente de IA da OpenAI
    - Inicializa o assistente com as credenciais da OpenAI (OPEN_AI_API_KEY)
    - Necessita de um assistente_id para funcionar (OPEN_AI_ASSISTANT_ID)


    """
    def __init__(self, repositorio_thread_openai: RepositorioThreadOpenai, professor: Professor, logger: Logger):
        self.id_assistente = os.environ.get('OPENAI_ASSISTANT_ID')
        self.openai = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
        self.professor = professor
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
        self.logger.debug(f"[assistente] Usando Thread {thread}")
        self.openai.beta.threads.messages.create(
            # TODO: mover instrucoes do professor para additional_instructions e validar se já funciona
            thread_id=thread.id_openai, content=f"{self.__instrucoes_professor(professor)}{mensagem}", role="user"
        )
        run = self.openai.beta.threads.runs.create_and_poll(
            thread_id=thread.id_openai,
            assistant_id=self.id_assistente,
            # additional_instructions=self.__instrucoes_professor(professor),<- Não funciona
        )
        if run.status == "completed":
            respostas = self.openai.beta.threads.messages.list(
                thread_id=thread.id_openai,
                extra_query={"run_id": run.id}
            )
            self.logger.debug(f"[assistente] Respostas: {respostas}")
            resultado = ResultadoAssistente(json.loads(respostas.data[0].content[0].text.value))
            self.__atualiza_thread(thread, resultado)
            return resultado

    def __atualiza_thread(self, thread: ThreadOpenAI, resultado: ResultadoAssistente):
        thread.timestamp_ultima_interacao = datetime.now()
        if resultado.tipo_pedido:
            thread.tipo = resultado.tipo_pedido
        if resultado.tema_pedido:
            thread.tema = resultado.tema_pedido
        if resultado.avaliacao_nota:
            thread.avaliacao_nota = resultado.avaliacao_nota
        if resultado.avaliacao_comentario:
            thread.avaliacao_comentario = resultado.avaliacao_comentario

        if resultado.avaliacao_nota and resultado.avaliacao_comentario:
            thread.finalizada = True
        self.logger.debug(f"[assistente] thread após execução -> {thread}")
        self.repo_thread_openai.salve(thread)

    def __instrucoes_professor(self, professor: Professor):
        instrucoes = ""
        if professor.nome:
            instrucoes += f"Meu nome é  {professor.nome}."
        if professor.disciplina:
            instrucoes += f"Sou professor de {professor.disciplina}."
        if professor.serie:
            instrucoes += f"Dou aula para alunos do {professor.serie}."
        return instrucoes



