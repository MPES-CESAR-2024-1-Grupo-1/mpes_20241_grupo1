from flask import Flask, render_template, request
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix
import logging
import markdown
from flask.logging import default_handler
import traceback

from src.database import (
    db,
    init_database,
)
from src.database.repositorios import (
    repositorio_professor,
    repositorio_log_de_solicitacao,
    repositorio_thread_openai
)
from src.assistente.open_ai import Assistente
from src.gpt.gpt_api import GptApi
from src.persona.persona_builder import PersonaBuilder

from src.whatsapp import WhatsApp
import os

VERIFY_TOKEN = 'J2CQMTcPDBXuwo7fi7svBoiF'

app = Flask(__name__)
init_database(app)

# Usa o logger do Gunicorn em vez do logger padrão do Flask
gunicorn_logger = logging.getLogger("gunicorn.error")
app.logger.handlers.extend(gunicorn_logger.handlers)
app.logger.handlers.remove(default_handler)
app.logger.setLevel(logging.DEBUG)

app.wsgi_app = ProxyFix(app.wsgi_app)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def index():
    return render_template(
        "landing.html",
        assets_version=os.environ.get("HOSTNAME")
    )

@app.route('/debug')
def gpt_debug():
    # ROTA DE DEBUG

    return render_template("gpt.html", retorno="<h1>Rodou debug</h1>")


# TESTE DE FORMULÁRIO
@app.route('/form_teste', methods=['POST'])
def m_receber_dados():
    if request.method == 'POST':
        formulario = request.json

        print(formulario)
        print(formulario["pergunta"])

        persona = PersonaBuilder()
        persona.m_add_contexto_profissao("Professor de história da quarta série do ensino fundamental do Brasil")
        persona.m_add_contexto_ambiente_or_tecnologias("receber material para realizar uma aula de 2 horas")

        gpt_api = GptApi()
        retorno = gpt_api.m_conversa(persona=persona, pergunta=f"sobre {formulario['pergunta']}")
        retorno = markdown.markdown(retorno)
        return retorno


@app.route('/gpt_assist')
def gpt_assist():
    assistent_id = "asst_RybHhABngVJoOdkFmlJLGpkW"

    msg = "que eram os espartanos."
    # event_handler = EventHandler()

    gpt_api = GptApi()
    thread = gpt_api.m_criar_thread()
    gpt_api.m_adicionar_msg_thread(thread=thread, msg=msg)

    msg = gpt_api.m_run(thread=thread, assistant_id=assistent_id)

    # event_handler.m_conversa(client=gpt_api.CLIENT, thread=thread, assistant=assistent_id)

    print(msg)

    # retorno = gpt_api.m_conversa(persona=persona, pergunta="sobre Mauricio de Nassau")
    # msg = markdown.markdown( msg)
    return render_template("gpt.html", retorno=msg)


@app.route('/gpt')
def gpt_pergunta():
    professor = repositorio_professor.carrega_ou_cria('+5581982467019')
    persona = PersonaBuilder()
    persona.m_add_contexto_profissao(f"Sou Professor de {professor.disciplina} da {professor.serie} do ensino fundamental do Brasil")
    persona.m_add_contexto_ambiente_or_tecnologias("crie um material para realizar uma aula de 2 horas")
    pergunta = f"sobre {request.args.get('pergunta', 'Mauricio de Nassau')}"
    gpt_api = GptApi()
    retorno = gpt_api.m_conversa(persona=persona, pergunta=pergunta, formato_json=True)
    repositorio_log_de_solicitacao.salva(professor, retorno)
    db.session.commit()
    return render_template("gpt.html", retorno=markdown.markdown(retorno['resposta']))


@app.route('/teste_conn')
def teste_criar_tb():
    query = "SELECT * FROM mpes.tb_teste;"

    engine = db.engine
    '''Deve se Implementado, nesta Versão!'''
    df = engine.read_sql(query, engine)
    print(df)

    return render_template('hello.html',  person= df.to_json())


@app.route('/api/webhook', methods=['GET', 'POST'])
def webhook():
    # Resposta para validação de domínio feita pela Meta ao add um novo webhook
    if request.method == "GET":
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        else:
            return 'Validação falhou', 403

    if request.method == 'POST':
        try:
            whatsapp = WhatsApp(
                mensagem_recebida=request.json,
                logger=app.logger
            )
            if not whatsapp.mensagem_recebida_eh_valida():
                '''whatsapp envia confirmações de envio e entrega das respostas enviadas. Podemos ignorar.'''
                app.logger.debug("Mensagem recebida não é válida [Possívelmente delivery status]. Encerrando execução")
                return 'ok', 200
            whatsapp.marque_mensagem_como_lida()
            professor = repositorio_professor.carrega_ou_cria(whatsapp.numero_de_telefone_do_professor)
            assistente = Assistente(
                repositorio_thread_openai=repositorio_thread_openai,
                professor=professor,
                logger=app.logger)
            resultado = assistente.responda(mensagem=whatsapp.texto_da_mensagem_recebida(), professor=professor)
            if resultado.nome_professor and not professor.nome:
                professor.nome = resultado.nome_professor
            if resultado.disciplina_professor and not professor.disciplina:
                professor.disciplina = resultado.disciplina_professor
            if resultado.serie_professor and not professor.serie:
                professor.serie = resultado.serie_professor
            app.logger.debug(f"Professor após execução -> {professor}")
            for textos in resultado.textos:
                whatsapp.responda_mensagem(textos)
            db.session.commit()
        except Exception as e:
            app.logger.error(f"Erro ao executar o Assistente: {e}")
            traceback.print_exc()
        return 'ok', 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug= "--debug")
