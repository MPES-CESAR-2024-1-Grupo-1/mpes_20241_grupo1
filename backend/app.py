from flask import Flask, render_template, request
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix
import logging
import pytz

import markdown

from src.db import Database, init_db
from src.db.models import LogDeSolicitacao
from src.gpt.gpt_api import GptApi
from src.gpt.EventHandler import EventHandler
from src.persona.persona_builder import PersonaBuilder

# PARA DEBUG APAGAR
from src.gpt.model.professor import ModelProfessor
from src.gpt.model.assistente import ModelAssistente
from src.gpt.model.gpr_thread import ModelGptThread
from src.gpt.model.metrica_uso import ModelMetricaUso
from src.gpt.model.serie_ensino import ModelSerieEnsino
from src.whatsapp import WhatsApp
import os


# Definindo o fuso horário de Brasília
brasilia_tz = pytz.timezone('America/Sao_Paulo')

VERIFY_TOKEN = 'J2CQMTcPDBXuwo7fi7svBoiF'

app = Flask(__name__)

# Usa o logger do Gunicorn
gunicorn_logger = logging.getLogger("gunicorn.error")
app.logger.handlers.extend(gunicorn_logger.handlers)
app.logger.setLevel(logging.DEBUG)

app.wsgi_app = ProxyFix(app.wsgi_app)
CORS(app, resources={r"/*": {"origins": "*"}})

init_db()


@app.route('/')
def index():
    return '<h1>Api MPES 2024.1 Hello World! I have been seen times2.</h1>'

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

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

@app.route('/gpt')
def gpt_pergunta():
    with Database() as db:
        professor = db.carrega_ou_cria_professor('+5581982467019')
        persona = PersonaBuilder()
        persona.m_add_contexto_profissao(f"Professor de {professor.disciplina} da {professor.serie} do ensino fundamental do Brasil")
        persona.m_add_contexto_ambiente_or_tecnologias("receber material para realizar uma aula de 2 horas")
        pergunta = request.args.get('pergunta', 'sobre Mauricio de Nassau')
        gpt_api = GptApi()
        retorno = gpt_api.m_conversa(persona=persona, pergunta=pergunta, formato_json=True)
        db.salva_log_de_solicitacao(professor, retorno)
        return render_template("gpt.html", retorno=markdown.markdown(retorno['resposta']))


@app.route('/teste_conn')
def teste_criar_tb():
    query = "SELECT * FROM mpes.tb_teste;"

    with Database() as db:
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
        whatsapp = WhatsApp(
            mensagem_recebida=request.json
        )
        with Database() as db:
            professor = db.carrega_ou_cria_professor(whatsapp.numero_de_telefone_do_professor)
            persona = PersonaBuilder()
            persona.m_add_contexto_profissao(f"Professor de {professor.disciplina} da {professor.serie} do ensino fundamental do Brasil")
            persona.m_add_contexto_ambiente_or_tecnologias("receber material para realizar uma aula de 2 horas")
            gpt_api = GptApi()
            retorno = gpt_api.m_conversa(persona=persona, pergunta=whatsapp.texto_da_mensagem_recebida(), formato_json=True)
            whatsapp.marcar_como_lida()
            whatsapp.responder_mensagem(markdown.markdown(retorno['resposta']))
            db.salva_log_de_solicitacao(professor, retorno)
            return 'ok', 200




if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug= "--debug")
